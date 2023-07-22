from django.http import JsonResponse

# Create your views here.


def home(request):
    return JsonResponse({'message': 'Hello from Django Store REST API!'})


def stores(request):
    return JsonResponse({'id': 1})