import pytesseract
from PIL import Image

# Accepts an input image file path from the user.
image_file_path = input("C:\\Users\\AMAZON BOX\\Desktop\\pp\\2018.jpg ")


# Utilizes pytesseract to extract text from the image.
extracted_text = pytesseract.image_to_string(Image.open(image_file_path))

# Outputs the extracted text to the console.
print(extracted_text)
