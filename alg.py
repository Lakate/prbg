#!/usr/bin/env python

from random import choice
import randtest

DEFAULT_RULE = "{0:b}".format(30)
POPULATION_SIZE = 5000
START_POPULATION_COUNT = 10
MUTATION_MAX_COUNT = 10 # 10%
current_state = None

TESTS = [
    'monobitfrequencytest',\
    'blockfrequencytest',\
    'runstest',\
    'longestrunones128',
    'binarymatrixranktest',\
    'spectraltest',\
    'nonoverlappingtemplatematchingtest',\
    'overlappingtemplatematchingtest',\
    # 'maurersuniversalstatistictest',\
    'linearcomplexitytest',\

    # works
    # 'randomexcursionstest',\
    # 'randomexcursionsvarianttest',\
    # 'lempelzivcompressiontest'\
]

def setRule():
    prefix = ''.join(['0'] * (8 - len(DEFAULT_RULE)))
    rule = prefix + DEFAULT_RULE

    return {
        '111': rule[0] or 0,
        '110': rule[1] or 0,
        '101': rule[2] or 0,
        '100': rule[3] or 0,
        '011': rule[4] or 0,
        '010': rule[5] or 0,
        '001': rule[6] or 0,
        '000': rule[7] or 0
    }

def getNewState():
    global current_state

    if current_state == None:
        current_state = getRandomInitialState()
    else:
        current_state = calculateState()

    return current_state

def getRandomInitialState():
    state = []
    # state = [1, 1, 1, 1, 0, 0, 1, 1, 1, 1]

    for i in range(0, POPULATION_SIZE):
        state.append(choice([0, 1]))

    return state

def getCellValue(left, current, right):
    rule = setRule()
    key = ''.join([str(left), str(current), str(right)])

    return rule[key]

def calculateState():
    newState = []
    firstArg = None
    secondArg = None

    for i in range(0, POPULATION_SIZE):
        if i == 0:
            firstArg = current_state[POPULATION_SIZE - 1]
        else:
            firstArg = current_state[i - 1]

        if i == POPULATION_SIZE - 1:
            secondArg = current_state[0]
        else:
            secondArg = current_state[i + 1]

        newState.append(getCellValue(firstArg, current_state[i], secondArg))

    return newState

def mutate(population):
    mutation_count = len(population) / MUTATION_MAX_COUNT

    print(mutation_count)

    for i in range(mutation_count):
        mutateted_gen = choice(range(0, len(population)))
        mutated_index = choice(range(0, POPULATION_SIZE))
        # mutation_value = #choice(range(0, 1))

        file.write('MUTATE: gen ' + str(mutateted_gen) +
         ' index ' + str(mutated_index) + '\n')

        population[mutateted_gen][mutated_index] = str(1 - int(population[mutateted_gen][mutated_index]))

    return population

def cross(population):
    new_population = []
    split_index = choice(range(0, POPULATION_SIZE, 1))
    parts = []

    file.write('SPLIT INDEX: ' + str(split_index) + '\n')

    for i in range(0, len(population), 2):
        parts = population[i][:split_index] + population[i + 1][split_index:]
        new_population.append(parts)

        parts = population[i + 1][:split_index] + population[i][split_index:]
        new_population.append(parts)

    return new_population

def printEmptyLine(text):
    for i in range(0, 5):
        file.write('\n')

    file.write(text + '\n')

def printCurrentPopulation(population):
    for state in population:
        for index in state:
            file.write(str(index))

        file.write('\n')

file = open('population.txt', 'w')
population = []
cross_population = []
mutate_population = []
state = None

# Set initial population
file.write('INITIAL POPULATION\n')
for i in range(0, 10):
    state = getNewState()
    population.append(state)

    for index in state:
        file.write(str(index))

    file.write('\n')

printEmptyLine('CROSS')
cross_population = cross(population)
printCurrentPopulation(cross_population)

printEmptyLine('MUTATE')
mutate_population = mutate(cross_population)
printCurrentPopulation(mutate_population)

printEmptyLine('SELECT')
for state in mutate_population:
    # for test in TESTS:
    #     file.write(test + ' ' + str(eval("randtest." + test)(state)) + '\n')
    print('randgen ', randtest.maurersuniversalstatistictest(state))
    file.write('\n')

file.close()
