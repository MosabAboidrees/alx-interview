#!/usr/bin/node
// Importing the request module
const request = require('request');

// Movie ID from command line arguments
const movieId = process.argv[2];

// Construct the URL for the specific movie
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  // Parse the response body to JSON
  let data;
  try {
    data = JSON.parse(body);
  } catch (parseError) {
    console.error('Failed to parse JSON:', parseError);
    return;
  }

  // Array of character URLs
  const characters = data.characters;

  // Function to fetch and print each character's name in order
  function fetchCharacter(index) {
    if (index >= characters.length) {
      return;
    }

    request(characters[index], (err, res, body) => {
      if (err) {
        console.error(`Failed to fetch character: ${err.message}`);
        return;
      }

      try {
        const character = JSON.parse(body);
        console.log(character.name);
      } catch (parseError) {
        console.error(`Failed to parse character JSON: ${parseError.message}`);
      }

      fetchCharacter(index + 1); // Fetch the next character
    });
  }

  // Start fetching characters from the first index
  fetchCharacter(0);
});
