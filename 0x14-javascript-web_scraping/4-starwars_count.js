#!/usr/bin/node
/**
 * prints the number of movies where the character “Wedge Antilles”
 * is present.
 */

const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (!err) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
