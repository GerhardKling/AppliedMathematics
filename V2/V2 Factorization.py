"""
Factorization
@author: GK
"""

import numpy as np

print("ax^2+bx+c=0; Please provide the parameters a, b, c")

# missing = True
# while missing:
#     a = input("Specify a: ")
#     try:
#         a = int(a)
#         missing = False
#     except:
#         print("Please input integers.")
        
def input_parameter(a: str):
    missing = True
    while missing:
        num = input(f"Specify {a}: ")
        try:
            num = int(num)
            missing = False
        except:
            print("Please input integers.")
    return num

parameters = ["a", "b", "c"]
val = []
for par in parameters:
    val.append(input_parameter(par))
    
#Check the discriminant 
dis = val[1]**2-4*val[0]*val[2]

if dis < 0:
    print("Sorry: no real solutions")    
elif dis == 0:
    s0 = -val[1]/(2*val[0])
    print(f"Factorization: (x-{s0})^2")       
else:
    s1 = (-val[1]-np.sqrt(dis))/(2*val[0])
    s2 = (-val[1]+np.sqrt(dis))/(2*val[0])
    print(f"Factorization: (x-{s1})(x-{s2})")
    

    
    