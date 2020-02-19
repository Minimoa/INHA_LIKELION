from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

<<<<<<< HEAD

def detail(request):
    return render(request,'detail.html')
=======
def new(request):
    return render(request, 'new.html')
>>>>>>> 3aa4d6c79fee01d74301f5a04f2e361392a36805
