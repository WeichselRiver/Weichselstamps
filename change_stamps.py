#%%
import json
GEBIET = "usa"
attrs = ["pf", "ug", "ge", "variante", "satz", "jahr"]
# with open(f"./static/data/{gebiet}.json") as f:
#     data = json.load(f)
# %%

def get_michnr(x : str):
    print([row for row in data if row["MichNr"] == x])

def add_michnrs(mn_start : int, mn_end : int):
    with open(f"./static/data/{GEBIET}.json", "r") as f:
        data_temp = json.load(f)
    for mn in range(mn_start, mn_end+1):
        data_temp.append(
            {"MichNr" : mn}
        )
    with open(f"./static/data/{GEBIET}.json", "w") as f:
        json.dump(data_temp, f, indent=4)

def set_prop(mn_start : int, mn_end : int, attr : str, prop : str, create=False):
    with open(f"./static/data/{GEBIET}.json", "r") as f:
        data_temp = json.load(f)
    marken = [marke for marke in data_temp if marke["MichNr"] in range(mn_start, mn_end+1)]
    for marke in marken:
        marke[attr] = prop

     
    with open(f"./static/data/{GEBIET}.json", "w") as f:
        json.dump(data_temp, f, indent=4)

# %%
# get_michnr(1)
# %%
# add_michnrs(4,5)
# %%
set_prop(mn_start=1, mn_end=3, attr="pf", prop = 0)