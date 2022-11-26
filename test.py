import gensim
model = gensim.models.Word2Vec.load('ja.bin')
for item, value in model.wv.most_similar('島村'):
    print(item,value)

