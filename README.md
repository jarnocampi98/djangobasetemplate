# djangobasetemplate

Per utilizzare creare venv (es. python3 -m venv venv)
Installare dipendenze requirements.txt (pip install -r requirements.txt)

Il nome del progetto attuale è "MyProject"
Per cambiare nome sostituire "MyProject" e rimoninare la cartella di progetto da "MyProject" nel nome che si desidera

Applicazioni pre-configurate:
- core --> Gestisce le route. registrare qui le rotte
- accounts --> gestisce registrazione
- app1 --> esempio applicazione

Per creare nuova applicazione (es. app2):
- python3 manage.py starapp [nome_app]
- registrare l'applicazione in MyProject/settings.py
- registrare i template dell'app2 in MyProject/settings.py (nella sezione di registrazione dei template, dove sono registrati quelli delle altre app)
- In app2 creare:
  - Templates/app2/ (creare i template .html qui)
  - urls.py (registrare le rotte per questa app qui)
