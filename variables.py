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
    ('22', 'I have memory lapses')
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

#with open("meds.csv", "r") as file:
#    reader = csv.reader(file)
#    list = []
#    x = 1
#    for row in reader:
#        row = ' '.join(row)
#        row = str(x), row
#        list.append(row)
#        x += 1

#    MEDICATION = tuple(list)

MEDICATION = [
    ('1', '*Brivaracetam*'), ('2', '*Cannabidiol oral solution*'), ('3', 'Epidiolex'), ('4', '*Carbamazepine*'), ('5', 'Epitol'), ('6', 'Tegretol'), ('7', '*Carbamazepine-XR*'), ('8', 'Carbatrol'), ('9', '*Tegretol XR*'), ('10', 'Cenobamate'), ('11', 'Xcopri'), ('12', '*Clobazam*'), ('13', 'Onfi'), ('14', 'Sympazan'), ('15', '*Clonazepam*'), ('16', 'Epitril'), ('17', 'Klonopin'), ('18', 'Rivotril'), ('19', '*Diazepam*'), ('20', 'Valtoco'), ('21', 'Diastat'), ('22', '*Divalproex Sodium*'), ('23', 'Depacon'), ('24', 'Depakote'), ('25', 'Epival'), ('26', '*Divalproex Sodium-ER*'), ('27', 'Depakote ER'), ('28', '*Eslicarbazepine Acetate*'), ('29', 'Aptiom'), ('30', '*Ethosuximide*'), ('31', 'Zarontin'), ('32', '*Ezogabine*'), ('33', 'Potiga'), ('34', '*Felbamate*'), ('35', 'Felbatol'), ('36', '*Fenfluramine*'), ('37', '*Gabapentin*'), ('38', 'Neurontin'), ('39', '*Lacosamide*'), ('40', 'Vimpat'), ('41', '*Lamotrigine*'), ('42', 'Lamictal'), ('43', '*Levetiracetam*'), ('44', 'Keppra'), ('45', 'Roweepra'), ('46', '*Levetiracetam XR*'), ('47', 'Keppra XR'), ('48', '*Lorazepam*'), ('49', 'Ativan'), ('50', '*Midazolam*'), ('51', 'Nayzilam'), ('52', '*Oxcarbazepine*'), ('53', 'Oxtellar XR'), ('54', 'Trileptal'), ('55', '*Perampanel*'), ('56', 'Fycompa'), ('57', '*Phenobarbital*'), ('58', '*Phenytoin*'), ('59', 'Dilantin'), ('60', 'Epanutin'), ('61', 'Phenytek'), ('62', '*Pregabalin*'), ('63', 'Lyrica'), ('64', '*Primidone*'), ('65', 'Mysoline'), ('66', '*Rufinamide*'), ('67', 'Banzel'), ('68', 'Inovelon'), ('69', '*Stiripentol*'), ('70', 'Diacomit'), ('71', '*Tiagabine Hydrochloride*'), ('72', 'Gabitril'), ('73', '*Topiramate*'), ('74', 'Topamax'), ('75', '*Topiramate XR*'), ('76', 'Qudexy XR'), ('77', 'Trokendi XR*'), ('78', '*Valproic Acid*'), ('79', 'Convulex'), ('80', 'Depakene'), ('81', 'Depakine'), ('82', 'Orfiril'), ('83', 'Valporal'), ('84', 'Valprosid'), ('85', '*Vigabatrin*'), ('86', 'Sabril'), ('87', '*Zonisamide*'), ('88', 'Zonegran')
]