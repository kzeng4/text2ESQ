import pandas as pd

test = pd.read_csv('~/easy_test.csv')
train = pd.read_csv('~/easy_train.csv')
valid = pd.read_csv('~/easy_valid.csv')

def pre(data):
    tokens = [eval(token) for token in data['tokens']]
    tags, texts = [],[]
    for pairs in tokens:
        tag = []
        text = []
        for pair in pairs:
            tag.append(pair['label'])
            text.append(pair['text'])
        tags.append(tag)  
        texts.append(text) 
    tags_string = [' '.join(x) for x in tags] 
    sentence = [' '.join(x) for x in texts]
    #sentence = [single_sentence.strip() for single_sentence in data['tp']]
    dict_= {"sentence":sentence,"tags":tags_string}
    df = pd.DataFrame(dict_)
    return df

df_test = pre(test)
df_train = pre(train)
df_dev = pre(valid)
