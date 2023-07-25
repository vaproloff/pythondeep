last = before = 0
text = ['Lorem ipsum dolor sit amet, consectetur adipising elit.',
        'Nibh tortor id aliquet lectus proin nibh nisl condimentum id.',
        'In fermentum posuere urna nec tincidunt praesent semper feugiat nibh.', ]
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
        print(f'{last = }, {before = }')
    print(f'{last = }, {before = }')
    print(f'{f.seek(before, 0) = }')
    f.write('\n'.join(text))
