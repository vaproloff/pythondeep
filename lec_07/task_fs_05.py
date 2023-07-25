import os
from pathlib import Path

# os.rmdir('dir')
# Path('some_dir').rmdir()
os.rmdir('dir/other_dir/new_os_dir')
Path('some_dir/dir/new_path_dir').rmdir()
