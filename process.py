from pathlib import Path
import sys

item = sys.argv[1]
Path("out-temp").mkdir(exist_ok=True)
Path("out-temp", item).write_text(item, encoding="utf-8")
