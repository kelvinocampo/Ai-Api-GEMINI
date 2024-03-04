import google.generativeai as genai

genai.configure(api_key='AIzaSyALn5MDkG4cApNZ9bLRdFtPCoF0v5nleFY')

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("Who is the Albert Einstein")

print(response.text)