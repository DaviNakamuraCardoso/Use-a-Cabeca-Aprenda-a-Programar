
import random


letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z','','','','','','','','','','',
            '','','','','','','','','','','','','']
syllables = []


def s_name(s):
    s = random.choice(list(range(0,9999)))
    return s

def syllable(s):
    while len(syllables) < 99999:
        syllable = str(random.choice(letters)) + str(random.choice(letters)) + str(random.choice(letters)) + str(random.choice(letters))
        syllables.append(syllable)

def syllables_count(word):
    syllables_counter = []
    while 'word' != str(syllables[s_name('a')]) + str(syllables[s_name('b')]) + str(syllables[s_name('c')]) + str(syllables[s_name('d')]) + str(syllables[s_name('e')]):
       composition == False 
    if composition == True:
        for n in range (0,9999):
            if syllables[n] != '':
                syllables_counter.append(syllables[n])

    return [len(syllables_counter) + 1]

test = syllables_count('test')
     
print(test)     
        
        
        
    
       
        
        
    




