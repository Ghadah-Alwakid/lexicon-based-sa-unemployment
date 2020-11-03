import os

from lexi_utilties import load_lex

mydir = 'lexicons_v6'

files = os.listdir(mydir)
print(files)
waw_word_count = 0
for fi in files:
    # if not fi.startswith('light_'):
    #     continue
    if not fi.endswith('.txt'):
        continue
    file_name = os.path.join(mydir, fi)
    lines_i = load_lex(file_name)
    for word in lines_i:
        if word.startswith('و') and word[1:] not in lines_i:
            print(word, file_name)
            waw_word_count += 1
print('waw_word_count', waw_word_count)
