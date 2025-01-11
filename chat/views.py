#from thefuzz import fuzz
from django.shortcuts import render
from django.http import JsonResponse
from openai import OpenAI
import logging
import os
import json
from dotenv import load_dotenv
load_dotenv()
# Set your OpenAI API key securely

# Set up logging for better debugging and monitoring
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import json
from openai import OpenAI

api_key=os.getenv("API_KEY")

def ask_openai(message):
    # Load assistant content from uni.json
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "uni.json")

    with open(file_path, "r") as file:
        assistant_content = json.load(file)
    assistant_content = json.dumps(assistant_content)
    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "DO NOT ANSWER ANY QUESTION THAT IS NOT RELATED TO THE UNIVERSITY. You can answer simple questions like 'How are you?' but not coding or math questions."},
            {"role": "assistant", "content": assistant_content},
            {"role": "user", "content": message}
        ]
    )
    return completion.choices[0].message.content


def chat(request):
    if request.method == 'POST':
        data = json.loads(request.body)  # Parse the incoming JSON data
        message = data.get('message')
        response = ask_openai(message)  # Call your OpenAI function
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chat/chat.html')