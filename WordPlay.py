import random

word_definitions = {
    'Dog': {
        'Synonyms': ['Canine', 'Pooch', 'Hound', 'Fido', 'Puppy'],
        'Definition': 'A furry animal that barks and is often kept as a pet.'
    },
    'Car': {
        'Synonyms': ['Automobile', 'Vehicle', 'Auto', 'Machine', 'Motorcar'],
        'Definition': 'A machine with wheels that people drive to get from one place to another.'
    },
    'Book': {
        'Synonyms': ['Tome', 'Volume', 'Manuscript', 'Publication', 'Literary work'],
        'Definition': 'A collection of pages with words and stories that you can read.'
    },
    'Sun': {
        'Synonyms': ['Star', 'Sol', 'Daystar', 'Sunlight', 'Solar orb'],
        'Definition': 'The big, bright, hot ball of light in the sky that gives us warmth and light during the day.'
    },
    'Shoes': {
        'Synonyms': ['Footwear', 'Sneakers', 'Boots', 'Sandals', 'Slippers'],
        'Definition': 'Things you wear on your feet to protect them and make walking more comfortable.'
    },
    'Moon': {
        'Synonyms': ['Lunar', 'Satellite', 'Celestial body', 'Orb', 'Crescent'],
        'Definition': 'The round, white object in the night sky that glows and changes shape.'
    },
    'Computer': {
        'Synonyms': ['PC', 'Machine', 'Device', 'System', 'Processor'],
        'Definition': 'An electronic device that helps you do tasks, play games, and find information.'
    },
    'Rain': {
        'Synonyms': ['Precipitation', 'Downpour', 'Shower', 'Drizzle', 'Rainfall'],
        'Definition': 'Water falling from the sky in small drops when the clouds are dark.'
    },
    'Friend': {
        'Synonyms': ['Companion', 'Pal', 'Buddy', 'Mate', 'Chum'],
        'Definition': 'Someone you like and enjoy spending time with.'
    },
    'Bed': {
        'Synonyms': ['Mattress', 'Cot', 'Sleeping platform', 'Bunk', 'Bedstead'],
        'Definition': 'A piece of furniture for sleeping or resting.'
    },
    'Clock': {
        'Synonyms': ['Timepiece', 'Watch', 'Chronometer', 'Timekeeper', 'Horologe'],
        'Definition': 'Round or square thing that tells you the time.'
    },
    'Rainbow': {
        'Synonyms': ['Spectrum', 'Arc', 'Prismatic colors', 'Iris', 'Color spectrum'],
        'Definition': 'Colorful arch in the sky after it rains.'
    },
    'Chair': {
        'Synonyms': ['Seat', 'Throne', 'Bench', 'Stool', 'Armchair'],
        'Definition': 'Something you sit on, usually with a back and four legs.'
    },
    'Phone': {
        'Synonyms': ['Telephone', 'Cellphone', 'Mobile', 'Smartphone', 'Handset'],
        'Definition': 'Device that helps you talk to people far away.'
    },
    'Tree': {
        'Synonyms': ['Plant', 'Woody plant', 'Flora', 'Timber', 'Shrub'],
        'Definition': 'Tall plant with leaves and branches.'
    },
    'Key': {
        'Synonyms': ['Lock opener', 'Code', 'Clue', 'Solution', 'Password'],
        'Definition': 'Small metal tool to unlock doors or start a car.'
    },
    'Cake': {
        'Synonyms': ['Pastry', 'Dessert', 'Confection', 'Sweet', 'Gateau'],
        'Definition': 'Sweet dessert often served at celebrations.'
    },
    'Bridge': {
        'Synonyms': ['Span', 'Crossing', 'Viaduct', 'Arch', 'Connection'],
        'Definition': 'Structure that helps you cross over water or valleys.'
    },
    'Cloud': {
        'Synonyms': ['Nebula', 'Mist', 'Vapor', 'Cumulus', 'Stratus'],
        'Definition': 'Fluffy collection of water vapor in the sky.'
    },
    'Cup': {
        'Synonyms': ['Mug', 'Goblet', 'Chalice', 'Vessel', 'Container'],
        'Definition': 'Small container for holding liquids, often with a handle.'
    },
    'Camera': {
        'Synonyms': ['Photographic device', 'Cam', 'Lens', 'Apparatus', 'Phone'],
        'Definition': 'Device that captures and stores images or videos.'
    },
    'Hat': {
        'Synonyms': ['Headgear', 'Cap', 'Bonnet', 'Lid', 'Topper'],
        'Definition': 'Head covering, sometimes for fashion or protection from the sun.'
    },
    'Ocean': {
        'Synonyms': ['Sea', 'Deep', 'Brine', 'Blue', 'Saltwater'],
        'Definition': 'Vast body of saltwater covering much of the Earth.'
    },
    'Pencil': {
        'Synonyms': ['Writing implement', 'Drawing tool', 'Graphite stick', 'Lead pencil', 'Sketching instrument'],
        'Definition': 'Writing tool made of wood with a graphite core.'
    }
}
player_score = 0
for total_ques in range(10):
    count=0
    str_word=(random.sample(list(word_definitions),1))
    str_word=str(str_word[0])
    dict_word=word_definitions[str_word]

    del word_definitions[str_word]
        
    ans=input("Guss the word: {}\n".format(dict_word['Definition']))
    ans=ans.title()

    
    if ans==str_word:
        print("Correct Answer. \n")
        player_score+=1
        continue
    else:
        for values in dict_word['Synonyms']:
            if values == ans:
                count+=1
                    
    if count >= 1:
        print("Correct Answer. \n")
        player_score+=1

    else:
        print("Wrong Answer, correct answer is {}\n".format(str_word))
    
print(f"You Scored : {player_score} out of 10.\n")