#!/usr/bin/python

# based on poemgen.py - Allison Nelson

"""
nouns = ["flower","tree","child","sun","moon","darkness","light","rain","beach","earth","dog","cat","lover","life","love","heart","fish","poetry","music","happiness","peace","serenity","quiet","blossoms","blooms","madness","anger","sadness","dance","books"] #1	
verbs = ["feel","is","smell","touch","taste","smile","wave","run","live","breathe","jump","caress","love","kiss","hear","hold"] #2
articles = ["the","a"] #3
prepositions = ["on","with","under","in","to","into"] #4
adjectives = ["beautiful","shining","slow","lovely","lively","nice","sad"] #5
gerunds = ["leaping","growing","loving","shaking","making","living","being","thinking","doing","building","singing"] #6
conjunctions = ["and","or"] #7
"""

ADJECTIVE=["blank", "sad", "void", "barren", "broken", "hollow","forsaken","righteous"]
NOUN = ["face", "sight", "destiny", "soul","sorrow","ghost","savior","man","lies"]
LOCATION = ["castle","mist","wastelands","window","grave","time"]
ACTION3 = ["disappears","cries","flees","dies","laments","weeps","bleeds"]
ACTION = ["counting","searching","wandering"]

"""
#each number refers to a part of speech listed above, commas are interpreted literally
sentence_structures = ["35124351","314351","64351","63514351,676","3517351,6","6351,676","3512","3124351"]

struct = choice(sentence_structures)
"""

from random import choice

structure = 	[	"adjective","noun","in the","noun","br",
			"made","adjective","in the","location","br",
			"3action","and","3action","br",
			"action","noun",",","action","noun"
		]

def parse_structs():
    line = []
    for i in range(0,len(structure)):
        curr = structure[i]
        if curr == 'adjective':
                line.append(choice(ADJECTIVE))
        elif curr == 'noun':
                line.append(choice(NOUN))
        elif curr == '3action':
                line.append(choice(ACTION3))
        elif curr == 'action':
                line.append(choice(ACTION))
        elif curr == 'location':
                line.append(choice(LOCATION))
        elif curr == "br":
                line.append("\n")
        else:
                line.append(curr)

        if i == 0:
                line[0]=line[0][0].capitalize()+line[0][1:]
        elif curr != ",":
                line.insert(len(line)-1," ")
    return line

import sys
sys.stdout.write("\n")

"""
for i in range(0,5):
    struct = choice(sentence_structures)
    line = parse_structs(sentence_structures)
    print ''.join(line)
"""
poem = parse_structs()
print "".join(poem)
sys.stdout.write("\n")



