#!/usr/bin/node
/**
 * Prints all characters of a Star Wars movie
 */

const { argv } = process;
const request = require('request');

const movieId = argv[2];

if (!movieId) {
  console.error('Usage: ./101-starwars_characters.js <Movie_ID>');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }
  const movieData = JSON.parse(body);
  const charactersPromises = movieData.characters.map(characterUrl => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          reject(charError);
        } else {
          const characterData = JSON.parse(charBody);
          resolve(characterData.name);
        }
      });
    });
  });
  Promise.all(charactersPromises)
    .then(characters => {
      characters.forEach(character => console.log(character));
    })
    .catch(error => {
      console.error('Error fetching character data:', error);
    });
});
