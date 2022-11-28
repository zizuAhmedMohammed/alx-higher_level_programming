#!/usr/bin/node
if (typeof(process.argv[2]) === String && process.argv.length > 3) console.log("Not a number");
else console.log("My number: ", Math.floor(process.argv[2]));
