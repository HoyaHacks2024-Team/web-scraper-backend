from django.shortcuts import render

from django.http import JsonResponse
from .scraping import perform_scraping  # Import your scraping function

def initiate_scraping(request):
    if request.method == 'POST':
        # Call the function to perform scraping and get embeddings
        embeddings = perform_scraping()
        return JsonResponse({"embeddings": embeddings})
