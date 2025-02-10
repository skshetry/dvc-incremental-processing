from pathlib import Path
import yaml

with open("params.yaml") as f:
    params = yaml.safe_load(f)
dataset = params["dataset_list"]


out = Path("out")
if out.is_dir():
    for path in out.iterdir():
        if path.name not in dataset:
            print("Removing", path)
            path.unlink()
