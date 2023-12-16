import json
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Book
from .forms import BookForm

class BookApi:

    def __init__(self, request, pk=None):
        self.request = request
        self.version = getattr(request, 'version', '1.0')
        self.pk = pk

    def to_json(self, objects):
        # depending on the version used and whether if we would have differences between versions
        # in serializing the objects we can add a check on the version here
        if isinstance(objects, Book):
            return serializers.serialize('json', [objects], fields=Book.get_json_attrs())[1:-1]
        return serializers.serialize('json', objects, fields=Book.get_json_attrs())

    def get(self):
        # depending on the version used and whether if we would have differences between versions
        # in handling get requests the objects we can add a check on the version here
        if self.pk:
            book_or_books = get_object_or_404(Book, pk=self.pk)
        else:
            book_or_books = Book.objects.all()

        return HttpResponse(self.to_json(book_or_books), status=200)
    
    def post(self):
        # depending on the version used and whether if we would have differences between versions
        # in handling post requests the objects we can add a check on the version here
        form = BookForm(json.loads(self.request.body))
        if form.is_valid():
            book = form.save()

            return HttpResponse(self.to_json(book), status=201)
        return HttpResponse(json.dumps(dict(form.errors)), status=400)
    
    def put(self):
        # depending on the version used and whether if we would have differences between versions
        # in handling put requests the objects we can add a check on the version here
        book = get_object_or_404(Book, pk=self.pk or None)
        form = BookForm(json.loads(self.request.body), instance=book)
        if form.is_valid():
            book = form.save()
            return HttpResponse(self.to_json(book), status=200)
        return HttpResponse(json.dumps(dict(form.errors)), status=400)
    
    def delete(self):
        # depending on the version used and whether if we would have differences between versions
        # in handling delete requests the objects we can add a check on the version here
        book = get_object_or_404(Book, pk=self.pk)
        book.delete()
        return HttpResponse({"message": "Book successfuly deleted"}, status=200)
    
    def handle_request(self):
        request_methods_handler = {
            'POST': self.post,
            'GET': self.get,
            'PUT': self.put,
            'DELETE': self.delete
        }
        return request_methods_handler.get(self.request.method, lambda: HttpResponse({"error": "Method not allowed"}, status=401))()
         

@csrf_exempt
def books(request, pk):

    api = BookApi(request, pk)
    return api.handle_request()
