import google.generativeai as genai
from PIL import Image

genai.configure(api_key='AIzaSyALn5MDkG4cApNZ9bLRdFtPCoF0v5nleFY')

img = Image.open('./image.jpg')

model = genai.GenerativeModel('gemini-pro-vision')

response = model.generate_content(["Hay un mango?, responde si o no", img])
response.resolve()

print(response.text)
