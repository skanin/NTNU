import random; random.seed(123)
import codecs
import string
from nltk.stem.porter import PorterStemmer
from nltk import FreqDist
import gensim
import os

f = codecs.open('/Users/sanderlindberg/Dropbox/NTNU/Informatikk/H2019/TDT4117/Øvinger/Øving_3/pg3300.txt', 'r', 'utf-8')

patrtition = f.readlines()

f_copy = patrtition.copy()

exclude = set(string.punctuation + "\n\r\t")

stemmer = PorterStemmer()

patrtition = list(
    map(
        lambda x: ''.join(ch for ch in x if ch not in exclude).lower().split(" "), list(
            filter(
                    lambda x: "gutenberg" not in x.lower(), patrtition)
                )
        )
    )

for i in range(0, len(patrtition)):
    for j in range(0, len(patrtition[i])):
        patrtition[i][j] = stemmer.stem(patrtition[i][j])

print(patrtition)

'''
dictionary = gensim.corpora.Dictionary(patrtition)

stopwords = codecs.open('/Users/sanderlindberg/Dropbox/NTNU/Informatikk/H2019/TDT4117/Øvinger/Øving_3/stopwords.txt', 'r').read().split(",")

stopword_ids = [dictionary.token2id[stopword] for stopword in stopwords if stopword in dictionary.token2id.keys()]

dictionary.filter_tokens(stopword_ids)

dictionary.save('/Users/sanderlindberg/Dropbox/NTNU/Informatikk/H2019/TDT4117/Øvinger/Øving_3/dictionary.dict')

corpus = [dictionary.doc2bow(text) for text in patrtition]

gensim.corpora.MmCorpus.serialize('/Users/sanderlindberg/Dropbox/NTNU/Informatikk/H2019/TDT4117/Øvinger/Øving_3/corpus.mm', corpus)

# corpus = gensim.corpora.MmCorpus('/Users/sanderlindberg/Dropbox/NTNU/Informatikk/H2019/TDT4117/Øvinger/Øving_3/corpus.mm')


tfidf = gensim.models.TfidfModel([corp for corp in corpus])

corpus_tfidf = tfidf[corpus]

index = gensim.similarities.MatrixSimilarity(corpus_tfidf)

lsi = gensim.models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=100)

corpus_lsi = lsi[corpus]

index_lsi = gensim.similarities.MatrixSimilarity(corpus_lsi)

def preprocessing(q):
    q = list(
    map(
        lambda x: ''.join(ch for ch in x if ch not in exclude).lower().split(" "), q.split(" ")
        )
    )
    q1 = []
    for word in q:
        if word[0] not in stopwords:
            q1.append(word)

    for i in range(0, len(q1)):
        for j in range(0, len(q1[i])):
            q1[i][j] = stemmer.stem(q1[i][j])
    
    return q1

query = preprocessing("How taxes influence Economics?")

query = [dictionary.doc2bow(w) for w in query]

tfidf_query = gensim.models.TfidfModel(query)

print(tfidf_query[query])
'''