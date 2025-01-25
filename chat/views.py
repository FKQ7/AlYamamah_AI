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
    # File path to JSON data
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "uni.json")

    # Load the JSON content
    with open(file_path, "r", encoding="utf-8") as file:
        assistant_content = json.load(file)

    # Extract key sections
    introduction = assistant_content.get("introduction", "No introduction available.")
    layout = assistant_content.get("layout", {})
    events_and_news = assistant_content.get("events_and_news", {})
    question_and_answer = assistant_content.get("question_and_answer", {})
    
    # Build layout context
    layout_context = []
    for section, details in layout.items():
        if isinstance(details, dict):
            layout_context.append(f"{section.capitalize()}:")
            for key, value in details.items():
                layout_context.append(f"  - {key.capitalize()}: {value}")
        elif isinstance(details, list):
            layout_context.append(f"{section.capitalize()}:")
            for item in details:
                if isinstance(item, dict):
                    for key, value in item.items():
                        layout_context.append(f"  - {key.capitalize()}: {value}")
        else:
            layout_context.append(f"{section.capitalize()}: {details}")
    layout_context = "\n".join(layout_context)

    # Build events context
    events_context = []
    upcoming_events = events_and_news.get("upcoming_events", [])
    for event in upcoming_events:
        events_context.append(f"{event['title']} on {event['date']} till {event['till_date']} at {event['location']}")
    events_context = "\n".join(events_context) if events_context else "No upcoming events available."

    # Build FAQ context
    faqs = question_and_answer.get("questions_and_answers", [])
    faq_context = "\n".join([f"Q: {qa['question']}\nA: {qa['answer']}" for qa in faqs]) if faqs else "No FAQs available."

    # Combine all into the assistant's message
    assistant_message = (
        f"You are a virtual assistant for the university. Your role is to guide users within the campus.\n\n"
        f"Introduction:\n{introduction}\n\n"
        f"Layout Information:\n{layout_context}\n\n"
        f"Upcoming Events:\n{events_context}\n\n"
        f"Frequently Asked Questions:\n{faq_context}\n\n"
        f"Now, please answer the following query:"
    )

    # Make the OpenAI API request
    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "DO NOT ANSWER ANY QUESTION THAT IS NOT RELATED TO THE UNIVERSITY. You can answer simple questions like 'How are you?' but not coding or math questions."},
            {"role": "assistant", "content": assistant_message},
            {"role": "user", "content": message}
        ]
    )
    return completion.choices[0].message.content


def chat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chat/chat.html')
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def inform(request):
    if request.method == 'POST':
        q = request.POST.get('question')
        a = request.POST.get('answer')
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "uni.json")
        with open(file_path, 'r',encoding='utf-8') as file:
            data = json.load(file)

        new_qa = {
            "question": q,
            "answer": a
        }
        print(new_qa)
        data['question_and_answer']['questions_and_answers'].append(new_qa)

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        return render(request, 'chat/inform.html', {'success': 'تم اضافة السؤال بنجاح'})

    return render(request, 'chat/inform.html')