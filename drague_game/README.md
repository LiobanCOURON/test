# 🌹 Premiers Contacts - Jeu de Drague Narrative

Un visual novel interactif en français basé sur le scénario "Chapitre 1 - Premiers Contacts".

## 📖 Description

**Premiers Contacts** est un jeu de drague narrative à embranchements où vous incarnez un nouveau venu dans un quartier charmant. Vous rencontrerez trois héroïnes aux personnalités distinctes :

- **Léna Vernet** (24 ans) - Brillante, sarcastique, travaille dans un café-librairie
- **Maya Rivière** (26 ans) - Extravertie, musicienne, connaît tout le monde  
- **Inès Delcourt** (25 ans) - Réservée, photographe, observatrice

⚠️ **Contenu 18+** - Romance, flirt et situations suggestives non graphiques. Tous les personnages sont majeurs.

## 🎮 Fonctionnalités

- ✅ Moteur de visual novel complet en HTML/CSS/JavaScript
- ✅ Système de dialogues avec effet machine à écrire
- ✅ Arbre de décisions à embranchements multiples
- ✅ Suivi des statistiques de relations (Affection, Respect/Confiance/Sécurité, Tension)
- ✅ Système de variables globales (Réputation, Chaos, Honnêteté)
- ✅ Sauvegarde/chargement de partie
- ✅ Journal d'historique des actions
- ✅ 68 images placeholder générées (backgrounds + sprites)
- ✅ Interface responsive et moderne

## 📁 Structure du projet

```
drague_game/
├── index.html              # Interface principale du jeu
├── data/
│   └── scenario.json       # Scénario complet avec dialogues et choix
├── assets/
│   └── images/             # 68 images (backgrounds + sprites)
├── src/                    # Code source (à développer)
└── generate_images.py      # Script de génération d'images
```

## 🚀 Comment jouer

### Option 1: Serveur local (recommandé)

```bash
cd /workspace/drague_game
python3 -m http.server 8000
```

Puis ouvrez votre navigateur à l'adresse : `http://localhost:8000`

### Option 2: Ouvrir directement

Ouvrez simplement le fichier `index.html` dans votre navigateur web moderne.

## 🎯 Système de jeu

### Variables principales
- **Jour** (DAY) : Jour actuel du chapitre
- **Moment** (TIME) : MATIN / APRÈS-MIDI / SOIR / NUIT
- **Réputation** : -3 à +5, opinion générale du quartier
- **Chaos** : Nombre de situations ayant dégénéré
- **Honnêteté** : Choix sincères cumulés

### Statistiques par héroïne
Chaque héroïne a 3 statistiques (0-10) :
- **Affection** : Intérêt romantique
- **Respect/Confiance/Sécurité** : Confiance selon l'héroïne
- **Tension** : Chimie romantique

### Fin du Chapitre 1
5 fins possibles selon vos choix :
- **Fin A** : Une Préférence Se Dessine (une héroïne >= 7)
- **Fin B** : Double Allégeance Émotionnelle (deux héroïnes >= 6)
- **Fin C** : Le Chaos Magnifique (CHAOS >= 6, RÉPUTATION >= 2)
- **Fin D** : Le Cœur Discret (HONNÊTETÉ >= 5)
- **Fin E** : Mauvaise Impression (RÉPUTATION <= -2)

## 🎨 Générer de vraies images

Les images actuelles sont des placeholders. Pour générer de vraies images IA :

### Avec Stable Diffusion (exemple)
```bash
# Prompt pour Léna
"anime style character sprite, young woman 24 years old, 
dark brown wavy shoulder-length hair, hazel eyes, 
wearing casual work clothes with apron, neutral expression, 
white background, visual novel character"
```

### Avec une API
Modifiez `generate_images.py` pour utiliser :
- OpenAI DALL-E API
- Stability AI API
- Midjourney (via Discord bot)

Voir le fichier `generate_images.py` pour les prompts détaillés de chaque image.

## 🛠️ Développement

### Ajouter de nouvelles scènes

Éditez `data/scenario.json` :

```json
"NOUVELLE_SCENE": {
  "id": "NOUVELLE_SCENE",
  "activation": "DAY>=2 && LENA.AFF>=3",
  "background": "assets/images/bg_cafe_bookstore.png",
  "character": "LENA",
  "dialogues": [
    {
      "speaker": "LENA",
      "text": "Votre dialogue ici...",
      "image": "assets/images/lena_expression.png",
      "expression": "neutral"
    }
  ],
  "choices": [
    {
      "text": "Option 1",
      "nextScene": "SCENE_SUIVANTE",
      "effects": {
        "LENA.AFF": 1,
        "HONNETETE": 1
      }
    }
  ]
}
```

### Personnalisation

- **Couleurs** : Modifiez les variables CSS dans `index.html`
- **Polices** : Changez la police dans la section `<style>`
- **Effets** : Ajoutez des animations CSS personnalisées

## 📝 Scénario inclus

Le fichier `scenario.json` contient :
- Scène d'ouverture avec 3 choix initiaux
- Rencontres avec Léna (6 scènes)
- Rencontres avec Maya (6 scènes)
- Rencontres avec Inès (6 scènes)
- Scènes croisées potentielles
- 5 fins différentes

Total : **20+ scènes** avec **60+ choix** possibles

## 🔧 Technologies utilisées

- **HTML5** - Structure sémantique
- **CSS3** - Styles modernes avec gradients et animations
- **JavaScript ES6+** - Moteur de jeu orienté objet
- **JSON** - Format de scénario
- **PIL/Pillow** - Génération d'images (Python)

## 📄 Licence

Projet basé sur le scénario original "Chapitre 1 - Premiers Contacts".
Usage personnel et éducatif uniquement.

## 🙏 Remerciements

Basé sur le document de scénario fourni avec :
- Character Bible complet (descriptions physiques détaillées)
- Système de relations complexes
- Arbres de dialogue branchants
- Conditions d'activation et conséquences

---

**Développé pour démontrer un moteur de visual novel narratif interactif.**

Pour toute question ou amélioration, consultez les fichiers sources dans `/workspace/drague_game/`.
