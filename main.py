from google import generativeai as genai
from config import API_KEY

client = genai.configure(api_key = API_KEY)

print('🤖simple-AI-chatbot--------')

def get_response():
    while True:
        user_input = input('You: ')
        if user_input.lower() in ["quit","exit","bye"]:
            print('\n 🤖 Chat bot: Goodbye!')
            break
            response = client.models.generate_content_stream(),
            model = 'gemini-3.5-flash',
            message = [
                {"role":"system","content":"you are helpful chatbot"},
                {"role":"user","content":user_input}
            ],
            contents = True
            )
            return response.text
     
