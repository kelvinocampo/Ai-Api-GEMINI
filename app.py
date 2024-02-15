import json
import google.generativeai as genai 
import PIL.Image
import flet as ft


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

#crea la interfaz
def main(page : ft.Page):
    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Por favor ingrese un elemento a buscar"
            page.update()
        else:
            value = txt_name.value
            response(value)

    txt_name = ft.TextField(label="Ingresa el elemento que desea buscar dentro de la imagen")

    page.add(txt_name, ft.ElevatedButton("buscar elemento!", on_click=btn_click))

def response(quest):
    #generar contenido
    response = model.generate_content([quest, img])
    response.resolve()

    #imprimir
    t = ft.Text(value=response.text, color="green")


#inicializa la interfaz
ft.app(target=main)

