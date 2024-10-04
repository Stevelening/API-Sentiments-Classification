# API-Sentiments-Classification
Il s'agit d'une api de classification de sentiments basée sur le modèle de `Bayes Naif Multinominal`.

# Comment tester/utiliser l'api

 Pour tester/utiliser notre api, il suffit de suivre les etapes suivantes :

 1 - Telecharger les fichiers "app.html" , "api.py" , "machineLearningClassification.pkl" et "mycv.pkl"
 
 2 - Lancer le serveur python :
	- ouvrir le terminal "Anaconda Prompt"
	- installer flask-core en executant le script : pip install -U flask-cors
	- lancer maintenant le serveur python en executant le script : python api.py
	- si tout se passe bien, on voit apparaitre dans le terminal le message : "Running on http://127.0.0.1:12345/ (Press CTRL+C to quit)"

 3 - Lancer l'application web en double cliquant sur le fichier "app.html"
 
 4 - Pour predire le sentiment d'un nouveau commentaire, entrer la chaine de caracteres(le commentaire a predire) dans la zone de texte
	 et cliquer sur le bouton "Soumettre"
	 
 5 - le resultat de la prediction s'affiche alors a l'ecran.
