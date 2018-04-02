from jellyfish import levenshtein_distance

correct_list = []
misspell_list = []
dictionary_list = []

with open ('correct.txt') as file:
    for line in file:
        correct_list.append(line.strip())

with open ('misspell.txt') as file:
    for line in file:
        misspell_list.append(line.strip())

with open ('dictionary.txt') as file:
    for line in file:
        dictionary_list.append(line.strip())

result = []

for mis in misspell_list:
    min = len(mis)
    min_index = 0
    for index, dic in enumerate(dictionary_list):
        distance = levenshtein_distance(mis, dic)
        if(distance < min):
            min_index = index
    result.append(min_index)
    print(min_index)

positive=0

for index, res in enumerate(result):
    if(dictionary_list[res] == correct_list[index]):
        positive += 1

accuracy = positive/len(misspell_list)

print(accuracy)

