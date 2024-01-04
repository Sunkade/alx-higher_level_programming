#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);

    console.log(`Characters in "${movieData.title}":`);

    // Iterate through characters in the same order as listed in the /films/ response
    movieData.characters.forEach((characterUrl) => {
      request(characterUrl, (characterError, characterResponse, characterBody) => {
        if (characterError) {
          console.error(characterError);
        } else {
          const characterData = JSON.parse(characterBody);
          console.log(characterData.name);
        }
      });
    });
  }
});
