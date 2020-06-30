import pytesseract
from PIL import Image
image_to_string:pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR'

#English is by default language either we specify or not it dosent matter.for other languages we have to specify like french, spanish.
im = Image.open("1.jpg")

text = pytesseract.image_to_string(im, lang = 'eng')

print(text)