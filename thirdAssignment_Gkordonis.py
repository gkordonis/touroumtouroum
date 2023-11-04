# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 21:52:09 2023

@author: George Kordonis
"""

class GetLinguisticInfo:
    def __init__(self, text):
        self.word_frequencies = {}
        self.words = []
        lower_text = text.lower()
        self.words = lower_text.split()
        
    '''Σε αυτή τη μέθοδο χρησιμοποιούμε το set ώστε να λάβουμε την κάθε
    λέξη της λίστας 1 φορά και στη συνέχεια γεμίζουμε το dictionary με την κάθε
    λέξη του set και με τον αριθμό 0. Έπειτα, μετράμε τον αριθμό των φορών
    που εμφανίζεται η κάθε λέξη στη λίστα μας και ενημερώνουμε το count της
    κάθε λέξης στο dictionary'''    
    def generate_frequencies(self):
        setofwords =set(self.words)
        count =0
        self.word_frequencies = {element: count for element in setofwords}
        for j in (self.word_frequencies):
            for i in (self.words):
                if i == j:
                    self.word_frequencies[j] = self.word_frequencies[j] + 1
        #print(self.word_frequencies)    
                    
    
    '''Σε αυτή τη μέθοδο ελέγχουμε αν η λέξη που μας δώθηκε υπάρχει στη λίστα μας
    και αν ναι, επιστρέφουμε τον αριθμό που έχουμε μετρήσει στο dictionary εναλ
    λακτικά επιστρέφουμε 0'''
    def get_frequency(self, word: str):
        if word in self.words:
            return self.word_frequencies[word]
        else:
            return 0 
        
    '''Σε αυτή τη μέθοδο επιστρέφουμε την λίστα μας '''        
    def get_words(self):
        return self.words
    


FirstText = GetLinguisticInfo('''In a hole in the ground there lived a hobbit. 
                         Not a nasty, dirty, wet hole, filled with the ends of 
                         worms and an oozy smell, nor yet a dry, bare, sandy 
                         hole with nothing IN it to sit down on or to eat: it 
                         was a hobbit-hole, and that means comfort''')
FirstText.generate_frequencies()
print(FirstText.get_frequency('test'))
print(FirstText.get_words())
print(FirstText.get_frequency('a'))