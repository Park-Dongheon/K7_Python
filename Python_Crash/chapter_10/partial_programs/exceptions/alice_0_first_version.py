from pathlib import Path


path = Path('alice2.txt')
contents = path.read_text(encoding='utf-8')