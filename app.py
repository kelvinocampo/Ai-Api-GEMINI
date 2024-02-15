import json
import google.generativeai as genai 

def obtener_api_key ():
    with open ('config.json', 'r') as f:
        config = json.load(f)
    return config['GOOGLE_API_KEY']

#Configuracion API KEY
GOOGLE_API_KEY = obtener_api_key()
genai.configure(api_key=GOOGLE_API_KEY)

#crear modelo
model = genai.GenerativeModel('gemini-pro')

#generar contenido
response = model.generate_content('¿Que es la vida?')

#imprimir
print(response.text)