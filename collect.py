from pathlib import Path
import shutil
import yaml

with open("params.yaml") as f:
    params = yaml.safe_load(f)
dataset = params["dataset_list"]

shutil.copytree("out-temp", "out")
for path in Path("out").iterdir():
    if path.name not in dataset:
        path.unlink()
