import itertools as it

def is_solution(prem):
    for i1,i2 in it.combinations(range(len(prem)),2):
        if abs(i1-i2) == abs(prem[i1]-prem[i2]):
            return False
    return True


for prem in it.permutations(range(8)):
    if is_solution(prem):
        print(prem)
        exit()