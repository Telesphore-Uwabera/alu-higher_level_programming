#!/usr/bin/node

const request = require('request');

if (process.argv.length > 2) {
  const apiUrl = process.argv[2];
  function isWedgeAntillesPresent (movie) {
    const wedgeAntillesId = 18;
    return movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`);
  }

  request.get(apiUrl, (error, response, body) => {
    if (error) {
      console.error(`An error occurred while making the request: ${error}`);
    } else if (response.statusCode !== 200) {
      console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
    } else {
      const movies = JSON.parse(body).results;
      const moviesWithWedgeAntilles = movies.filter(isWedgeAntillesPresent);
      console.log(moviesWithWedgeAntilles.length);
    }
  });
} else {
  console.log('Please provide the API URL as an argument.');
}
