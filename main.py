import re
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

df = pd.read_csv('movie.csv')

#object of WordNetLemmatizer
lm = WordNetLemmatizer()

# download required nltk packages
nltk.download('stopwords')
nltk.download('wordnet')


# create a template function to calculate amount of words in each string record
def count_words(text):
    return len(text.split())

# template function to remove stopwords from text records
def remove_stopwords(text):
  pattern = r'\b(?:{})\b'.format('|'.join(stopwords_))
  return re.sub(pattern, '', text.lower(), flags=re.IGNORECASE)


# template function to transform text using nltk package
def text_transformation(item):

    new_item = item.replace('br', '')
    new_item = re.sub('[^a-zA-Z]',' ',str(item))
    new_item = new_item.lower()
    new_item = new_item.split()
    words = [lm.lemmatize(word) for word in new_item if word not in set(stopwords.words('english'))]
    
    return ' '.join(str(word) for word in words)

# apply template function to text feature of the dataframe
df['words_count'] = df['text'].apply(count_words)

# load a list of stop words to remove from the string
with open('archive/english.txt', 'r') as stopwordsfile:
  stopwords_ = stopwordsfile.readlines()  

# strip newline characteurs from stopwords in an array
stopwords_ = list(map(lambda x: x.strip(), stopwords_))

# create a version of each text with no stop words using nltk
df['text_no_stop_words_nltk'] = df['text'].apply(text_transformation)

# create a version of each text with no stop words included in manual approach
df['text_no_stop_words_manual'] = df['text'].apply(remove_stopwords)

df.to_csv('movie_desc_transformed.csv')