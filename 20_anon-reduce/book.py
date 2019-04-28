# Team Reduce Reuse Recycle -- Simon Tsui and Jason Lin
# SoftDev2 pd7
# K20 -- Reductio ad Absurdum
# 2019-04-17

from functools import reduce
import string

f = open("tom.txt",'r', encoding="utf8")
words = f.read()
for c in string.punctuation+"“”":
    words = words.replace(c," ")
words = words.split()
f.close()
# print(words)

# Adds one to the current count if the word is the same as the input
# reduce solution
def word_freq(word):
    return reduce((lambda x,y : x+1 if y.lower() == word else x),words,0)
# print(word_freq("entirely"))

# listcompy solution
def wordFreq(word):
    temp = [1 for x in words if x.lower() == word]
    return sum(temp)
print(wordFreq("the"))

# Use list comprehension to create a sliding window that adds a 1 if it finds the
# phrase and 0 if it doesn't match. Then use reduce to add up all the 1s.

#reduce solution
def phrase_freq(phrase):
    phrase = phrase.split()
    return reduce((lambda x,y: x+y),[1 if words[i:i+len(phrase)] == phrase\
                                       else 0\
                                       for i in range(len(words)-len(phrase)+1)],0)
# print(phrase_freq("in the"))

#listcompy solution
def phraseFreq(phrase):
    phrase = phrase.split()
    temp = [1 for i in range(len(words) - len(phrase) + 1) if words[i:i+len(phrase)] == phrase ]
    return sum(temp)
print(phrase_freq("in the"))



def incr_dict(dict, word):
    new_dict = dict.copy()
    word = word.lower()
    if word in new_dict.keys():
        new_dict[word] = new_dict[word] + 1
    else:
        new_dict[word] = 1
    return new_dict

# Goes through the entire book once and counts the occurance of each word in a dictionary
# Then find the highest frequency word
def get_most_frequent():
    all_word_freq = reduce((lambda x,y: incr_dict(x,y)), words, {"+":-1})
    return reduce((lambda a,b: [b,all_word_freq[b]] if all_word_freq[b] > a[1] else a),all_word_freq.keys(),['',0])

print(get_most_frequent())
