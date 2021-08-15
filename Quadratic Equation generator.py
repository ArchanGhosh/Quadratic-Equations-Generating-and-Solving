import random
import pandas as pd
import numpy as np
import math

#Creating a List to store the randomly generated Coefficients, roots and the equation 
coef_a = []
coef_b = []
coef_c = []

root_1 = []
root_2 = []

eqn = []

# ax2+bx+c = 0 
count = 375

while(1):
  a = random.randint(1,10)
  b = random.randint(-36, 101)
  c = random.randint(-100,150)
  
  if ((b**2 - 4*a*c)>0):
    count-= 1
    x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)

    coef_a.append(a)
    coef_b.append(b)
    coef_c.append(c)

    root_1.append(x1)
    root_2.append(x2)

    if (a == 1):
      equa = "x\u00b2"

    else:
      equa = str(a)+"x\u00b2" 

    if (b == 1):
      equa = equa + " + " + "x"
    elif (b== -1):
      equa = equa + " - " + "x"
    elif (b>0):
      equa = equa + " + " + str(b) + "x"
    elif (b<0):
      equa = equa + " - " + str(-b) + "x"
    
    if (c>0):
      equa = equa + " + " + str(c)
    elif (c<0):
      equa = equa + " - " + str(-c)

    equa = equa + " = 0"

    eqn.append(equa)
    equa =""

    if (count==0):
      break

#ax2 + bx = -c

count = 375

while(1):
  a = random.randint(10,20)
  b = random.randint(-36, 101)
  c = random.randint(-100,150)
  
  if ((b**2 - 4*a*c)>0):
    count-= 1
    x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)

    coef_a.append(a)
    coef_b.append(b)
    coef_c.append(c)

    root_1.append(x1)
    root_2.append(x2)

#ax2+bx = c
    if (a == 1):
      equa = "x\u00b2"

    else:
      equa = str(a)+"x\u00b2" 

    if (b == 1):
      equa = equa + " + " + "x"
    elif (b== -1):
      equa = equa + " - " + "x"
    elif (b>0):
      equa = equa + " + " + str(b) + "x"
    elif (b<0):
      equa = equa + " - " + str(-b) + "x"
    
    if (c>0):
      equa = equa + " = " + str(-c)
    else:
      equa = equa + " = " + str(-c) 

    eqn.append(equa)
    equa =""

    if (count==0):
      break

#bx+c = -ax2
count = 375

while(1):
  a = random.randint(20,37)
  b = random.randint(-36, 101)
  c = random.randint(-100,150)
  
  if ((b**2 - 4*a*c)>0):
    count-= 1
    x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)

    coef_a.append(a)
    coef_b.append(b)
    coef_c.append(c)

    root_1.append(x1)
    root_2.append(x2)


    if (b == 1):
      equa = equa + "x"
    elif (b== -1):
      equa = equa + " - " + "x"
    elif (b>0):
      equa = equa + str(b) + "x"
    elif (b<0):
      equa = equa + " - " + str(-b) + "x"
    
    if (c>0):
      equa = equa + " + " + str(c)
    elif (c<0):
      equa = equa + " - " + str(-c)

    if (a == 1):
      equa = equa + " = " + "-"+"x\u00b2"
    else:
      equa = equa + " = " + "-" + str(a)+"x\u00b2"

    eqn.append(equa)
    equa =""

    if (count==0):
      break

#for (x-r1)(x-r2) = 0
count = 375

while (1):
  r1 = random.randint(-10,25)
  r2 = random.randint(-25, 25)

  if (r1==0) or (r2==0):
    continue 

  count-= 1
  root_1.append(r1)
  root_2.append(r2)

  coef_a.append(1)
  coef_b.append(r1+r2)
  coef_c.append(r1*r2)

  equa=""

  if (r1>0):
    equa = "(x - " + str(r1) +")"
  else:
    equa = "(x + "+ str(-r1) +")"
  if (r2>0):
    equa = equa + "(x - " + str(r2) + ")"
  else:
    equa = equa + "(x + " + str(-r2) + ")"

  equa = equa + " = 0"
  eqn.append(equa)
  equa =""

  if (count==0):
      break

#Rounding the Roots to 4 decimal place

r1 = [round(num, 4) for num in root_1]
r2 = [round(num, 4) for num in root_2]

#Creating a dataframe to store the entire dataset

quad = pd.DataFrame()

quad['a'] = coef_a
quad['b'] = coef_b
quad['c'] = coef_c

quad['root_1'] = r1
quad['root_2'] = r2

quad['equation'] = eqn


from sklearn.utils import shuffle
quad = shuffle(quad)
quad = quad.reset_index(drop=True)


#Creating a ID path Directory to Locate the different Equations
id = []
path = []
for i in range(0,1500):
  id.append('eqn_'+str(i).zfill(4))
  path.append('quadratic/'+id[i])

quad.insert(loc=0, column='id', value=id)
quad.insert(loc =1, column='path', value=path)
  