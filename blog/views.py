from django.shortcuts import render
#from django.http import JsonResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def blog(request):
    return render(request,'blog.html', {})


# __________________________________________this is demo test 
#def chatbot_response(request):
 #   user_message = request.GET.get("message", "")
    
    # Simple rule-based chatbot
  #  responses = {
   #     "hi": "Hello! How can I help you?",
    #    "bye": "Goodbye!",
     #   "help": "I can answer simple questions. Try typing 'hi'."
    #}
    
    #reply = responses.get(user_message.lower(), "Sorry, I don’t understand that.")
    #return JsonResponse({"response": reply})
#http://127.0.0.1:8000/blog/chatbot/?message=hi


@csrf_exempt
def chatbot_response(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "")

        # Very simple logic for now
        if "hello" in user_message.lower():
            bot_response = "Hi there! How can I help you today?"
        elif "bye" in user_message.lower():
            bot_response = "Goodbye! Have a nice day 😊"
        else:
            bot_response = "Sorry, I don't understand that."

        return JsonResponse({"response": bot_response})

def chat_page(request):
    return render(request, "chat.html")
