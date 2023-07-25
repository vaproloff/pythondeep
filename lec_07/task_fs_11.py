import os
from pathlib import Path

os.rename('old_name.py', 'newest_file.py')

p = Path('old_file.py')
p.rename('new_file.py')

Path('new_file.py').rename('newest_file.py')
