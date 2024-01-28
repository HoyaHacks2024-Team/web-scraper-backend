from django.shortcuts import render
from django.http import JsonResponse



def return_data(request):
    
    
    return JsonResponse({"message": "context"})
