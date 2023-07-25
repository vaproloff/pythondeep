text = ['Lorem ipsum dolor sit amet, consectetur adipising elit.',
        'Nibh tortor id aliquet lectus proin nibh nisl condimentum id.',
        'In fermentum posuere urna nec tincidunt praesent semper feugiat nibh.', ]
with open('new_data.txt', 'w', encoding='utf-8') as f:
    print(f.tell())
    for line in text:
        f.write(f'{line}\n')
        print(f.tell())
    print(f.tell())
print(f.tell())
