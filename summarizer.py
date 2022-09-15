import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def split_dot(text):
    return text.split('.')

def remove_stopwords(text):
    return [word for word in text if word not in nltk.corpus.stopwords.words('english')]

def tokenize(text):
    return word_tokenize(text)

def lemmatize(word):    
    return WordNetLemmatizer().lemmatize(word)

def pos(tokens):
    return nltk.pos_tag(tokens)

# finds relevant phrases which have words that occurs in the title
def find_title_phrases(text, title): 
    sentences = []
    flag = False
    for sentence in split_dot(text):
        for word in tokenize(sentence):
            if word in title and not flag: # still haven't found a word in the title for this sentence
                sentences.append(sentence)
                flag = True
        flag = False
    return sentences


'''
    0) Remove stopwords and split text in sentences.    
    1) For every sentence, if it contanis a lemma that occurs in the title, save it.
    2) For every sentence, find the most relevant words, by using pos tagging and cue phrases taken by the file cue_phrases.txt.
    3) Itersection between the sentence found in the firist two steps
'''
