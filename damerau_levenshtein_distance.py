from jellyfish import damerau_levenshtein_distance
import datetime
start = datetime.datetime.now()
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

for mis_index, mis in enumerate(misspell_list):
    
    result.append([])
    for dic_index, dic in enumerate(dictionary_list):
        distance = damerau_levenshtein_distance(mis, dic)
        result[mis_index].append([distance, dic])
    result[mis_index].sort()

return_guess = []
total_guess_len = 0
for word_index, sorted_dist_list in enumerate(result):
    return_guess.append([])
    for item in sorted_dist_list:
        if item[0] == sorted_dist_list[0][0]:
            return_guess[word_index].append(item[1])
        else:
            total_guess_len += len(return_guess[word_index])
            print(return_guess[word_index])
            break

positive=0

for pos, guesses in enumerate(return_guess):
    if(correct_list[pos] in guesses):
        positive += 1

precision = positive/total_guess_len
recall = positive/len(correct_list)
print("precision: ",precision)
print("recall:",recall)
end = datetime.datetime.now()
print(start - end)

