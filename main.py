import re
import csv

from PIL import Image
import pytesseract


# Simple image to string
IMAGE_STR = pytesseract.image_to_string(Image.open("test.png"))
IMAGE_STR = IMAGE_STR.lower()
names = []

with open("names.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        names.append((row[0].lower(), row[1].lower()))

for name in names:
    if re.search(f"{name[0]} {name[1]}", IMAGE_STR) is None:
        print(f"Didn't find {name[0]} {name[1]}")
