#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url + process.argv[2] + '/', (err, res, bdy) => {
  if (err) throw err;

  console.log(JSON.parse(bdy).title);
});
