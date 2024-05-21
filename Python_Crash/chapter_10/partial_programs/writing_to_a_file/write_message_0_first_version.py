from pathlib import Path
import os
print(f"현재경로={os.getcwd()}")

path = Path('programming.txt')
path.write_text("I love programming.")