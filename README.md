NetSpeed Analyzer
https://screenshot.png

📋 Description
NetSpeed Analyzer est une application GUI complète et intuitive pour tester votre vitesse internet. Développée avec PySide6 (Qt for Python), elle utilise la bibliothèque speedtest-cli pour effectuer des mesures précises de débit et latence.

✨ Fonctionnalités
🚀 Test de Vitesse
Test Download/Upload : Mesure précise en Mbps

Ping/Latence : Mesure du temps de réponse

Serveurs personnalisables : Choix parmi des centaines de serveurs mondiaux

Sélection automatique : Trouve le meilleur serveur disponible

📊 Visualisation
Graphiques temps-réel : Historique des tests

3 graphiques séparés : Download, Upload et Ping

Statistiques détaillées : Moyennes, maximums et minimums

📁 Gestion des Données
Historique local : Sauvegarde automatique des résultats

Export CSV : Exportation des données pour analyse

Interface intuitive : Design moderne et responsive

🔧 Configuration
Sélection du serveur : Liste complète des serveurs Speedtest

Timeout réglable : De 5 à 30 secondes

Informations système : Détails sur l'environnement d'exécution

🛠️ Installation
Prérequis
Python 3.7 ou supérieur

Pip (gestionnaire de packages Python)

Installation des dépendances
bash
# Cloner le dépôt
git clone https://github.com/votre-username/netspeed-analyzer.git
cd netspeed-analyzer

# Installer les dépendances
pip install -r requirements.txt
Dépendances principales
PySide6 >= 6.4.0 (Interface graphique)

speedtest-cli >= 2.1.3 (Tests de vitesse)

matplotlib >= 3.5.0 (Graphiques)

platform (Inclue dans Python)

🚀 Utilisation
Lancement de l'application
bash
python main.py
Interface utilisateur
Onglet "Test de Vitesse" :

Sélectionnez un serveur ou laissez "Auto"

Configurez le timeout si nécessaire

Cliquez sur "🚀 Lancer le Test"

Visualisez les résultats en temps réel

Onglet "Système" :

Informations sur le système et l'application

Détails sur les bibliothèques utilisées

Boutons disponibles
🚀 Lancer le Test : Démarre un nouveau test

⏹️ Arrêter : Interrompt le test en cours

🔄 Rafraîchir : Met à jour la liste des serveurs

📊 Historique : Affiche l'historique des tests

💾 Exporter : Exporte les résultats en CSV

🗑️ Effacer : Supprime l'historique

📁 Structure du projet
text
netspeed-analyzer/
│
├── main.py              # Application principale
├── requirements.txt     # Dépendances Python
├── README.md           # Ce fichier
├── LICENSE             # Licence MIT
├── history.json        # Fichier d'historique (généré)
├── icon.png            # Icône de l'application (optionnel)
└── screenshots/        # Captures d'écran
📈 Résultats et export
Format des données
Les résultats sont sauvegardés dans history.json (format JSON) et peuvent être exportés en CSV avec les colonnes suivantes :

Numéro de test

Date et heure

Download (Mbps)

Upload (Mbps)

Ping (ms)

Serveur

Pays

Distance (km)

Visualisation
L'application génère automatiquement des graphiques montrant l'évolution des performances au fil du temps.

🔧 Développement
Architecture
Design Pattern MVC : Séparation claire des responsabilités

Threads QThread : Tests en arrière-plan sans bloquer l'interface

Signaux/Slots : Communication entre composants

Extensions possibles
Ajout de tests de stabilité de connexion

Intégration avec des services cloud

Notifications système

Mode sombre/clair

🤝 Contribution
Les contributions sont les bienvenues ! Pour contribuer :

Fork le projet

Créez une branche (git checkout -b feature/AmazingFeature)

Committez vos changements (git commit -m 'Add some AmazingFeature')

Push vers la branche (git push origin feature/AmazingFeature)

Ouvrez une Pull Request

Standards de code
Respecter PEP 8 pour Python

Ajouter des docstrings aux fonctions

Tester les nouvelles fonctionnalités

Mettre à jour la documentation

🐛 Dépannage
Problèmes courants
"ModuleNotFoundError: No module named 'speedtest'"

bash
pip install speedtest-cli
L'interface ne se lance pas

bash
pip install PySide6 matplotlib
Pas de serveurs trouvés

Vérifiez votre connexion internet

Essayez d'augmenter le timeout

Rafraîchissez la liste des serveurs

Débogage
Pour activer les logs de débogage :

python
import logging
logging.basicConfig(level=logging.DEBUG)
