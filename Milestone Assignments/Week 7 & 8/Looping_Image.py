from PIL import Image
from pathlib import Path
# Obtaining exact location of current .py file
folder = (Path(__file__).resolve().parent) # Parent removes .py from current location & returns as variable value

# This line opens the image and loads it into a variable called "image_original"
image_original = Image.open(f'{folder}\\earth.jpg')

# This line attempts to open a new window to display the image.
image_original.show()

# https://stackoverflow.com/questions/7162366/get-location-of-the-py-source-file