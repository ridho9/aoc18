from blist import blist

problem = 20307394
recipes = blist([3, 7])

idx1 = 0
idx2 = 1

while len(recipes) < problem + 10:
    # print(f"idx1 @{idx1} {recipes[idx1]} idx2 @{idx2} {recipes[idx2]}")
    res = (int(x) for x in str(recipes[idx1] + recipes[idx2]))
    for x in res:
        recipes.append(x)

    idx1 = (1 + recipes[idx1] + idx1) % len(recipes)
    idx2 = (1 + recipes[idx2] + idx2) % len(recipes)

    # print(recipes)

print(''.join(f'{x}' for x in recipes[-10:]))
