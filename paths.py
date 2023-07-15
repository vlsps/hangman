from pathlib import Path

work_path = Path.cwd()
add_path = '' if work_path.parts[-1] == 'hangman' else '..'

WORDBOOK_PATH: str = Path(work_path, add_path, 'files', 'wordbook.txt').resolve()
TEMPLATES_PATH: str = Path(work_path, add_path, 'files', 'templates.txt').resolve()
