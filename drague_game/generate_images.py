# Générateur d'Images pour Visual Novel

Ce script génère des images placeholder pour le jeu. Pour de vraies images IA, utilisez une API comme Stable Diffusion ou DALL-E.

## Structure des images nécessaires

### Backgrounds (1920x1080)
- bg_neighborhood.png - Rue de quartier européen charmant
- bg_cafe_bookstore.png - Intérieur café-librairie cosy
- bg_market_square.png - Place de marché animée
- bg_photo_studio.png - Extérieur studio photo
- bg_evening_party.png - Soirée festive en extérieur
- bg_street_walk.png - Rue résidentielle calme
- bg_sunset.png - Coucher de soleil sur le quartier
- bg_neighborhood_afternoon.png - Quartier l'après-midi

### Sprites Personnages (400x600)

#### Léna Vernet (24 ans)
- Cheveux: châtains foncés ondulés, longueur omoplates
- Yeux: noisette/brun doré
- Silhouette: élancée, 1.68m
- Style: vêtements pratiques, tablier de travail

Expressions:
- neutral - Expression neutre professionnelle
- slightly_annoyed - Légèrement agacée, sourcils froncés
- hopeful - Espoir, mains jointes
- small_smile - Petit sourire sincère
- warm_smile - Sourire chaleureux
- surprised - Surprise, yeux écarquillés
- relieved - Soulagée, épaules détendues
- deadpan - Expression plate, impassible
- amused_mockery - Moquerie amusée, sourire en coin
- competitive_smirk - Sourire compétitif
- challenging - Défi, regard intense
- genuinely_impressed - Vraiment impressionnée
- respectful_smile - Sourire respectueux
- trying_not_to_smile - Essaie de ne pas rire
- hesitating - Hésitante, garde levée
- rare_vulnerability - Vulnérabilité rare, yeux doux
- back_to_business - Retour au professionnel

#### Maya Rivière (26 ans)
- Cheveux: bruns avec reflets cuivrés, volumineux
- Yeux: verts-noisette
- Silhouette: athlétique souple, 1.72m
- Style: décontracté, accessoires colorés

Expressions:
- flustered_but_happy - Empêtrée mais heureuse
- bright_smile - Grand sourire éclatant
- grateful_smile - Sourire reconnaissant
- enthusiastic - Enthousiaste, animée
- mock_offended_then_laughing - Faussement offensée puis rit
- playful_challenge - Défi ludique
- pure_joy - Joie pure, bras levés
- breathless_happy - Essoufflée heureuse
- friendly_smile - Sourire amical
- slightly_guarded - Légèrement sur la défensive
- urgent_pleading - Supplication urgente
- hopeful_desperate - Espoir désespéré
- excited_supportive - Excitée et supportive
- proud_happy - Fière et heureuse
- beaming - Rayonnante
- uncontrollable_laughter - Rire incontrôlable
- thrilled - Ravie, excitée
- understanding_smile - Sourire compréhensif

#### Inès Delcourt (25 ans)
- Cheveux: brun-noir longs et raides
- Yeux: brun foncé presque noirs
- Silhouette: fine, 1.65m
- Style: sobre, sac photo toujours présent

Expressions:
- concentrated - Concentrée sur son appareil
- calm_direct - Calme et directe
- small_genuine_smile - Petit sourire sincère rare
- taken_aback - Prise au dépourvu
- slightly_impressed - Légèrement impressionnée
- hesitant_but_open - Hésitante mais ouverte
- passionate - Passionnée, yeux animés
- soft_approving - Approbation douce
- warm_quiet - Chaleur tranquille
- analytical_respectful - Analyse respectueuse
- stoic - Stoïque, neutre
- slightly_amused - Légèrement amusée

## Utilisation avec Stable Diffusion

Exemple de prompt pour Léna:
```
anime style character sprite, young woman 24 years old, dark brown wavy shoulder-length hair, hazel eyes, wearing casual work clothes with apron, neutral professional expression, standing in café-bookstore, waist-up portrait, white background, visual novel character, clean lines, detailed face
--ar 2:3 --v 5
```

Exemple de prompt pour background café:
```
cozy café-bookstore interior, wooden shelves filled with books, tables with coffee cups, warm ambient lighting, inviting atmosphere, digital art, detailed background for visual novel, no characters, 1920x1080
--ar 16:9 --v 5
```

## Script Python de génération (placeholder)

```python
import os
from PIL import Image, ImageDraw, ImageFont

def create_placeholder_image(filename, width, height, color, text):
    img = Image.new('RGB', (width, height), color=color)
    draw = ImageDraw.Draw(img)
    
    # Add text
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    
    # Center text
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    draw.text((x, y), text, fill='white', font=font)
    
    img.save(filename)
    print(f"Created: {filename}")

# Create directories
os.makedirs('assets/images', exist_ok=True)

# Create backgrounds
backgrounds = [
    ('bg_neighborhood.png', 'Neighborhood Street'),
    ('bg_cafe_bookstore.png', 'Café Bookstore'),
    ('bg_market_square.png', 'Market Square'),
    ('bg_photo_studio.png', 'Photo Studio'),
    ('bg_evening_party.png', 'Evening Party'),
    ('bg_street_walk.png', 'Street Walk'),
    ('bg_sunset.png', 'Sunset'),
    ('bg_neighborhood_afternoon.png', 'Afternoon'),
]

for filename, text in backgrounds:
    create_placeholder_image(
        f'assets/images/{filename}',
        1920, 1080,
        (102, 126, 234),  # Purple-blue
        text
    )

# Create character sprites
characters = {
    'lena': [
        'greeting_01', 'greeting_02', 'request_01', 'smile_01',
        'grateful_01', 'surprised_01', 'finding_01', 'relieved_01',
        'staring_01', 'smirking_01', 'walking_away_01', 'challenge_01',
        'challenge_02', 'searching_01', 'impressed_01', 'approval_01',
        'deadpan_02', 'suppressed_laugh_01', 'hesitating_01',
        'vulnerable_01', 'composing_01', 'refocusing_01'
    ],
    'maya': [
        'struggling_01', 'bags_01', 'introducing_01', 'relieved_01',
        'excited_01', 'defensive_01', 'music_reaction_01',
        'dance_invitation_01', 'dancing_01', 'post_dance_01',
        'understanding_01', 'protective_01', 'party_01', 'panic_01',
        'begging_01', 'cheering_01', 'post_song_01', 'compliment_01',
        'laughing_hard_01', 'tears_of_laughter_01', 'excited_future_01',
        'accepting_01'
    ],
    'ines': [
        'working_01', 'focused_01', 'looking_01', 'introducing_01',
        'soft_smile_01', 'surprised_01', 'reviewing_01',
        'showing_photo_01', 'explaining_01', 'invitation_01',
        'instruction_01', 'appreciating_01', 'grateful_quiet_01',
        'analyzing_01', 'stoic_01', 'admitting_01'
    ]
}

colors = {
    'lena': (255, 107, 107),  # Red-pink
    'maya': (254, 202, 87),   # Yellow
    'ines': (162, 155, 254)   # Purple
}

for char, expressions in characters.items():
    for expr in expressions:
        filename = f'{char}_{expr}.png'
        create_placeholder_image(
            f'assets/images/{filename}',
            400, 600,
            colors[char],
            f'{char.upper()}\n{expr}'
        )

print("\nAll placeholder images created!")
print("Replace with AI-generated images for production.")
```

## Notes importantes

1. **Consistance des personnages**: Gardez les mêmes traits physiques pour chaque personnage à travers toutes les expressions
2. **Style artistique**: Choisissez un style cohérent (anime, semi-réaliste, peinture digitale, etc.)
3. **Format**: PNG avec transparence pour les sprites
4. **Résolution**: 
   - Backgrounds: 1920x1080 (16:9)
   - Sprites: 400x600 minimum
5. **Droits**: Assurez-vous d'avoir les droits pour les images générées
