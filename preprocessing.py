import json
import spacy
from spacy.tokens import Doc
from spacy.tokens import DocBin
import spacy.lang.ro.stop_words
from sklearn.utils import shuffle


def create_train_data(data_train, split, remove_stopwords, shuffle_data):
    sentence_count = len(data_train)                            # data_train = list of training data
    if shuffle_data:                                            # split = percentage of data used for training
        data_train = shuffle(data_train, random_state=0)        # 1 - split = percentage of data used for validation
                                                                # 0 <= split <= 1
    db = DocBin()                                               # remove_stopwords = bool, if True, stopwords will be filtered from training data
    for dict in data_train[:int(split*sentence_count)]:         # shuffle_data = bool, if True, the order of training data will be random
        labels = dict['ner_tags']
        tokens = dict['tokens']
        spaces = dict['space_after']

        if remove_stopwords:
            tokens_filtered = []
            spaces_filtered = []
            labels_filtered = []
            for token, space, label in zip(tokens, spaces, labels):
                if token not in spacy.lang.ro.stop_words.STOP_WORDS:
                    tokens_filtered.append(token)
                    spaces_filtered.append(space)
                    labels_filtered.append(label)
            tokens = tokens_filtered
            spaces = spaces_filtered
            labels = labels_filtered
        doc = nlp(Doc(nlp.vocab, words=tokens, spaces=spaces))

        ents = []
        poz_init = 0
        for index in range(len(tokens)):
            poz_fin = poz_init + len(tokens[index])
            if labels[index] != "O":
                span = doc.char_span(poz_init, poz_fin, label=labels[index])
                ents.append(span)
            poz_init = poz_fin
            if spaces[index]:
                poz_init += 1
        doc.ents = ents
        db.add(doc)
    db.to_disk("./train.spacy")

    db = DocBin()
    for dict in data_train[int(split*sentence_count):]:
        labels = dict['ner_tags']
        tokens = dict['tokens']
        spaces = dict['space_after']

        if remove_stopwords:
            tokens_filtered = []
            spaces_filtered = []
            labels_filtered = []
            for token, space, label in zip(tokens, spaces, labels):
                if token not in spacy.lang.ro.stop_words.STOP_WORDS:
                    tokens_filtered.append(token)
                    spaces_filtered.append(space)
                    labels_filtered.append(label)
            tokens = tokens_filtered
            spaces = spaces_filtered
            labels = labels_filtered

        doc = nlp(Doc(nlp.vocab, words=tokens, spaces=spaces))
        ents = []
        poz_init = 0
        for index in range(len(tokens)):
            poz_fin = poz_init + len(tokens[index])
            if labels[index] != "O":
                span = doc.char_span(poz_init, poz_fin, label=labels[index])
                ents.append(span)
            poz_init = poz_fin
            if spaces[index]:
                poz_init += 1
        doc.ents = ents
        db.add(doc)
    db.to_disk("./dev.spacy")


nlp = spacy.blank("ro")
f_train = open('train.json')
data_train = json.load(f_train)
label_to_id = {"O": 0, "PERSON": 1, "QUANTITY": 12, "NUMERIC_VALUE": 13, "NAT_REL_POL": 5, "GPE": 3, "DATETIME": 9, "ORGANIZATION": 2, "PERIOD": 10, "EVENT": 6, "FACILITY": 15, "ORDINAL": 14, "LOC": 4, "MONEY": 11, "WORK_OF_ART": 8, "LANGUAGE": 7, "PRODUCT": 0}

create_train_data(data_train, 0.7, True, True)

