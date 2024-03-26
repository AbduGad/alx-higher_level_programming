#!/usr/bin/node
const request = require('request');
const urlElement = process.argv[2];
request.get(urlElement, function (error, response) {
  if (error) {
    return console.log(error);
  }
  console.log('code: %d', response && response.statusCode);
});
/*const request = require('request');
const process = require('process');

request(process.argv[2], (err, res, body) => {
  if (err | !err) { console.log('code:', res.statusCode); }
});*/
