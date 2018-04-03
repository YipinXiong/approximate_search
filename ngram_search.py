from operator import itemgetter
import ngram
import datetime

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
dic_gram = ngram.NGram(dictionary_list)
print(datetime.datetime.now().__str__())
for mis_index, mis in enumerate(misspell_list):
    #result.append([])
    mis_distance = dic_gram.search(mis)
    result.append(mis_distance)
    # result[mis_index] = sorted(result[mis_index], key=itemgetter(1), reverse=True)
    print(datetime.datetime.now().__str__())


return_guess = []
total_guess_len = 0
for word_index, sorted_dist_tuple in enumerate(result):
    return_guess.append([])
    for item in sorted_dist_tuple:
        if item[1] == sorted_dist_tuple[0][1]:
            return_guess[word_index].append(item[0])
        else:
            total_guess_len += len(return_guess[word_index])
            print(return_guess[word_index])
            break

positive=0
print(return_guess)

for pos, guesses in enumerate(return_guess):
    if(correct_list[pos] in guesses):
        positive += 1

precision = positive/total_guess_len
recall = positive/len(correct_list)
print("precision: ",precision)
print("recall:",recall) 
