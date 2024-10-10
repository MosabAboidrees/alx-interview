#!/usr/bin/python3
"""
0-lockboxes.py
Method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened."""
    n = len(boxes)
    opened_boxes = set([0])
    keys = boxes[0].copy()
    while keys:
        new_keys = []
        for key in keys:
            if 0 <= key < n and key not in opened_boxes:
                opened_boxes.add(key)
                new_keys.extend(boxes[key])
        keys = new_keys
    return len(opened_boxes) == n
