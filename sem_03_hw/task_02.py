# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

FREQUENT_QTY = 10
PUNCTUATION = '''.,;:!?#@%&*+=\\/()[]{}<>-—«»'"'''

some_text = '''Another useful data type built into Python is the dictionary (see Mapping Types — dict). Dictionaries
are sometimes found in other languages as “associative memories” or “associative arrays”. Unlike sequences, which are
indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type; strings and numbers
can always be keys. Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains
any mutable object either directly or indirectly, it cannot be used as a key. You can’t use lists as keys, since lists
can be modified in place using index assignments, slice assignments, or methods like append() and extend().
It is best to think of a dictionary as a set of key: value pairs, with the requirement that the keys are unique
(within one dictionary). A pair of braces creates an empty dictionary: {}. Placing a comma-separated list of key:value
pairs within the braces adds initial key:value pairs to the dictionary; this is also the way dictionaries are written
on output.
The main operations on a dictionary are storing a value with some key and extracting the value given the key. It is
also possible to delete a key:value pair with del. If you store using a key that is already in use, the old value
associated with that key is forgotten. It is an error to extract a value using a non-existent key.
Performing list(d) on a dictionary returns a list of all the keys used in the dictionary, in insertion order (if you
want it sorted, just use sorted(d) instead). To check whether a single key is in the dictionary, use the in keyword.
Here is a small example using a dictionary:'''

pretty_text = some_text.lower()
for symbol in PUNCTUATION:
    pretty_text = pretty_text.replace(symbol, ' ')

words = pretty_text.split()
words_qty = {word: words.count(word) for word in words}
words_sorted = sorted(words_qty, key=words_qty.get, reverse=True)

frequent_words = {}
for word in words_sorted[:min(FREQUENT_QTY, len(words_qty))]:
    frequent_words[word] = words_qty[word]
print(f'{FREQUENT_QTY} cамых частых слов:\n{frequent_words}')
