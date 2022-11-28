#!/usr/bin/node
import { argv } from 'node:process';
if (process.argv.arguments.length < 1) console.log('No argument');
else if (process.argv.arguments.length === 1) console.log('Argument found');
else console.log('Arguments found');
