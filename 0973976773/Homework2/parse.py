import sys
import nltk
from providedcode import dataset
from providedcode.transitionparser import TransitionParser

from providedcode.dependencygraph import DependencyGraph

tp = TransitionParser.load(sys.argv[1])
testdata = []
for line in sys.stdin:
    sentence = DependencyGraph.from_sentence(line)
    testdata.append(sentence)
model = sys.argv[1]

tp = TransitionParser.load(model)
parsed = tp.parse(testdata)

for p in parsed:
    print(p.to_conll(10).encode('utf-8'))
