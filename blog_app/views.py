from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from .serializer import BlogSerializer, CategorySerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Blog, Category

# GET, POST
class AllBlogView(APIView):
    def get(self, request=Request):
        blog = Blog.objects.filter(is_public=True)
        serializer = BlogSerializer(blog, many=True)
        response = {
            "messsage": "all blogs",
            "data": serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)
    
    def post(self, request=Request):
        data = request.data
        serializer = BlogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "successful"
            }
            return Response(data=response, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET, PUT, DELETE
class BlogDetailView(APIView):
    # get a single post
    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        serializer = BlogSerializer(blog)
        response = {
            "data": serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)
    
    # Delete request
    def put(self, request, pk):
        blog = Blog.objects.get(pk=pk) # instance of the data
        data = request.data # the new edited data
        serializer = BlogSerializer(instance=blog, data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
            "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    # delete
    def delete(self, request, pk):
        post = Blog.objects.all(pk=pk)
        post.delete()
        return Response(status=status.HTTP_200_OK)
    
class CategoryListView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        response = {
            "message": "all category",
            "data": serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)
    
class CategoryDetailView(APIView):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category)
        response = {
            "message": "categoory_detail",
            "data": serializer.data,
        }
        return Response(data=response, status=status.HTTP_200_OK)