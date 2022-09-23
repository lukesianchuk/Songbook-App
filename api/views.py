from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from songs.models import Song
from api.serializers import SongSerializer

from rest_framework import serializers
from rest_framework import status
  
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
  
    return Response(api_urls)


