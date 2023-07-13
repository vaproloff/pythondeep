"""map(function, iterable)"""
texts = ['Привет', 'ЗДАРОВА', 'привеТствую']
res = map(lambda x: x.lower(), texts)
print(*res)
