
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
