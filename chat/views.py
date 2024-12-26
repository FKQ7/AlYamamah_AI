#from thefuzz import fuzz
from django.shortcuts import render
from django.http import JsonResponse
from openai import OpenAI
import logging
import os
from dotenv import load_dotenv
load_dotenv()
# Set your OpenAI API key securely
api_key=os.getenv("API_KEY")
# Set up logging for better debugging and monitoring
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
common_questions = {
    "what is your name?": "My name is Gemini.",
    "how are you?": "I am doing well, thank you.",
    "what can you do?": "I can help you with various tasks, such as answering questions regarding the uni, such as Events, News, and Announcements.",}

def ask_openai(message):    
    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "DO NOT ANSWER ANY QUESTION THAT IS NOT RELATED TO THE UNIVERSITY. You can answer simple questions like 'How are you?' but not coding or math questions."},
            {
            "role": "assistant",
                "content": (
                    "You are a university assistant. Your role is to help users navigate the campus and understand the building structure. "
                    "The university campus consists of:\n"
                    "- Two gyms: one for men and one for women.\n"
                    "  - The men's gym is in the left side of the campus, in the first building.\n"
                    "  - The women's gym is in the left side of the campus, in the second building.\n"
                    "- The main building is the only building for classes. It has five floors, including the ground floor. "
                    "Classrooms are labeled as follows:\n"
                    "- 'A' indicates the right side of the main building.\n"
                    "- 'B' indicates the left side of the main building.\n"
                    "- Class numbers are formatted as (LETTER)-(FLOOR MINUS ONE FLOOR)(CLASS NUMBER). For example:\n"
                    "  - A-24: Right side, 1st floor, classroom 4.\n"
                    "  - B-11: Left side, ground floor, classroom 1.\n"
                    "  - A-54: This does not exist because the building has only five floors.\n"
                    "- The big auditorium is located on the right side of the campus, in the first big building.\n"
                    "To determine the floor:\n"
                    "   - The number immediately after the letter indicates the floor (1 = ground floor, 2 = 1st floor, etc.).\n"
                    "   - The last digit indicates the classroom on that floor.\n"
                    "Provide clear and concise directions based on this information."
                ) 
            },
            {"role": "user", "content": message}
        ]
    )
    return completion.choices[0].message.content

def chat(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chat/chatbot.html')