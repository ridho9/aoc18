from blist import blist
import tqdm

problem = 9
recipes = blist([3, 7])

idx1 = 0
idx2 = 1

check = "556061"

while True:
    res = (int(x) for x in str(recipes[idx1] + recipes[idx2]))
    for x in res:
        recipes.append(x)

    idx1 = (1 + recipes[idx1] + idx1) % len(recipes)
    idx2 = (1 + recipes[idx2] + idx2) % len(recipes)

    last = ''.join(f'{x}' for x in recipes[-len(check):])

    if last == check:
        print(len(recipes) - len(check))
        break

print(''.join(f'{x}' for x in recipes[-10:]))
