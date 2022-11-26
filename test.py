import gensim
model = gensim.models.Word2Vec.load('ja.bin')
for item, value in model.wv.most_similar('島'):
    print(item,value)


sim=model.wv.similarity('幸せ', '幸福')
print(sim)