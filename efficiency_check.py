import json
import spacy
from spacy.tokens import Doc


def check_accuracy(model_name, training_data):      # model_name = file name of used model
    total_eff = 0                                   # training_data = list of data used to check accuracy
    sentence_count = len(data)                              # Note: slow on large input
    nlp = spacy.load(model_name)
    for dict in data:
        labels = []
        labels_correct = ['ner_tags']
        tokens = dict['tokens']
        spaces = dict['space_after']
        doc = Doc(nlp.vocab, words=tokens, spaces=spaces)
        doc = nlp(doc)
        for token in doc:
            if token.ent_type_:
                labels.append(token.ent_type_)
            else:
                labels.append('O')
        labels = [x.replace("NUMERIC_VALUE", "NUMERIC").replace("ORGANIZATION", "ORG").replace("PRODUCT", "O").rjust(11)
                  for
                  x in labels]
        correct_count = 0
        total_count = 0
        for i in range(len(labels_correct)):
            if labels[i] == labels_correct[i]:
                if not labels[i] == "O":
                    correct_count += 1
                    total_count += 1
            else:
                total_count += 1
        if total_count:
            total_eff += correct_count / total_count

    total_eff /= sentence_count
    return total_eff


f = open('train.json')
data = json.load(f)
f.close()

print(check_accuracy("model-90", training_data=data))

