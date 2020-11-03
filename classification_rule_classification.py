def classify(positive_score, negative_score):
    if positive_score + negative_score > 0:
        label = 'positive'
    elif positive_score + negative_score < 0:
        label = 'negative'
    elif positive_score == 0 and negative_score == 0:
        label = 'neutral'
    else:
        label = 'mix'
    print('pos {}\tneg {}\tlabel {}'.format(pos_socre, neg_score, label))


pos_socre = 0.0;
neg_score = 0.0
classify(pos_socre, neg_score)
pos_socre = 0.5;
neg_score = -0.5
classify(pos_socre, neg_score)
pos_socre = 0.8;
neg_score = -0.5
classify(pos_socre, neg_score)
pos_socre = 0.5;
neg_score = -0.8
classify(pos_socre, neg_score)

# output
# pos 0.0	neg 0.0	label neutral
# pos 0.5	neg -0.5	label mix
# pos 0.8	neg -0.5	label positive
# pos 0.5	neg -0.8	label negative
