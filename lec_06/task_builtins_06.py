import random
from sys import argv

data = [2, 4, 6, 8, 42, 73]

print(random.uniform(int(argv[1]), int(argv[2])))
print(random.randrange(int(argv[1]), int(argv[2]), int(argv[1])))
print(random.sample(range(int(argv[1]), int(argv[2]), int(argv[1])), 10))
