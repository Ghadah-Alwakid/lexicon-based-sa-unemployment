def count_spaces(infile):
    text = open(infile, encoding='utf-8').read()
    return text.count(' ')


print(count_spaces('lexicons_v5/neg.txt'))
print(count_spaces('lexicons_v5/pos.txt'))
print(count_spaces('lexicons_v5/very_neg.txt'))
print(count_spaces('lexicons_v5/very_pos.txt'))
