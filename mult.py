import math
import time 

num = int(input('Write a number '))

def func(a, b, c):
    return "({0} x {1} x {2})".format(a, b, c)

start_time = time.time()

root3 = pow(num, 1/3)
root3 = int(root3)

res = []
start_from = 1
for f_m in range (1, root3 + 1):
    root2 = math.sqrt(num / f_m)
    root2 = int(root2)
    for s_m in range(f_m, root2 + 1):
        if num % (s_m * f_m) == 0:
            t_mult = int(num / (s_m * f_m))
            res.append(func(f_m, s_m, t_mult))
         
print(res)
print("--- %s seconds ---" % (time.time() - start_time))
