from django.shortcuts import render

from django.http import JsonResponse
from initiate_scraping.utils.langchain import finalize_text
from initiate_scraping.utils.get_url import get_university_website
from store_data.views import store_data

from initiate_scraping.utils.llama import create_vector_embedding


def initiate_scraping(request):
    uni_name = request.GET.get('name')
    uni_site = get_university_website(uni_name)
    context = finalize_text(uni_site)

    # prep data
    vectorized_context = create_vector_embedding(context)
    data_to_store = {uni_name: vectorized_context}

    # store to mongodb
    store_data(data_to_store)

    # return to other api
    
    
    return JsonResponse({uni_name: context}, safe=False)
