#!/usr/bin/env python
"""
Script pour adapter les fixtures Django au format correct.
- Ajoute les données Quizz manquantes
- Réorganise les données dans le bon ordre (Quizz -> Questions -> Answer)
- Corrige le format des dates
"""
import json
from datetime import datetime

# Mapping des quizz avec leurs informations
# Vous pouvez ajuster ces valeurs selon vos besoins
QUIZZ_DATA = {
    5: {
        "title": "JARGON MARKET",
        "topic": "JARGON MARKET",
        "number_of_questions": 50,
        "time": 30,
        "require_score_to_pass": 70
    },
    6: {
        "title": "EDITEURS / SOFTS / OUTILS",
        "topic": "EDITEURS / SOFTS / OUTILS",
        "number_of_questions": 92,
        "time": 45,
        "require_score_to_pass": 70
    },
    7: {
        "title": "LANGAGES / FRAMEWORKS / BIBLIOTHEQUES",
        "topic": "LANGAGES / FRAMEWORKS / BIBLIOTHEQUES",
        "number_of_questions": 45,
        "time": 30,
        "require_score_to_pass": 70
    },
    8: {
        "title": "BUISNESS MODEL",
        "topic": "BUISNESS MODEL",
        "number_of_questions": 10,
        "time": 15,
        "require_score_to_pass": 70
    },
    9: {
        "title": "METRICS",
        "topic": "METRICS",
        "number_of_questions": 3,
        "time": 10,
        "require_score_to_pass": 70
    }
}

def fix_date_format(date_str):
    """Convertit le format de date ISO avec Z en format Django"""
    if date_str.endswith('Z'):
        # Remplace Z par +00:00 pour le timezone UTC
        return date_str.replace('Z', '+00:00')
    return date_str

def adapt_fixtures(input_file, output_file):
    """Adapte les fixtures au format Django correct"""
    
    # Charger les données existantes
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Séparer les données par modèle
    quizz_data = []
    questions_data = []
    answers_data = []
    
    for item in data:
        model = item.get('model', '')
        if model == 'api.quizz':
            quizz_data.append(item)
        elif model == 'api.questions':
            # Corriger le format de date
            if 'created' in item['fields']:
                item['fields']['created'] = fix_date_format(item['fields']['created'])
            questions_data.append(item)
        elif model == 'api.answer':
            # Corriger le format de date
            if 'created' in item['fields']:
                item['fields']['created'] = fix_date_format(item['fields']['created'])
            answers_data.append(item)
    
    # Créer les entrées Quizz manquantes
    existing_quizz_ids = {item['pk'] for item in quizz_data}
    for quizz_id, quizz_info in QUIZZ_DATA.items():
        if quizz_id not in existing_quizz_ids:
            quizz_entry = {
                "model": "api.quizz",
                "pk": quizz_id,
                "fields": {
                    "title": quizz_info["title"],
                    "topic": quizz_info["topic"],
                    "number_of_questions": quizz_info["number_of_questions"],
                    "time": quizz_info["time"],
                    "require_score_to_pass": quizz_info["require_score_to_pass"]
                }
            }
            quizz_data.append(quizz_entry)
    
    # Trier les quizz par pk
    quizz_data.sort(key=lambda x: x['pk'])
    
    # Réorganiser les données dans le bon ordre: Quizz -> Questions -> Answer
    # Trier les questions par pk pour maintenir la cohérence
    questions_data.sort(key=lambda x: x['pk'])
    answers_data.sort(key=lambda x: x['pk'])
    
    # Assembler les données dans le bon ordre
    final_data = quizz_data + questions_data + answers_data
    
    # Sauvegarder le fichier adapté
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(final_data, f, ensure_ascii=False, indent=4)
    
    print("Fixtures adaptees avec succes!")
    print(f"  - {len(quizz_data)} quizz")
    print(f"  - {len(questions_data)} questions")
    print(f"  - {len(answers_data)} reponses")
    print(f"  - Fichier sauvegarde: {output_file}")

if __name__ == '__main__':
    input_file = 'api/fixtures/data.json'
    output_file = 'api/fixtures/data.json'
    
    # Creer une sauvegarde
    import shutil
    backup_file = 'api/fixtures/data.json.backup'
    shutil.copy2(input_file, backup_file)
    print(f"Sauvegarde creee: {backup_file}")
    
    adapt_fixtures(input_file, output_file)
