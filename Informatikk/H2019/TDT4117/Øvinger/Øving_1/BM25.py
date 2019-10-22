from math import log2

def bm25(k1, b, queries, documents):
    ldocs = sum(map(lambda x: len(x), documents))
    n = len(documents)
    lave = ldocs/n
    results = list()
    documentnum = 0
    for document in documents:
        documentnum += 1
        querynum = 0
        ld = len(document)
        for query in queries:
            querynum += 1
            result = 0
            for term in query:
                tf = document.count(term)
                dft = len(list(filter(lambda x: term in x, documents)))
                result += log2(n/dft)*(((k1+1)*tf)/(k1*((1-b) + b * (ld/lave)) + tf))
            results.append(f"Document {documentnum} Query {querynum}: {result}")
    return results



docs = [
    ["Big", "Cat", "Small", "Dog"],
    ["Dog"],
    ["Cat", "Dog"],
    ["Big", "Cat", "Big", "Small", "Cat", "Dog"],
    ["Big", "Small"],
    ["Small", "Cat", "Dog", "Big"],
    ["Big", "Big", "Big"],
    ["Dog", "Cat", "Cat"],
    ["Cat", "Small"],
    ["Small", "Small", "Big", "Dog"]
]

docs2 = [
    ["Trump", "Hillary", "Trump", "Trump"],
    ["President", "Hillary", "Hillary",],
    ["Trump", "Hillary", "Hillary"],
    ["President", "Trump"],
    ["Hillary"],
    ["President", "President"],
    ["Hillary", "Hillary", "President", "Trump", "President", "Hillary", "Trump"],
    ["President"],
    ["President", "Hillary", "Trump"],
    ["President", "Trump", "Trump", "President"]
]

lst = bm25(1.2, 0.75, [["Cat", "Dog"], ["Small"]], docs)

counter = 1
for i in range(0, len(lst), 2):
    print(f"Document {counter}:\n{lst[i]}\n{lst[i+1]}\n")
    counter += 1