import pandas as pd
from io import StringIO

def test(input):
    init_tags = pd.read_table(StringIO(input), header=None, sep='\t')

    lastLWord = ''
    curTag = ''
    curSentence = ''
    isLStart = True
    res = []
    for row in init_tags.iterrows():
        word = row[1][0]
        tag = row[1][1][0]

        if tag == 'O':
            if len(curTag) < 1 or (len(curTag) == 1 and curTag[0] == 'L'):
                continue
            if curTag[0] != 'L':
                curTag = 'L' + curTag
                curSentence = lastLWord + curSentence
            res.append((curSentence, curTag))
            curSentence = ''
            curTag = ''
            isLStart = True
            continue

        if tag == 'L':
            if isLStart:
                lastLWord = word
                isLStart = False
            else:
                lastLWord += word
        else:
            isLStart = True
        
        if len(curTag) == 0 or (len(curTag) > 0 and curTag[-1] != tag):
            if len(curTag) > 0 and curTag[0] != 'L' and tag == 'L':
                curTag += ''
            elif tag != 'S':
                curTag += tag
        
        if len(curTag) > 0 and curTag[0] != 'L' and tag == 'L':
            curSentence += ''
        elif tag != 'S':
            curSentence += word

    df = pd.DataFrame(res, columns=['初始句子', '生成句子'])
    return df.to_string()