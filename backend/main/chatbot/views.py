from django.shortcuts import render

# Create your views here.

def chatbot(request):
    return render(request, "chat/chatbot.html")