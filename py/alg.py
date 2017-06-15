#!/usr/bin/env python

from random import choice
import randtest

DEFAULT_RULE = "{0:b}".format(30)
POPULATION_SIZE = 10
START_POPULATION_COUNT = 10
MUTATION_MAX_COUNT = 10 # 10%
current_state = None

tests= [
    'monobitfrequencytest',\
    'blockfrequencytest',\
    'runstest',\
    'longestrunones10000',
    'binarymatrixranktest',\
    'spectraltest',\
    'nonoverlappingtemplatematchingtest',\
    'overlappingtemplatematchingtest',\
    'maurersuniversalstatistictest',\
    'linearcomplexitytest',\
    'serialtest',\
    'aproximateentropytest',\
    'cumultativesumstest',\
    'randomexcursionstest',\
    'randomexcursionsvarianttest',\
    'cumultativesumstestreverse',\
    'lempelzivcompressiontest'\
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
    state = [1, 1, 1, 1, 0, 0, 1, 1, 1, 1]

    # for i in range(0, POPULATION_SIZE):
    #     state.append(choice([0, 1, 1]))

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


file = open('population.txt', 'w')
population = []
cross_population = []
mutate_population = []
state = None

# Set initial population
for i in range(0, 10):
    state = getNewState()
    population.append(state)

    for index in state:
        file.write(str(index))

    file.write('\n')

file.write('\n')
file.write('\n')
file.write('\n')
file.write('CROSS\n')

# Cross -> Mutate -> Select
cross_population = cross(population)

for state in cross_population:
    for index in state:
        file.write(str(index))

    file.write('\n')

file.write('\n')
file.write('\n')
file.write('\n')
file.write('MUTATE\n')

mutate_population = mutate(cross_population)

for state in mutate_population:
    for index in state:
        file.write(str(index))

    file.write('\n')

file.write('\n')
file.write('\n')
file.write('\n')
file.write('SELECT\n')

# for state in mutate_population:
#     # for test in tests:
#         # file.write(test + ' ' + str(eval("randtest." + test)(state)) + '\n')
#     file.write('randgen ' + randtest.randgen(state) + '\n')

file.close()

# def mutate(member):
#   # record it into the genes
#   input_str = member.get_appearance()
#   genes = member.get_genes()
#   genes.append(input_str)

#   # modify the string appearance
#   input_str = list(input_str)
#   max_index = len(input_str)
#   mutated_index = choice(range(0,max_index))
#   mutation_char = choice(ascii_lowercase + " ")
#   output_str    = input_str[:]
#   output_str[mutated_index] = mutation_char
#   output_str = "".join(output_str)

#   # create a new mutated creature
#   mutated = Creature(output_str, genes)
#   return mutated

# def reproduce(member, k):
#   output = []
#   for i in range(0,k):
#     output.append(mutate(member))
#   return output

# def select(offsprings, selection, size):
#   survival_value = map(lambda x: (match(x, selection), x), offsprings)
#   select      = list(map(lambda xy: xy[1], sorted(survival_value)[:size]))
#   return select

# # generaction is the current set of strings
# # offspring_size is the number of mutations
# def next_generation(generation, offspring_size, survival_size, selection_word):
#   offsprings = []
#   for member in generation:
#     offsprings += reproduce(member, offspring_size)
#   next_generation = select(offsprings, selection_word, survival_size)
#   return next_generation

# def isPresent(selection, generation):
#   selection_word = selection.appearance
#   generation_words = list(map(lambda x: x.appearance, generation))
#   if selection_word in generation_words:
#     return True
#   else:
#     return False

# def evolution(selection_word, max_num_generations=2000):
#   selection_word = selection_word.lower()
#   random = random_str(len(selection_word))
#   selection = Creature(selection_word, [])
#   root   = Creature(random,[])
# # print("Random word: " + random)
#   generation = [root]
#   num_of_offsprings = 100
#   num_of_select  = 10
#   generation_index  = 1
#   while True:
#     generation = next_generation(generation, num_of_offsprings, num_of_select, selection)
#     if isPresent(selection,generation):
#       break
#     generation_index += 1
#     if generation_index > max_num_generations:
#       raise Exception("Not reached in the maximal number of generations")
#   return generation[0], generation_index

# def print_evolution(sentence):
#   out = evolution(sentence)
#   number_of_generations = out[1]
#   best = out[0]
#   print(str(number_of_generations) + ","+ best.appearance)

# def print_genes(sentence):
#   out = evolution(sentence)
#   best = out[0]
#   for gene in best.genes:
#     print(gene)
#   print(best.appearance)

