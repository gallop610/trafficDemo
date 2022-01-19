from django.shortcuts import render

# Create your views here.
def basic_test(request):
    return render(request, 'basic_test.html')