def removeStopwords(d, stopwords):
    for word in stopwords:
        if word in d:
            d.remove(word)
    
    return ' '.join(d)



f = open('/Users/sanderlindberg/Dropbox/NTNU/Informatikk/H2019/TDT4117/stopwords.txt', 'r')
words = f.read().split('\n')
document = "BARCELONA Catalonia's regional leader opened the door to a unilateral declaration of independence from Spain on Sunday after voters defied a violent police crackdown and, according to regional officials, voted 90 percent in favor of breaking away.”".split(' ')
print(removeStopwords(document, words))