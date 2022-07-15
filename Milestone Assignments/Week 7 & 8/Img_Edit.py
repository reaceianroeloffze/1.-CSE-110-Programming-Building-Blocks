from PIL import Image

img = Image.open('snowscape.jpg')

pix = img.load()

# print(pix[500, 400])
# print(pix[100, 300])
# print(pix[700, 200])
# print(pix[300, 500])
# print(pix[600, 100])
for y in range(200, 400):
    for x in range(100, 500):
        (r,g,b) = pix[x, y]
        pix[x, y] = (196, 250, b)
# pix[700, 100] = (0,255,0)
# pix[70, 50] = (0,0,255)
# pix[500, 80] = (0,255,255)
# pix[300, 200] = (255,0,255)
# pix[200, 100] = (255,0,0)
# pix[100, 100] = (255,255,0)

# img.show()
img.save('snowscape_edit.jpg')
