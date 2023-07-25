text = ['Lorem ipsum dolor sit amet, consectetur adipising elit.',
        'Nibh tortor id aliquet lectus proin nibh nisl condimentum id.',
        'In fermentum posuere urna nec tincidunt praesent semper feugiat nibh.', ]
with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        print(line, file=f)
