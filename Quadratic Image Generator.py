#Creating the images for respective equations
import pandas as pd

quad = pd.read_csv(`NAME and LOCATION of the QUADRATIC CSV`)

from PIL import ImageFont, ImageDraw, Image

for i in range(len(quad)):
  W, H = (300,100)
  eq = quad.iloc[i,7]
  font = ImageFont.truetype(r'../Hind_Siliguri/HindSiliguri-Regular.ttf', 25)

  im = Image.new("RGBA",(W,H),"white")
  draw = ImageDraw.Draw(im)
  w, h = draw.textsize(eq)
  draw.text(((W-w)/2 - 30,(H-h)/2 - 20), eq, font=font, fill="black")

  im.save("../quadratic/"+str(quad.iloc[i,0])+".png", "PNG")