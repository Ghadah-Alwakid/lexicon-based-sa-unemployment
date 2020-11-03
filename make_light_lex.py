import aspell

from lexi_utilties import light_stem_word


def make_light_lexicon(infile, outfile):
    ar_spell = aspell.Speller(('dict-dir', './ar_dict/'), ('lang', 'ar'),
                              ('encoding', 'utf-8'))
    lexicon = open(infile, encoding='utf-8').read().split()
    print(infile, 'size', len(lexicon))
    light_lexicon = set()
    for word in lexicon:
        light_word = light_stem_word(word)
        if light_word != word and light_word not in lexicon \
                and light_word in ar_spell:
            light_lexicon.add(light_word)
    light_lexicon = list(sorted(light_lexicon))
    print('light size', len(light_lexicon))
    with open(outfile, mode='w', encoding='utf-8') as file_writer:
        file_writer.write('\n'.join(light_lexicon))


make_light_lexicon('lexicons_v5/neg.txt', 'lexicons_v5/light_neg.txt')
make_light_lexicon('lexicons_v5/pos.txt', 'lexicons_v5/light_pos.txt')
make_light_lexicon('lexicons_v5/very_neg.txt', 'lexicons_v5/light_very_neg.txt')
make_light_lexicon('lexicons_v5/very_pos.txt', 'lexicons_v5/light_very_pos.txt')
print('all done')
