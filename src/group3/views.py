from django.shortcuts import render
from .models import TextOptimization
from .logic import process_input
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializer import toJson
from .database import query,secret

# Create your views here.

def home(request):
    return render (request , 'group3.html' , {'group_number': '3'})



class TextMistakesAPIView(APIView):
    def post(self, request):
        input_text = request.data.get('text', '')
        if not input_text:
            return Response({"error": "No text provided"}, status=status.HTTP_400_BAD_REQUEST)

        # Call your backend logic to process the text
        mistakes = process_text(input_text)  # Replace with your logic function

        return Response({"suggestions": mistakes}, status=status.HTTP_200_OK)

# Replace this with your actual text processing logic
def process_text(text):
    # Example: Find dummy mistakes in the text
    return [{"start":0, "end": 5, "suggest": "سلام"}]


def optimize_text(request):
    if request.method == 'POST':
        input_text = request.POST.get('text')
        optimized_text = process_input(input_text)
        return render(request, 'group3/result.html', {'optimized_text': optimized_text})

    return render(request, 'group3/optimize.html')


@api_view(['POST'])
def post_text(request):
    if request.method == 'POST':
        input_text = request.POST.get('text')
        optimized_text = process_input(input_text)
        return toJson(optimized_text)
    
mydb = query.create_db_connection(secret.DB_HOST, secret.DB_PORT, secret.DB_USER, secret.DB_PASSWORD, secret.DB_NAME)
query.save_texts(mydb, )

