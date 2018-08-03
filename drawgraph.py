from PIL import Image, ImageDraw
img = Image.open('C:/Users/sriordan/Desktop/blank.png')
draw_img = ImageDraw.Draw(img)

def drawChart(rows, cols):
	y=0
	x=0
	for i in range(rows):
		y = y + 100
		draw_img.line((0,y,rows*100,y), width=5, fill=(0,0,0,0))
	for i in range(cols):
		x = x + 100
		draw_img.line((x,0,x,cols*100), width=5, fill=(0,0,0,0))
		
drawChart(5,5)

data1 = ['10','20','30','40','50']
data2 = ['60','70','80','90','100']
data3 = ['110','120','130','140','150']
data4 = ['160','170','180','190','200']
data5 = ['210','220','230','240','250']

def fillRow(data, y):
	x = 50
	for i in range(len(data)):
		draw_img.text((x, y), data[i], fill=(0,0,0))
		x = x + 100

fillRow(data1,50)
fillRow(data2,150)
fillRow(data3,250)
fillRow(data4,350)
fillRow(data5,450)
	
img.show()



		