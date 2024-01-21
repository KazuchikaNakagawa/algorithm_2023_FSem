import random
db = {}
with open("algorithm.csv") as f:
    sdatas = f.read().replace("\n", "").split(",")
    for sdata in sdatas:
        tpl = sdata.split(":")
        db[tpl[0]] = tpl[1]

while len(db) != 0:
    q = random.choice(list(db.keys()))
    a = db[q]
    print(f"\033[34m{q}\033[m")
    ans = input("PRESS ENTER or Enter Answer: ")
    if ans == "q":
        print("q means quit.")
        exit()
    print(f"\033[31mA: {a}\033[m")
    if len(ans) != 0 and ans in a:
        print(" -- might be correct!")
    print("-----------")
    del db[q]
