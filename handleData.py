
import sys
sys.executable
!pip install wordcloud

import nltk
from nltk.probability import FreqDist
from nltk.corpus import webtext
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk import sent_tokenize, word_tokenize

nltk.download("punkt")


myWords= "Bro i really dont what to say. but this guy has a lot of things to cry about, okay bro. i really wanted to show you guys what i like, but bro dont like it"

#What this line does is, it basically divids the sentence into sepearete words
nltk.word_tokenize(myWords)
