import csv
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np
img = Image.open('C:/Users/sriordan/Desktop/blank.png')
draw_img = ImageDraw.Draw(img)

data = []

class info:
	def __init__(self, name, color, number):
		self.name = name
		self.color = color
		self.number = number
	
	def name(self):
		return name
	def color(self):
		return color
	def number(self):
		return number

with open('C:/Users/sriordan/Downloads/testdata - Sheet1.csv', 'rb') as file:
	reader = csv.reader(file)
	for row in reader:
		data.append(info(row[0], row[1], row[2]))
		
plt.xlabel('Names')
plt.ylabel('Numbers')
x = [data[0].name, data[1].name, data[2].name, data[3].name]
y = [data[0].number, data[1].number, data[2].number, data[3].number]

plt.plot(x,y)
plt.show()

		


