import pickle


def func(a, b, c):
    return a * b * c


with open('my_dict.pickle', 'rb') as f:
    new_dict = pickle.load(f)
print(f'{new_dict = }')
print(f'{new_dict["functions"][0](2, 3, 4) = }')
