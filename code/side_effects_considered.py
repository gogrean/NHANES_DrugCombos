import os
import glob
import json
import re

root_dir = "/Users/gogrean/Documents/Insight_Fellowship/Research/Mental_Health/NHANES_Survey/data/side_effects/"
os.chdir(root_dir)

side_effects = {}
for fname in glob.glob("*.json"):
    drug_name = re.search("(.*).json", fname).group(1).upper()
    side_effects[drug_name] = {}
    with open(fname, 'r') as f:
        data = json.load(f)
        for d in data[:10]:
            side_effects[drug_name][d[0]] = d[1]

se = set()
for m in side_effects:
    se.update(set(side_effects[m].keys()))

with open('side_effects_considered.json', 'w') as f:
    json.dump(list(se), f)
