
### 	Abordarea problemei:
Am plecat de la modelul oferit de spacy pentru lb romana<br>
Am incercat multe variatii pentru impartirea datelor de train/validation (50-50, 66-33, 75-25, 90-10, 95-5, 99-1)<br>
Am incercat sa transformam tot input ul in lowercase <br>
Am incercat sa parcurgem train data-ul in ordine random<br>
Am incercat sa excludem stopwords din datele de train<br>
Cel mai bun rezultat a fost obtinut cu raportul 90-10, fara alte modificari<br>

###   Prerequisites:
Programul foloseste modulul spacy3, care poate fi descarcat folosind package manager-ul din PyCharm. <br>
E necesara si instalarea "ro_core_news_lg", folosind: <br>
```
python -m spacy download ro_core_news_lg <br>
```
in terminalul din PyCharm.


###	Mod de utilizare:
Se va rula preprocessing.py pentru a obtinele fisierele .spacy folosite ca input pentru train.<br>
Functia get_training_data primeste parametrii data_train, split, stopwords si shuffle_data,<br>
pentru a obtine diverse variante de input de train. Semnificatia variabilelor e descrisa<br>
in codul sursa, in comentarii.<br>

Datele de config pentru train se afla in config.cfg (settings: romanian, ner, cpu, efficiency)<br>
Alte variatii de config se pot obtine de pe https://spacy.io/usage/training#quickstart<br>

Se va rula, in terminal, in folder-ul cu proiectul, fisierul de config si cele 2 fisiere .spacy (train.spacy, dev.spacy)<br>
```
python -m spacy train config.cfg --paths.train ./train.spacy --paths.dev ./dev.spacy --output ./model/output<br>
```
Doua modele vor fi create in folderul /model/output, ultima iteratie (model-last) si cea mai buna iteratie (model-best).<br>

###	Alte functii implementate:
create_submission.py va genera un fisier .csv cu formatul corespunzator pentru un submission<br>
Numele modelului folosit se afla in variabila model_name, iar numele fisierului de output in filename<br>

check_efficiency.py verifica acuratetea pe un set de date de train ale modelului ales<br>

