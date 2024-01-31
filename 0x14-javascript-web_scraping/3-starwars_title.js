#!/usr/bin/node
/*
 * Displays title of a starwars movie where the episode number matches
 * a given integer
 */

const request = require('request');
const { argv } = process;
if (argv.length < 3) {
  console.error('Usage: ./3-starwars_title.js <episode_no>');
  process.exit(1);
}

const id = argv[2];
const link = 'https://swapi-api.alx-tools.com/api/films/';
request.get(`${link}${id}`, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const filmData = JSON.parse(body);
  const title = filmData.title;
  console.log(title);
});
