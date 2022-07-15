# --- Import Pillow Library ---
from PIL import Image

# --- Image Merging ---

# -- Space Shuttle and Earth --

# --- Load 2 images ---
img_earth = Image.open('earth.jpg')
img_spaceshuttle = Image.open('spaceshuttle.jpg')

# --- Create New Image in RGB Format ---
img_shuttleearth = Image.new('RGB', img_earth.size)

# --- Load Pixels for Each Image ---
pix_earth = img_earth.load()
pix_spaceshuttle = img_spaceshuttle.load()
pix_shuttleearth = img_shuttleearth.load()

# --- Merge 2 Images Using if/else Statement, Loops and RGB Values ---
for x in range(800):
    for y in range(600):
        (r,g,b) = pix_spaceshuttle[x,y]
        if g > 150 and r < 125 and b < 130:
            pix_shuttleearth[x,y] = pix_earth[x,y]
        else:
            pix_shuttleearth[x,y] = pix_spaceshuttle[x,y]

# --- Display New Image ---
img_shuttleearth.show()

# --- Save New Image ---
img_shuttleearth.save('Shuttle_Earth.jpg')

# -- Sunset and Boat --

# --- Load 2 images ---
img_sunset = Image.open('sunset.jpg')
img_boat = Image.open('boat.jpg')

# --- Create New Image in RGB Format ---
img_sunboat = Image.new('RGB', img_sunset.size)

# --- Load Pixels for Each Image ---
pix_sunset = img_sunset.load()
pix_boat = img_boat.load()
pix_sunboat = img_sunboat.load()

# --- Merge 2 Images Using if/else Statement, Loops and RGB Values ---
for x in range(800):
    for y in range(600):
        (r,g,b) = pix_boat[x,y]
        if g > 150 and r < 155 and b < 140:
            pix_sunboat[x,y] = pix_sunset[x,y]
        else:
            pix_sunboat[x,y] = pix_boat[x,y] 

# --- Display New Image ---
img_sunboat.show()

# --- Save New Image ---
img_sunboat.save('sunboat.jpg')

# -- My own Images from Unsplash --

# --- Load 2 images ---
img_blue = Image.open('adam-jicha-7AckmETIk54OS-unsplash.jpg')
img_red = Image.open('adam-jicha-fAaL7XBkqgQOS-unsplash.jpg')

# --- Create New Image in RGB Format ---
img_blue_red = Image.new('RGB', img_red.size)

# --- Load Pixels for Each Image ---
pix_blue = img_blue.load()
pix_red = img_red.load()
pix_blue_red = img_blue_red.load()

# --- Merge 2 Images Using if/else Statement, Loops and RGB Values ---
for x in range(2338):
    for y in range(3273):
        (r,g,b,) = pix_blue[x,y]
        if r < 250 and g < 250 and b > 185 :
            pix_blue_red[x,y] = pix_red[x,y]
        else:
            pix_blue_red[x,y] = pix_blue[x,y]

# --- Display New Image ---
img_blue_red.show()

# --- Save New Image ---
img_blue_red.save('3D_Edit.jpg')