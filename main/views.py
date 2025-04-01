from django.shortcuts import render
 
 # Create your views here.
def student(request):
     return render(request, 'student.html')

def FA(request):
     return render(request, 'FA.html')