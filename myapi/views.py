from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse, response
from myapi.models import Book
from django.views import View

# Create your views here.
#get method for the api
class MyAPIView(APIView):
    def get(self, request):
        data = {'message': 'Welcome to my First API!'}
        return Response(data)

#post meethod for the api
class BookCreateView(APIView):
    def post(self, request):
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_date = request.POST.get('publication_date')

        book = Book.objects.create(
            title=title,
            author=author,
            publication_date=publication_date
        )
        return JsonResponse({'message': 'Book created successfully'})
