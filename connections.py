import gensim
import gensim.downloader as api
import pickle
import gzip
import itertools



try:
    f = open('model.dat','rb')
    print('Loading model')
    gnews = pickle.load(f)
except FileNotFoundError:
    print("Downloading model")
    gnews = api.load('word2vec-google-news-300')
    print("Saving model for later")
    pickle.dump(gnews,open('model.dat','wb'))

print('\n')

words = []
print('Enter 16 words, each on a new line')
for k in range(16):
    words.append(input("> "))

words = set(words)




print('\n')
print('Looking for connections within = ')
print(words)
print('\n')

def quadscore(quad):
    score = 1
    for pair in itertools.combinations(quad,2):
        score = score * gnews.similarity(pair[0],pair[1])
    return score


for k in range(4):
    bestscore = 0
    for quad in itertools.combinations(words,4):
        score=quadscore(quad)
        #print(quad,score)
        if(score>bestscore):
            bestscore=score
            bestquad =quad
    print(bestquad)
    words = words - set(bestquad)
    

    




