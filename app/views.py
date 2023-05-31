from django.shortcuts import render

# Create your views here.
def condition(request):
    d = {'a':100,'b':60,'c':110}
    return render(request,'condition.html',d)
