#!/usr/bin/node

const request = require('request-promise');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

async function getCharacterNames(characterUrls) {
  const names = await Promise.all(
    characterUrls.map(async (characterUrl) => {
      try {
        const characterData = await request.get(characterUrl);
        return JSON.parse(characterData).name;
      } catch (error) {
        console.error(`Error fetching character data: ${error}`);
        return null;
      }
    })
  );
  return names.filter((name) => name !== null);
}

async function main() {
  try {
    const movieData = await request.get(url);
    const content = JSON.parse(movieData);
    const characters = content.characters;
    
    console.log(`Characters in "${content.title}":`);
    
    const characterNames = await getCharacterNames(characters);
    characterNames.forEach((name) => console.log(name));
  } catch (error) {
    console.error(`Error fetching movie data: ${error}`);
  }
}

main();
