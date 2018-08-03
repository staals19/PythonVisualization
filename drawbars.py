from PIL import Image, ImageDraw, ImageFont
img = Image.open('C:/Users/sriordan/Desktop/blank.png')
draw_img = ImageDraw.Draw(img)
 
data = ['10','20','30','40','50']
labels = ["ten", "twenty", "thirty", "fourty", "fifty"]

def drawBars(start):
	x = 0
	y = 0
	for i in data:
		x = x + 100
		y = start - int(i)*5
		draw_img.line((x,start,x,y), width = 50, fill=(0,0,0))


def drawLabels(start):
	x = 0	
	for i in range(len(labels)):
		if(len(labels[i]) < 5):
			x = x + 80
		else:
			x = x + 100
		draw_img.text((x,start), labels[i], fill=(0,0,0))
		
drawBars(600)
drawLabels(600)
img.show()


