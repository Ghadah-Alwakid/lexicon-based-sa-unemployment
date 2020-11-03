import os

from lexi_utilties import load_lex

# mydir = 'lexicons_v4'
# mydir = 'new lexicon Feb2019 v2 - Copy'
mydir = 'lexicons_v6'

files = os.listdir(mydir)
print(files)
overlap_count = 0
for fi in files:
    # if not fi.startswith('light_'):
    #     continue
    if not fi.endswith('.txt'):
        continue
    file_name = os.path.join(mydir, fi)
    lines_i = load_lex(file_name)
    for fj in files:
        if fi is fj or not fj.endswith('.txt'):
            continue
        file_name = os.path.join(mydir, fj)
        lines_j = load_lex(file_name)
        for token in lines_i:
            if token in lines_j and fi[-7:-3] != fj[-7:-3]:
                print(token, fi, fj)
                print(fi[-7:-3], fj[-7:-3], fi[-7:-3] != fj[-7:-3])
                overlap_count += 1
print('overlaps:', overlap_count)
print('all done')
