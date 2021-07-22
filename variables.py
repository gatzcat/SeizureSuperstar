import csv 

PRE_ICTAL = [
    ('1', 'Bitter, acidic taste'),
    ('2', 'Déja vu (feeling of familiarity with a person, place, or thing without having experienced it)'),
    ('3', 'Jamais vu (feeling of unfamiliarity with a person, place, or thing despite having already experienced it)'), 
    ('4', 'Flickering vision'), 
    ('5', 'Hallucinations'), 
    ('6', 'Head, arm, or leg pain'),
    ('7', 'Dizziness'), 
    ('8', 'Nausea/stomachache'), 
    ('9', 'Numbness'), 
    ('10', 'Out-of-body sensation'), 
    ('11', 'Ringing or buzzing sounds'),
    ('12', 'Strange, offensive smells'), 
    ('13', 'Strong feelings of joy, sadness, fear, or anger'), 
    ('14', 'Subtle arm or leg twitching'), 
    ('15', 'Tingling'),
    ('16', 'Vision loss or blurring')
]

DURING = [
    ('1', 'I am aware of my surroundings'), 
    ('2', 'I am confused'), 
    ('3', 'I have strange sensations'), 
    ('4', 'I have intense emotions'), 
    ('5', 'I walk about'), 
    ('6', 'I rub/move my hands'), 
    ('7', 'I stop talking'), 
    ('8', 'I stop moving'), 
    ('9', 'I flutter my eyes'), 
    ('10', 'I close my eyes'), 
    ('11', 'I smack my lips or chew'), 
    ('12', 'I tense up/stiffen'), 
    ('13', 'I lose muscle strength'), 
    ('14', 'I head drops/nods'), 
    ('15', 'I fall over'), 
    ('16', 'I convulse'), 
    ('17', 'I twitch lightly'), 
    ('18', 'I drool'), 
    ('19', 'I lose bladder or bowel control'), 
    ('20', 'I have difficulty breathing'),
    ('21', 'I experience hearing loss'),
    ('22', 'I have memory lapses'),
    ('23', 'I don\'t know yet')
]

POST_ICTAL = [
    ('1', 'Limb weakness'),
    ('2', 'Body soreness'),
    ('3', 'Confusion'), 
    ('4', 'Lost Vocabulary/Names'), 
    ('5', 'Drowsiness'), 
    ('6', 'Fear'),
    ('7', 'Embarrassment'), 
    ('8', 'Sadness'), 
    ('9', 'General discomfort'), 
    ('10', 'Headaches/Migraines'), 
    ('11', 'Hypertension'),
    ('12', 'Memory Loss'), 
    ('13', 'Nausea'), 
    ('14', 'Thirst')
]

TRIGGERS = [
    ('1', 'Missed medication'),
    ('2', 'Lack of sleep'),
    ('3', 'Stress'), 
    ('4', 'Alcohol'), 
    ('5', 'Menstruation'), 
    ('6', 'Fear'),
    ('7', 'Fever/Cold/Sickness'), 
    ('8', 'Flashing Lights'), 
    ('9', 'Illicit Drug Use'), 
    ('10', 'Medication/Dosage change'), 
    ('11', 'Hypertension'),
    ('12', 'Hyperthermia'), 
    ('13', 'High Ketones'), 
    ('14', 'Thirst')
]

# The list could have been hard coded but calling from a CSV probably allows for easier updating when new medications are released
with open("meds.csv", "r") as file:
    reader = csv.reader(file)
    list = []
    x = 1
    for row in reader:
        row = ' '.join(row)
        row = str(x), row
        list.append(row)
        x += 1

    MEDICATION = list

def unlist(data, array):
        entry = []
        for d in data:
            entry.append(array[int(d) - 1][1]
            + ', ')
        entry = ''.join(entry)
        return entry