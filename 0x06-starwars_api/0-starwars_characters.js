#!/usr/bin/node
// Importing the request module
const request = require('request');

// Movie ID from command line arguments
const movieId = process.argv[2];

// Construct the URL for the specific movie
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Fetch the movie data
request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  // Parse the response body to JSON
  const data = JSON.parse(body);

  // Loop over each character URL in the "characters" array
  const characters = data.characters;

  // Function to print character names in the order provided
  const printCharacters = async () => {
    for (const character of characters) {
      await new Promise((resolve) => {
        request(character, (err, res, body) => {
          if (err) {
            console.error(err);
            return;
          }
          console.log(JSON.parse(body).name);
          resolve();
        });
      });
    }
  };

  printCharacters();
});
