from pathlib import Path
import sys

item = sys.argv[1]
Path("out").mkdir(exist_ok=True)
Path("out", item).write_text(item, encoding="utf-8")
