import os

repos = [
    "git@github.com:ltgoslo/norne.git",
    # only if you want to use the document-aligned files:
    # "git@github.com:tollefj/UD-NARC.git",
]

for repo in repos:
    name = repo.split("/")[-1].split(".")[0]
    if os.path.exists(name):
        print(f"Skipping {name} - already downloaded")
        continue
    os.system(f"git clone --depth 1 --branch master {repo}")
    os.system(f"git clone --depth 1 --branch main {repo}")
    os.system(f"rm -rf {name}/.git")
