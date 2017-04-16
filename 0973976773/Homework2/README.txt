1(b)
Determining whether a dependency graph is projective:
First add an arc where the child index is less than the parent index. Then
check the indices of arcs within the index range of the child and parent. 
If any node has an arc that connects to an index less than the child or
greater than the parent, then the graph is not projective. 

1(c)
Projective Sentence:
I will keep searching for my key.

Non-Projective Sentence:
I will keep searching for my key which can open the door of my apartment that
locates on upper west side.

2(b)
Bad Features:

UAS: 0.279305354559 
LAS: 0.178726483357

3(a)
New Features:
0) Number of VERBs between the token on top of the stack and the first token
in the buffer.
Complexity: O(N)

1) LEMMA OF STK[0], STK[1], BUF[0]
Complexity: O(1)

2) POSTAG of STK[0], STK[1], BUF[0], BUF[1], BUF[2], BUF[3]
Complexity: O(1)

3) #of left and right child of STK[0], BUF[0]
Complexity: O(length of arc_list)

4) FORM of BUF[1]
Complexity: O(1)

5) Distance
Complexity: O(1)


3(c)
Swedish model:
		Number of training examples : 500
		Number of valid (projective) examples : 437

		Swedish Results
		UAS: 0.870477568741
		LAS:0.766280752533

English model:

		Number of training examples : 200
		Number of valid (projective) examples : 200
		UAS: 0.867481662592 
		LAS :0.820537897311
Danish model:
		Number of training examples : 200
		Number of valid (projective) examples : 165

		Danish Results
		UAS:0.875083948959 
		LAS0.760913364674
3(d)
complexity of arc-eager: O(n)
tradeoff: inability to parse non-projective sentence
