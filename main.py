from pprint import pprint
from summarizer import *
text_2_title = 'The world\'s second biggest cryptocurrency just got a lot greener'

text = ""
with open('data/text_2.txt', 'r') as f:
    for word in f:
        text = text + " " + word

sentences_1 = find_title_sentences(text, text_2_title)
sentences_2 = find_relevant_sentences(text)

print("Sentences from title:")
pprint(sentences_1)
print('\n\n\n')

print("Sentences from cue phrases:")
pprint(sentences_2)
print('\n\n\n')
'''
nasari = get_nasari_from_title(text_2_title)
print(nasari, '\n')
nasari_elems = find_nasari_elems(text, nasari)
print(nasari_elems)'''