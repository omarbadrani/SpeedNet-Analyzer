# NetSpeed Analyzer ⚡

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![PySide6](https://img.shields.io/badge/PySide6-6.4%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

Une application GUI moderne et intuitive pour tester et analyser votre vitesse internet avec des graphiques détaillés et un historique complet.

## ✨ Fonctionnalités

### 🚀 Test de Vitesse Complet
- **📥 Download** : Mesure précise de la vitesse de téléchargement
- **📤 Upload** : Test de la vitesse d'envoi
- **⏱️ Ping/Latence** : Mesure du temps de réponse du serveur
- **🌍 Serveurs Mondiaux** : Accès à des centaines de serveurs dans le monde entier

### 📊 Visualisation Avancée
- **Graphiques en Temps Réel** : Historique visuel des performances
- **3 Graphiques Séparés** : Download, Upload et Ping indépendants
- **Statistiques Détaillées** : Moyennes, maximums, minimums et tendances
- **Évaluation Automatique** : Classification de la qualité de connexion

### 🔧 Interface Moderne
- **Design Qt6** : Interface fluide et professionnelle
- **Multi-onglets** : Test et informations système
- **Emojis et Icônes** : Interface visuelle et intuitive
- **Configuration Flexible** : Timeout réglable et sélection de serveur

### 📁 Gestion des Données
- **💾 Sauvegarde Automatique** : Historique conservé entre les sessions
- **📤 Export CSV** : Données exportables pour analyse externe
- **🗑️ Nettoyage** : Possibilité d'effacer l'historique
- **📊 Comparaison** : Suivi des performances sur le temps

## 🖼️ Aperçu

```
┌─────────────────────────────────────────────────────┐
│               ⚡ NetSpeed Analyzer                   │
├─────────────────────────────────────────────────────┤
│ 📡 Serveur: Auto (Meilleur serveur)                 │
│ ⏱️ Timeout: 10 secondes                             │
├─────────────────────────────────────────────────────┤
│ 🚀 Lancer le Test   🔄 Rafraîchir   📊 Historique    │
├─────────────────────────────────────────────────────┤
│ [███████████████████████░░░░░░] 85%                 │
│ Test d'upload en cours...                          │
├─────────────────────────────────────────────────────┤
│ ✅ Test Terminé - Excellent                         │
│ 📥 Download: 245.67 Mbps                            │
│ 📤 Upload: 125.34 Mbps                              │
│ ⏱️ Ping: 12 ms                                      │
└─────────────────────────────────────────────────────┘
```

## 🛠️ Installation

### Prérequis
- Python 3.7 ou supérieur
- Connexion internet fonctionnelle

### Installation Rapide

```bash
# 1. Cloner le dépôt
git clone https://github.com/votre-username/netspeed-analyzer.git
cd netspeed-analyzer

# 2. Créer un environnement virtuel (recommandé)
python -m venv venv

# 3. Activer l'environnement
# Sur Windows :
venv\Scripts\activate
# Sur Linux/Mac :
source venv/bin/activate

# 4. Installer les dépendances
pip install -r requirements.txt
```

### Dépendances
- **PySide6** >= 6.4.0 - Interface graphique Qt6
- **speedtest-cli** >= 2.1.3 - Tests de vitesse internet
- **matplotlib** >= 3.5.0 - Création de graphiques

## 🚀 Utilisation

### Lancement de l'application

```bash
python main.py
```

### Guide d'utilisation étape par étape

1. **Configuration du test**
   - Sélectionnez un serveur spécifique ou laissez "Auto"
   - Ajustez le timeout si nécessaire (10 secondes recommandé)
   - Cliquez sur "🔄 Rafraîchir" pour mettre à jour la liste des serveurs

2. **Lancement du test**
   - Cliquez sur "🚀 Lancer le Test"
   - Suivez la progression dans la barre et les messages
   - Vous pouvez arrêter à tout moment avec "⏹️ Arrêter"

3. **Analyse des résultats**
   - Consultez les vitesses Download/Upload et le ping
   - Observez les graphiques d'évolution
   - Vérifiez les statistiques moyennes

4. **Gestion des données**
   - "📊 Historique" : Affiche les 10 derniers tests
   - "💾 Exporter" : Sauvegarde en fichier CSV
   - "🗑️ Effacer" : Supprime l'historique des tests

## 📁 Structure des Fichiers

```
netspeed-analyzer/
│
├── main.py                    # Application principale
├── requirements.txt           # Dépendances Python
├── README.md                  # Ce fichier
├── LICENSE                    # Licence MIT
│
├── history.json               # Historique des tests (auto-généré)
├── speedtest_results_*.csv    # Exports CSV (auto-généré)
│
└── assets/                    # Ressources (optionnel)
    ├── icon.png              # Icône de l'application
    └── screenshots/          # Captures d'écran
```

## 📊 Format des Données

### Sauvegarde Automatique (JSON)
```json
{
  "count": 1,
  "timestamp": "2024-01-15 14:30:45",
  "download": 245.67,
  "upload": 125.34,
  "ping": 12.5,
  "server": "Provider (Paris, France)",
  "server_info": {
    "sponsor": "Provider",
    "name": "Paris",
    "country": "France",
    "d": 25.3,
    "latency": 12.5
  }
}
```

### Export CSV
```
Numéro;Date;Download (Mbps);Upload (Mbps);Ping (ms);Serveur;Pays;Distance (km)
1;2024-01-15 14:30:45;245.67;125.34;12.5;Provider (Paris);France;25.3
```

## 🔧 Développement

### Architecture Technique
- **Interface** : PySide6 (Qt6) avec QThread pour les opérations asynchrones
- **Tests Réseau** : Speedtest-cli avec gestion d'erreurs robuste
- **Visualisation** : Matplotlib avec mise à jour en temps réel
- **Persistance** : JSON pour l'historique local

### Extensions Possibles
```python
# Idées pour améliorer l'application :

# 1. Tests de stabilité
- Test de ping continu sur 1 minute
- Mesure de la gigue (jitter)
- Tests à intervalles réguliers

# 2. Fonctionnalités réseau
- Test de plusieurs serveurs simultanément
- Mesure de la perte de paquets
- Analyse de la route (traceroute)

# 3. Intégrations
- Export vers Google Sheets/Excel
- Notifications système
- Partage des résultats
```

## 🐛 Dépannage

### Problèmes Courants et Solutions

| Problème | Solution |
|----------|----------|
| **"Module speedtest non trouvé"** | `pip install speedtest-cli` |
| **Interface ne se lance pas** | Vérifiez PySide6 : `pip install PySide6` |
| **Pas de serveurs disponibles** | Vérifiez la connexion internet et firewall |
| **Graphiques non affichés** | `pip install matplotlib` |
| **Test trop lent** | Augmentez le timeout ou changez de serveur |

### Mode Débogage
```bash
# Pour voir les messages détaillés
python -c "import speedtest; print('Speedtest version:', speedtest.__version__)"
```

## 📈 Évaluation de la Qualité

L'application classe automatiquement votre connexion :

| Catégorie | Download | Upload | Ping |
|-----------|----------|--------|------|
| **Excellent** | > 100 Mbps | > 50 Mbps | < 20 ms |
| **Bon** | 50-100 Mbps | 20-50 Mbps | 20-50 ms |
| **Moyen** | 10-50 Mbps | 5-20 Mbps | 50-100 ms |
| **Faible** | < 10 Mbps | < 5 Mbps | > 100 ms |

## 🤝 Contribution

Les contributions sont les bienvenues ! Voici comment contribuer :

1. **Fork** le projet
2. **Créez une branche** (`git checkout -b feature/ma-fonctionnalite`)
3. **Commitez** vos changements (`git commit -am 'Ajout de ma fonctionnalité'`)
4. **Push** vers la branche (`git push origin feature/ma-fonctionnalite`)
5. **Ouvrez une Pull Request**

### Bonnes Pratiques
- Suivez les conventions PEP 8
- Ajoutez des tests pour les nouvelles fonctionnalités
- Documentez votre code
- Mettez à jour le README si nécessaire

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

```
MIT License

Copyright (c) 2024 Omar Badrani

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

## 👤 Auteur

**Omar Badrani**
- Développeur passionné par les applications réseaux et interfaces graphiques
- Contact : omarbadrani770@gmail.com
- GitHub : https://github.com/omarbadrani

## 🙏 Remerciements

- [speedtest-cli](https://github.com/sivel/speedtest-cli) pour l'excellente bibliothèque de tests
- [Qt/PySide6](https://www.qt.io/) pour le framework d'interface exceptionnel
- [Matplotlib](https://matplotlib.org/) pour les superbes capacités de visualisation
- Tous les contributeurs et testeurs

## 📞 Support

Si vous rencontrez des problèmes ou avez des questions :

1. **Vérifiez les [Issues](https://github.com/votre-username/netspeed-analyzer/issues)** existantes
2. **Créez une nouvelle Issue** avec :
   - Description claire du problème
   - Étapes pour reproduire
   - Captures d'écran si possible
   - Configuration système

3. **Contact direct** : omarbadrani770@gmail.com

---

⭐ **Si vous aimez ce projet, n'oubliez pas de mettre une étoile sur GitHub !** ⭐

---

## 📱 Téléchargements

### Version Exécutable
Des versions compilées pour Windows, macOS et Linux seront bientôt disponibles.

### Installation via Pip (à venir)
```bash
pip install netspeed-analyzer
netspeed-analyzer
```

---

**Dernière mise à jour** : Janvier 2024  
**Version** : 1.2.0  
**Support Python** : 3.7+  
**Plateformes** : Windows, Linux, macOS

---

*NetSpeed Analyzer - Parce que votre connexion mérite d'être analysée avec précision* 🚀
