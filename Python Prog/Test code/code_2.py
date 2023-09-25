import random

def pi_est(n):
    x = 0
    y = 0
    for i in range(n):
        a = random.uniform(1,0)
        b = random.uniform(1,0)
        d = a**2 + b**2
        if d <= 1:
            x+=1
        y+=1
    return (4*x)/y