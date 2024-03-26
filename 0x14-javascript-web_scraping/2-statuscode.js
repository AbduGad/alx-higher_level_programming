#!/usr/bin/node
const process = require('process');
const request = require('request');

let url = process.argv[2];

request(url, function (error, response, body) {
  if (error != null) {
    console.log(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
/*const request = require('request');
const process = require('process');

request(process.argv[2], (err, res, body) => {
  if (err | !err) { console.log('code:', res.statusCode); }
});*/
