import sklearn
from sklearn.manifold import TSNE
#import matplotlib.pyplot as plt
from dependencyRNN import DependencyRNN

answer_embeddings = DependencyRNN.load("random_init.npz")
ans_dict = answer_embeddings.answers
#print ans_dict
#print ans_dict[u'mao_zedong']
matrix = []
labels = []
for key in ans_dict:
    matrix.append(ans_dict[key])
    labels.append(key)

tsne = sklearn.manifold.TSNE(n_components = 2, perplexity = 30.0)
matrix_reduced = tsne.fit_transform(matrix)

x = []
y = []
for point in matrix_reduced:
    x.append(point[0])
    y.append(point[1])


print labels

#fig, ax = plt.subplots()
#ax.scatter(x, y)

#for i, txt in enumerate(n):
    #ax.annotate(txt, (x[i], y[i]))
#plt.show()
