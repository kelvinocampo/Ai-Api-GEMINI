import json
import google.generativeai as genai 
import PIL.Image
import flet as ft

#crea la interfaz
def main(page : ft.Page):
    pass
    
#inicializa la interfaz
ft.app(target=main)

def obtener_api_key ():
    with open ('config.json', 'r') as f:
        config = json.load(f)
    return config['GOOGLE_API_KEY']

#Configuracion API KEY
GOOGLE_API_KEY = obtener_api_key()
genai.configure(api_key=GOOGLE_API_KEY)

#identifica la imagen
img = PIL.Image.open('image.jpg')

#crear modelo
model = genai.GenerativeModel('gemini-pro-vision')

#generar contenido
response = model.generate_content(["Write a short, engaging blog post based on this picture. It should include a description of the meal in the photo and talk about my journey meal prepping.", img])
response.resolve()

#imprimir
print(response.text)
