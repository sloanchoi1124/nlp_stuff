Xuelai Cui	xc2315
------------------------------------------
A1

UNIGRAM near 			-12.4560686964
BIGRAM near the 		-1.56187888761
TRIGRAM near the ecliptic 	-5.39231742278

A2
output/A2.uni.txt		1052.4865859
output/A2.bi.txt		53.8984761198
output/A2.tri.txt		5.7106793082

A3
output/A3.TXT			12.5516094886

A4
Yes.
Because lower perplexity indicates that we know more information from n-gram.
Since Tri-gram model performs better compared with bi-gram and uni-gram
model, the perplexity of interpolation must be higher since it's a weited
average of bi-gram, uni-gram and tri-gram model.

A5
output/Sample1_scored.txt	11.1670289158
output/Sample2_scored.txt	1627571078.54

Since the perplexity of Sample 1 is close to that of A3, and the perplexity of
Sample 2 is extremely high, meaning that Sample 2 is very likely to contain
data that doens't exist in the training data. Therefore, Sample1 belongs to
the Brown training data set.
B2
TRIGRAM CONJ ADV NOUN 		-4.46650366731
TRIGRAM DET NUM NOUN 		-0.713200128516
TRIGRAM NOUN PRT CONJ 		-6.38503274104

B4
midnight NOUN 			-13.1814628813
Place VERB 			-15.4538814891
primary ADJ 			-10.0668014957
STOP STOP 			0.0
_RARE_ VERB 			-3.17732085089
_RARE_ X 			-0.546359661497

B5
Percent correct tags: 93.3249946254

B6
Percent correct tags: 91.3944534563
---------------------------------------------
Part A: 13.79sec
Part B: 63.52sec
