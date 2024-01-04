#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, { json: true }, (error, response, movieData) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`Characters in "${movieData.title}":`);

    // Iterate through characters in the same order as listed in the /films/ response
    const fetchCharacterData = (characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, { json: true }, (characterError, characterResponse, characterData) => {
          if (characterError) {
            reject(characterError);
          } else {
            resolve(characterData);
          }
        });
      });
    };

    const characterPromises = movieData.characters.map(fetchCharacterData);

    Promise.all(characterPromises)
      .then((characters) => {
        characters.forEach((character) => {
          console.log(character.name);
        });
      })
      .catch((err) => {
        console.error(err);
      });
  }
});
