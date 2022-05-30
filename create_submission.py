import json
import spacy
from spacy.tokens import Doc

model_name = "model-90"
filename = "default.csv"


nlp = spacy.load(model_name)
label_to_id = {"O": 0, "PERSON": 1, "QUANTITY": 12, "NUMERIC_VALUE": 13, "NAT_REL_POL": 5, "GPE": 3, "DATETIME": 9, "ORGANIZATION": 2, "PERIOD": 10, "EVENT": 6, "FACILITY": 15, "ORDINAL": 14, "LOC": 4, "MONEY": 11, "WORK_OF_ART": 8, "LANGUAGE": 7, "PRODUCT": 0, "ORG": 2, "NUMERIC": 13}
word_counter = 0

f_test = open('test.json')
data_test = json.load(f_test)


output = open(filename, 'w')
output.write("Id,ner_label\n")
for dict in data_test:                   # output of format (word_id, word_entity) in csv format
    tokens = dict['tokens']
    spaces = dict['space_after']
    doc = nlp(Doc(nlp.vocab, words=tokens, spaces=spaces))
    for token in doc:
        if token.ent_type_:
            output.write(str(word_counter) + "," + str(label_to_id[token.ent_type_]) + "\n")
        else:
            output.write(str(word_counter) + ",0\n")
        word_counter += 1
