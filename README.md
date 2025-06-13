# intrusion_detector
Appli construite avec **Flask** qui permet de détecter les intrusions réseau à partir de fichiers CSV en utilisant un modèle de machine learning pré-entraîné.

## 🚀 Fonctionnalités

- ✅ Téléversement de fichiers `.csv`
- ✅ Détection automatique des intrusions (0 = normale, 1 = intrusion)
- ✅ Affichage du nombre et du pourcentage d’intrusions détectées

- ## 🧠 Modèle utilisé

Le modèle est un **Random Forest Classifier** entraîné à partir d'un jeu de données de détection d'intrusion. Les données ont été prétraitées avec un `StandardScaler` pour normaliser les features.

📤 Utilisation
Prépare un fichier CSV contenant uniquement les features nécessaires (sans la colonne label).

Clique sur "Choisir un fichier" et sélectionne ton fichier .csv.

Clique sur Predict pour lancer l’analyse.

Le résultat s’affiche juste en dessous.

🖼️ Aperçu de l'interface
<img width="562" alt="image" src="https://github.com/user-attachments/assets/7fd32dfd-7a62-4ec0-a550-03214712dde4" />

