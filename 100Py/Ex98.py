"""
Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
"""

def solve_animals(heads, legs):
    for chickens in range(heads+1):
        rabbits = heads - chickens
        if 2*chickens + 4*rabbits == legs:
            return chickens, rabbits
    return None, None

sol = solve_animals(35, 94)
if sol:
    print sol
else:
    print "no solution"