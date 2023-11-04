# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 20:55:42 2022

@author: George Kordonis
"""
import re

"""this is a function that receives an import text in Greek or English.
    It turns Uppercase to lowercase, it removes each word which isn't all Greek 
    , it recognises and counts specific Connectors and returns the percentage 
    of the """
def TxtProc(import_text):
    lowercase_text = import_text.lower()
    word_list=re.sub("[^\w]", " ",lowercase_text).split()
    non_greek = []
    for i in word_list:
        x = re.search('[a-z]',i)
        if x: 
            non_greek.append(i)
            word_list.remove(i)
    
    targetlinks={'και':0, 'κι':0, 'ή':0, 'είτε':0, 'δηλαδή':0, 'πως':0, 'που':0, 'ότι':0}
    for j in (targetlinks):
        for k in (word_list):
            if k == j:
                targetlinks[j] = targetlinks[j] + 1
    
    numoflinks = 0
    for v in (targetlinks):
        numoflinks = targetlinks[v] +numoflinks
        
    percentage = 100* (numoflinks/len(word_list))
    rpercentage = round(percentage,2)
    
    return {'rpercentage':rpercentage,'non_greek':non_greek}
  

def TxtProc2(detailedOutput:bool):
    TxtToProcess='''Η δεκάδα των ταινιών που διεκδικούν το Όσκαρ καλύτερης 
ταινίας βρίθει ποικιλίας και αξίζει ειδικής μνείας για την ενσωμάτωση 
προϋπολογισμών διαφορετικών ταχυτήτων, ισορροπίας ανάμεσα σε americanικές, 
αγγλικές και μη αγγλόφωνες παραγωγές, δηλαδή εμπορικότατων και festivalικών ή 
ή ή ή film. δηλαδή'''
    if detailedOutput == False:
        return TxtProc(TxtToProcess)
    else:
        wordys =[]
        wordys =re.sub("[^\w]", " ",TxtToProcess).split()
        word_count = len(wordys)
        TxtProc(TxtToProcess)
        processed2 = TxtProc(TxtToProcess)
        targetlinkz={'και':0, 'κι':0, 'ή':0, 'είτε':0, 'δηλαδή':0, 'πως':0, 'που':0, 'ότι':0}
        for l in (targetlinkz):
           for m in (wordys):
               if l == m:
                    targetlinkz[l] = targetlinkz[l] + 1
        truelinksa = {}
        for p in targetlinkz:
            if targetlinkz[p]!=0:
                truelinksa.update({p:targetlinkz[p]})
        truelinklist= sorted(truelinksa.items(), key = lambda x:x[1], reverse=True)
        truelink ={}
        for x in range(len(truelinklist)):
            truelink.update(dict([truelinklist[x]]))
        #print(truelink)
        numoflinkz = 0
        for y in (targetlinkz):
            numoflinkz = targetlinkz[y] + numoflinkz
        return{'processed2':processed2,'word_count':word_count,'numoflinkz':numoflinkz,'truelink':truelink}
        
    

text1 = '''Πήγαν στην εκδρομή και οι τρεις, αλλά κι αυτός εδώ που σου δείχνω.
Ξέρω πως τώρα διαβάζει. Πώς να είναι άραγε; Μου είπε που πήρες και εσύ
μέρος στους αγώνες. Δεν ξέρω πού να πάω και κάθομαι εδώ προς το παρόν.
Ο αθλητής έπιασε το αccόντιο και το έρριξε μakρυά στο gήπεδο, gήπεδο'''
TxtProc(text1)

print('Input text processed = \"\n',text1,'\n\"')
pers1 = TxtProc(text1)
print('Percentage of conjuctions-to-search in text entered after cleaning =',pers1['rpercentage'],'%')
print('Non GR Tokens found =',pers1['non_greek'],'\n')

text2 ='''Ως έναν μεγάλο βαθμό, οι φετινές υποψηφιότητες των Oscαρ καλύπτουν
αξιοπρόσεκτα μεγάλη γκάμα γούστου και ύφους, με εκπροσώπους 
διαφορετικών ηλικιών και προέλευσης, με τις εκπλήξεις και τα 
snobαρίσματα μέσα στο παιχνίδι fυσικά, και αυτές είναι οι δέκα 
θεματικές των τάσεων που οδηγούν στην 95η απονομή των βραβείων της 
Ακαδημίας, στις 12 Μαρτίου.'''   
TxtProc(text2)

print('Input text processed = \"\n',text2,'\n\"')
pers2 = TxtProc(text2)
print('Percentage of conjuctions-to-search in text entered after cleaning =',pers2['rpercentage'],'%')
print('Non GR Tokens found =',pers2['non_greek'],'\n')



TxtToProcess='''Η δεκάδα των ταινιών που διεκδικούν το Όσκαρ καλύτερης 
ταινίας βρίθει ποικιλίας και αξίζει ειδικής μνείας για την ενσωμάτωση 
προϋπολογισμών διαφορετικών ταχυτήτων, ισορροπίας ανάμεσα σε americanικές, 
αγγλικές και μη αγγλόφωνες παραγωγές, δηλαδή εμπορικότατων και festivalικών ή 
ή ή ή φιλμ. δηλαδή'''
print('Input text processed = \"\n',TxtToProcess,'\n\"')
pers3 = TxtProc2(False)
print('Percentage of conjuctions-to-search in text entered after cleaning =',pers3['rpercentage'],'%')
print('Non GR Tokens found =',pers3['non_greek'],'\n')

TxtProc2(True)
print('Input text processed = \"\n',TxtToProcess,'\n\"')
pers4 = TxtProc2(True)
print('Word Count in cleaned text =',pers4['word_count'])
print('Conjuctions Count in cleaned text =',pers4['numoflinkz'])
print('Percentage of conjuctions-to-search in text entered after cleaning =',pers4['processed2']['rpercentage'],'%')
print('Conjuctions-Occurrence pairs in text entered after cleaning =' ,pers4['truelink'])
print('Non GR Tokens found =',pers4['processed2']['non_greek'],'\n')
