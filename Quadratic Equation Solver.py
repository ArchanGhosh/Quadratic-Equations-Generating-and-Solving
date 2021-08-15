import pandas as pd
import numpy as np

import pytesseract

try:
  from PIL import Image
except importerror:
  import Image

quad_final = pd.read_csv("./quadratic_final.csv")

!unzip "./quadratic_images.zip" -d "./quadratic_images"

eqns =[]

path = "../quadratic_images/"

for i in range(0, 1500):
  tmp = pytesseract.image_to_string(Image.open(path+"eqn_"+str(i).zfill(4)+".png"))
  eqns.append(tmp.rstrip("\n\x0c")) 

def preprocess(mp):
  mp = mp.replace('”', '?')
  mp = mp.replace('"', '?')
  mp = mp.replace(' ', '')
  mp = mp.replace('N', '11')
  mp = mp.replace('M', '11')
  mp = mp.replace('T', '1')
  mp = mp.replace('i', '1')
  mp = mp.replace('I', '1')
  mp = mp.replace('B', '8')
  mp = mp.replace('A', '4')
  mp = mp.replace('°', '?')
  mp = mp.replace('xX', 'x')
  mp = mp.replace('O','0')
  mp = mp.replace('k', 'x')
  mp = mp.lower()
  k = mp.split('=')
  j =""
  j+= k[0]
  if k[1][0] == '-':
    if k[1][-1] =='?':
      if k[0][0] == '-':
        j = k[1][1:] + j
      else:
        j = k[1][1:] + "+"+j
    else:
      j+= "+"
      j += k[1][1:]
  elif k[1][0] =='0':
    pass
  else:
    j+= "-"
    j+=k[1]

  print(j)

  tsx = j.split('?')

  try:
    try:
      if 'x' not in tsx[1]:
        tsx[1] = '0x'+tsx[1]
      if tsx[1][-1] == 'x':
        tsx[1]+= '0'
      j_1 = tsx[1].split('x')

      if tsx[0] == 'x':
        a = 1
      else:
        a = int(tsx[0][:-1])

      if j_1[0] == '+':
        b = 1
      elif j_1[0] == '-':
        b = -1
      else:
        b = int(j_1[0])
      c = j_1[1]
      print(a,b,c)
      
    except:

      p = tsx[0]

      s = p.split(')')

    
      rt = []
      for i in s:
        if i == "":
          continue
        m = i.split('x')
        j_1 = int(m[1])
        rt.append(-j_1)
      a = 1
      b = rt[0]+rt[1]
      c = rt[0]*rt[1]

      print("except ", a,b,c)

  except:
    a=0
    b=0
    c=0    
  return int(a), int(b), int(c)
coef_a=[]
coef_b=[]
coef_c=[]
for i in eqns:
  a, b, c = preprocess(i)
  coef_a.append(a)
  coef_b.append(b)
  coef_c.append(c)

root1 = []
root2 = []

roots = quad_final['Roots'].str.split(',')

for i in roots:
  root1.append(float(i[0]))
  root2.append(float(i[1]))

import math
calc_root1 = []
calc_root2 = []

for i in range(len(coef_a)):
  a = coef_a[i]
  b = coef_b[i]
  c = coef_c[i]
  try:
    r1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    r2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
  except:
    r1=0
    r2=0
  calc_root1.append(round(r1, 4)) 
  calc_root2.append(round(r2, 4))

from sklearn.metrics import mean_squared_error

r1_rmse = math.sqrt(mean_squared_error(root1, calc_root1))
r2_rmse = math.sqrt(mean_squared_error(root2, calc_root2))

print(r1_rmse, r2_rmse)

c1=0
c2=0
for i in range(len(root1)):
  if(root1[i] == calc_root1[i]):
    c1+=1
  if(root2[i] == calc_root2[i]):
    c2+=1

r1_acc = c1/len(calc_root1)
r2_acc = c2/len(calc_root2)

print(r1_acc, r2_acc)
  