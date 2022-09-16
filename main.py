from pprint import pprint
from summarizer import *

text = ""
with open('data/text.txt', 'r') as f:
    for word in f:
        text = text + " " + word

sentences_1 = find_title_sentences(text, "rock and roll")
sentences_2 = find_relevant_sentences(text)

'''print("Sentences from title:")
pprint(sentences_1)
print('\n\n\n')

print("Sentences from cue phrases:")
pprint(sentences_2)
print('\n\n\n')'''

nasari = get_nasari_from_title('hall of fame')
print(nasari, '\n')
nasari_elems = find_nasari_elems(text, nasari)
print(nasari_elems)