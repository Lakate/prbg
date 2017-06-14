'use strict'

const DEFAULT_RULE = (30).toString(2);
const POPULATION_SIZE = 10;
var CURRENT_STATE = undefined;

exports.setRule = function(rule) {
    rule = rule || DEFAULT_RULE

    var prefix = Array(8 - rule.length).fill(0).join('')

    rule = prefix + rule

    return {
        '111': rule[0] | 0,
        '110': rule[1] | 0,
        '101': rule[2] | 0,
        '100': rule[3] | 0,
        '011': rule[4] | 0,
        '010': rule[5] | 0,
        '001': rule[6] | 0,
        '000': rule[7] | 0
    }
};

exports.getNewState = function() {
    if (!CURRENT_STATE) {
        CURRENT_STATE = module.exports.getRandomInitialState();
    } else {
        CURRENT_STATE = module.exports.calculateState();
    }

    return CURRENT_STATE
};

exports.getRandomInitialState = function() {
    var state = Array(POPULATION_SIZE)

    for (var i = 0; i < state.length; i++) {
        state[i] = Math.round(Math.random()); // {0, 1}
    }

    return state
};

exports.calculateState = function() {
    var newState = Array(POPULATION_SIZE)

    for (var i = 0; i < POPULATION_SIZE; i++) {
        newState[i] = module.exports.getCellValue(
            i === 0 ? CURRENT_STATE[POPULATION_SIZE - 1] : CURRENT_STATE[i - 1] | 0,
            CURRENT_STATE[i],
            i === POPULATION_SIZE - 1 ? CURRENT_STATE[0] : CURRENT_STATE[i + 1] | 0
        )
    }

    return newState
};

exports.getCellValue = function(left, current, right) {
    var rule = module.exports.setRule(),
        key = [left, current, right].join('')

    return rule[key]
};

// Скрещивание
exports.crossing = function(population) {
    var firstPopulation, secondPopulation,
        half = POPULATION_SIZE / 2,
        firstPart, thirdPart, newPopulation = [];

    for (var i = 0; i < population.length; i += 2) {
        firstPopulation = population[i];
        secondPopulation = population[i + 1];

        firstPart = firstPopulation.splice(0, half);
        thirdPart = secondPopulation.splice(0, half);

        newPopulation.push(firstPart.concat(secondPopulation));
        newPopulation.push(thirdPart.concat(firstPopulation));

        console.log(i);
    }

    return newPopulation;
};

// Мутация
exports.mutation = function(population) {
    const MUTATION_KOEF = 3;
    var index;

    for (var i = 0; i < MUTATION_KOEF; i++) {
        index = Math.random(0, POPULATION_SIZE); // {0, 1}
        // 0 -> 1 а 1 -> 0
        population[index] = 1 - population[index];
    }

    return population;
}


