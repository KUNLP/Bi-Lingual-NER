import random

if __name__ == '__main__':
    with open('./data/en_train.conll' , mode='r' ) as f :
        en_train = []
        for line in f :
            en_train.append(line)
    print('en_train :', len(en_train), '\n')

    with open('./data/ko_train.conll' , mode='r' ) as f :
        ko_train = []
        for line in f :
            ko_train.append(line)
    print('ko_train :', len(ko_train), '\n')

    en_ko_train = en_train + ko_train
    print('en_ko_train :', len(en_ko_train), '\n')

    start_idx = 0
    group = []
    for idx, word in enumerate(en_ko_train):
        if en_ko_train[idx] == '\n':
            lump = en_ko_train[start_idx:idx+1]
            lump.insert(-1, '\n')
            start_idx = idx+1
            group.append(lump)
    random.shuffle(group)
    # print(group[:10])

    flat_text = [element for array in group for element in array]
    with open('./data/en_ko_train.conll', 'w', encoding='UTF-8') as f:
        for line in flat_text:
            f.write(line)