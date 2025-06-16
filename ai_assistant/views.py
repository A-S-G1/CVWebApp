# myproject/ai_assistant/views.py
import os
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI
from django.conf import settings # IMPORTANT: Import settings here to access OPENAI_API_KEY

# Print the API key value (first 5 and last 5 chars) to your Django server console
# when the view module is accessed. Useful for debugging API key loading.
print(f"DEBUG: API Key value in views.py: {settings.OPENAI_API_KEY[:5]}...{settings.OPENAI_API_KEY[-5:] if settings.OPENAI_API_KEY else 'N/A'}")

# Initialize OpenAI client using the key from settings.
# This should be done once at the module level to avoid re-initializing on every request.
try:
    client = OpenAI(api_key=settings.OPENAI_API_KEY)
    print("DEBUG: OpenAI client initialized successfully.")
except Exception as e:
    print(f"DEBUG: Error initializing OpenAI client: {e}")
    client = None # Set client to None if initialization fails

@csrf_exempt # Disables CSRF protection for this view (useful for API endpoints if not using Django forms)
def chat_with_assistant(request):
    # If the OpenAI client failed to initialize, return a server error immediately
    if client is None:
        return JsonResponse({'error': 'AI assistant is not configured correctly on the server. Please check API key.'}, status=500)

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message')
            current_page_info = data.get('currentPage') # Information about the current page from frontend

            if not user_message:
                return JsonResponse({'error': 'No message provided'}, status=400)

            # --- AI Model Interaction Logic ---
            # This prompt guides the AI on its persona and task
            prompt = f"""
            You are a friendly and helpful cartoon hero AI assistant for Anton Georgiiev's personal portfolio website.
            Your purpose is to explain the current page to the user and suggest other interesting pages they might want to visit.
            Always maintain a cheerful and heroic persona.
            
            The current page the user is viewing is: "{current_page_info}".

            Here are the pages on Anton's website and their purposes:
            - "About Me": This page introduces Anton, his background, bio, contact information, and languages.
            - "Experience": Details Anton's professional work history, roles, and responsibilities.
            - "Skills": Lists Anton's core, technical, and professional skills in various categories.
            - "Projects": Showcases Anton's test applications and coding projects, highlighting his practical work.
            - "Blog": This is Anton's blog, where he shares articles, insights, and updates on various topics.
            - "Contact": This page allows users to send Anton general feedback about the website or submit work offers.
            - "Tech Specs": Provides detailed specifications about the languages and technologies used to build this web app.

            Based on the user's message and the current page, explain the page's purpose clearly and then
            recommend other relevant pages to visit from the list above. Keep your responses concise,
            helpful, and in character as a cartoon hero!
            """

            # Call to the OpenAI API for chat completion
            chat_completion = client.chat.completions.create(
                model="gpt-3.5-turbo", # You can use "gpt-4" for more advanced capabilities, but it might cost more
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": user_message}
                ]
            )

            assistant_response = chat_completion.choices[0].message.content

            return JsonResponse({'response': assistant_response})

        except json.JSONDecodeError:
            # Handle cases where the request body is not valid JSON
            return JsonResponse({'error': 'Invalid JSON in request body.'}, status=400)
        except Exception as e:
            # Catch all other exceptions, including OpenAI API errors
            print(f"DEBUG: Error during chat completion: {e}") # Print the full error for debugging
            # Return a generic error message to the frontend for security
            return JsonResponse({'error': f'An unexpected error occurred: {e}.'}, status=500)
    
    # Return error for methods other than POST
    return JsonResponse({'error': 'Invalid request method. Only POST allowed.'}, status=405)
