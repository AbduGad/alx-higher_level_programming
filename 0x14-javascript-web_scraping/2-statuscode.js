#!/usr/bin/node
const link = process.argv[2];
const req = require('request');
req(link, (error, response, body) => {
  if (error) throw error;
  console.log('code: ' + response.statusCode);
});
/*const request = require('request');
const process = require('process');

request(process.argv[2], (err, res, body) => {
  if (err | !err) { console.log('code:', res.statusCode); }
});*/
