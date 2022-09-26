'''
    PROCESS:
    0) Remove stopwords and split text in sentences.    
    1) For every sentence, if it contanis a lemma that occurs in the title, save it.
    2) For every sentence, find the most relevant words by using cue sentences taken by the file cue_sentences.txt.
    3) Itersection between the sentences found in the two steps above.
'''


import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer

CUE_PATH = 'data/cue_sentences.txt'
NASARI_PATH_1 = 'data/mini_NASARI.tsv'
NASARI_PATH_2 = 'data/dd-small-nasari-15.txt'


def split_dot(text):
    return text.split('.')

def remove_stopwords(tokens):
    return [lemmatize(word) for word in tokens if word not in nltk.corpus.stopwords.words('english')]

def tokenize_simple(text):
    return word_tokenize(text)

def tokenize_all(text):  # remove the punctuation too
    tokenizer = RegexpTokenizer(r'\w+')
    return tokenizer.tokenize(text)

def lemmatize(word):    
    return WordNetLemmatizer().lemmatize(word)

def pos(tokens): #! not used
    return nltk.pos_tag(tokens)

# finds relevant sentences which have words that occurs in the title
def find_title_sentences(text, title): 
    sentences = []
    flag = False
    text = ' '.join(remove_stopwords(tokenize_simple(text)))
    context_title = [lemmatize(word.lower()) for word in tokenize_simple(title)]
    for sentence in split_dot(text.lower()):
        for word in tokenize_simple(sentence):
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
            cues.append(line.lower())
    return cues

# finds relevant sentences
def find_relevant_sentences(text):
    sentences = []
    text = ' '.join(remove_stopwords(tokenize_simple(text)))
    cues = get_cue_sentences(CUE_PATH)
    for sentence in split_dot(text):
        for c in cues:
            if c in sentence.lower():
                sentences.append(sentence)
    return sentences

# get the nasari vectors associated with the tokens in title
def get_nasari_from_title(text):
    tokens = remove_stopwords(tokenize_all(text))
    nasari = {}
    with open(NASARI_PATH_2, 'r', encoding="utf8") as f:
        for line in f:
            for token in tokens:
                if token.lower() == line.split(';')[1].lower():
                    nasari[token] = line.split(';')[2:]
    return nasari                    

# finds sentences that occurs in NASARI vectrors retrieved from title
def find_nasari_elems(text, nasari):     
    sentences = []
    flasg = False
    text = ' '.join(remove_stopwords(tokenize_simple(text)))
    for sentence in split_dot(text):
        for token in tokenize_all(sentence):
            for key in nasari.keys():
                for elem in nasari[key]:
                    if token.lower() == elem.split('_')[0].lower() and not flag:
                        sentences.append(sentence)
                        flag = True
        flag = False
    return sentences

def overlap(list_1, list_2):
    return [value for value in list_1 if value in list_2]