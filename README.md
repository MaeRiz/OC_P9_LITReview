# Application web de critique par LitReview

Ce site est une application web développer avec le [Framework Django](https://www.djangoproject.com/).

## Prérequis

1. Installer [Python 3](https://www.python.org/downloads/).

2. Télécharger le programme via GitHub avec la commande ci-dessous ou en téléchargeant [l'archive](https://github.com/MaeRiz/OC_P9_LITReview/archive/refs/heads/master.zip).
```bash
git clone https://github.com/MaeRiz/OC_P9_LITReview.git
```

3. Créer un environnement virtuel et l'activer :
```cmd
python3 -m venv env
env\Scripts\activate
```

4. installer les modules :
```cmd
pip install -r requirements.txt
```

5. Faire les migrations:
```cmd
litreview\manage.py makemigrations
litreview\manage.py migrate
```
## Utilisation
1. Lancer le serveur [Django](https://www.djangoproject.com/):
```cmd
litreview\manage.py runserver
```
2. Dans un navigateur se rendre à l'adresse [http://localhost:8000/](http://localhost:8000/)