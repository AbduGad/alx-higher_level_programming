#!/usr/bin/node
const request = require( 'request' );
const process = require( "process" );

request(process.argv[2],  (err, res, body) => {
	console.log('code:', res.statusCode);
});
