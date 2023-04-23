# from pdf2image import convert_from_path
# import easyocr
# import numpy as np
# import PIL
# from PIL import ImageDraw
# import spacy
# from IPython.display import display, Image
# reader = easyocr.Reader(['en'])

# images = convert_from_path("Files/EC030BIL6000400_EIP Bill Summary.pdf")
# display(images[0])

# from pdf2image import convert_from_path
# images = convert_from_path('Files/EC030BIL6000327_Invoice.pdf')  # Store Pdf with convert_from_path function

# for i in range(len(images)):
# 	images[i].save('image1'+ str(i) +'.jpg', 'JPEG')  # Save pages as images in the pdf


# import cv2
# import pytesseract
# img = cv2.imread('image0.jpg')	
# img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# print(pytesseract.image_to_string(img))
# cv2.imshow('Result',img)
# cv2.waitKey(0)

# from PIL import Image

# img1 = Image.open ('image0.jpg')
# img1.show ()

# from PIL import Image
# from pytesseract import pytesseract
# img = Image. open('image10.jpg')
# text = pytesseract. image_to_string(img)
# print(text)
