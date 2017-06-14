'use strict'

var lib = require('./lib/lib.js');
// Модуль для работы с файловой системой
var fs = require('fs');

const STEPS = 10;
var population = [],
    state;

fs.appendFileSync('population.txt', 'POPULATION\n');
for (var i = 0; i < STEPS; i++) {
    state = lib.getNewState();
    population.push(state);

    fs.appendFileSync('population.txt', state);
    fs.appendFileSync('population.txt', '\n');
}

fs.appendFileSync('population.txt', '\n');
fs.appendFileSync('population.txt', '\n');
fs.appendFileSync('population.txt', '\n');
fs.appendFileSync('population.txt', 'CROSSING\n');

population = lib.crossing(population);
population.forEach(function(item) {
    fs.appendFileSync('population.txt', item);
    fs.appendFileSync('population.txt', '\n');
})

fs.appendFileSync('population.txt', '\n');
fs.appendFileSync('population.txt', '\n');
fs.appendFileSync('population.txt', '\n');
fs.appendFileSync('population.txt', 'MUTATION\n');


population = lib.mutation(population);
population.forEach(function(item) {
    fs.appendFileSync('population.txt', item);
    fs.appendFileSync('population.txt', '\n');
})
