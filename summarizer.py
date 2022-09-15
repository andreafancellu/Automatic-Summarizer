'''
    PROCESS:
    0) Remove stopwords and split text in sentences.    
    1) For every sentence, if it contanis a lemma that occurs in the title, save it.
    2) For every sentence, find the most relevant words by using cue sentences taken by the file cue_sentences.txt.
    3) Itersection between the sentences found in the two steps above.
'''


import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

CUE_PATH = 'data/cue_sentences.txt'

def split_dot(text):
    return text.split('.')

def remove_stopwords(text):
    return [word for word in text if word not in nltk.corpus.stopwords.words('english')]

def tokenize(text):
    return word_tokenize(text)

def lemmatize(word):    
    return WordNetLemmatizer().lemmatize(word)

def pos(tokens): #! not used
    return nltk.pos_tag(tokens)

# finds relevant sentences which have words that occurs in the title
def find_title_sentences(text, title): 
    sentences = []
    flag = False
    text = ' '.join(remove_stopwords(tokenize(text)))
    context_title = [lemmatize(word) for word in tokenize(title)]
    for sentence in split_dot(text):
        for word in tokenize(sentence):
            if word in context_title and not flag: # still haven't found a word in the title for this sentence
                sentences.append(sentence)
                flag = True
        flag = False
    return sentences

# get cue phrases from file in path
def get_cue_sentences(path):
    cues = []
    with open(path, 'r') as f:
        for line in f:
            cues.append(line)
    return cues

# finds relevant sentences
def find_relevant_sentences(text):
    sentences = []
    text = ' '.join(remove_stopwords(tokenize(text)))
    cues = get_cue_sentences(CUE_PATH)
    for sentence in split_dot(text):
        for c in cues:
            if c in sentence:
                sentences.append(sentence)
    return sentences

def overlap(list_1, list_2):
    return [value for value in list_1 if value in list_2]
