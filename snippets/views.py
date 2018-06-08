from django.shortcuts import get_object_or_404
from django.http import Http404
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializer import SnippetSerializer
# Create your views here.


# @csrf_exempt
# @api_view(['GET', 'POST'])
# def snippet_list(request, format=None):
# class SnippetList(APIView):
#     '''List all code snippets, or create a new snippet.
#     '''
#     # if request.method == 'GET':
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         # return JsonResponse(serializer.data, safe=False)
#         return Response(serializer.data)
#
#     # if request.method == 'POST':
#     def post(self, request, format=None):
#         # data = JSONParser().parse(request)
#         # serializer = SnippetSerializer(data=data)
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             # return JsonResponse(serializer.data, status=201)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         # return JsonResponse(serializer.errors, status=400)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk, format=None):
# class SnippetDetail(APIView):
#     ''' Retreive, update or delete a code snippet.
#     '''
#     def get_object(self, pk):
#         snippet = get_object_or_404(Snippet, pk=pk)
#         return snippet
#
#     # if request.method == 'GET':
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         # return JsonResponse(serializer.data)
#         return Response(serializer.data)
#
#     # elif request.method == 'PUT':
#     def put(self, request, pk, format=None):
#         # data = JSONParser().parse(request)
#         # serializer = SnippetSerializer(snippet, data=data)
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#
#     # elif request.method == 'DELETE':
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         # return HttpResponse(status=204)
#         return Response(status=status.HTTP_204_NO_CONTENT)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
