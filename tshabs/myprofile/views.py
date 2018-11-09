from django.shortcuts import render

def home(request):
    temp_path = 'myprofile/home.html'
    temp_dict = {'title': home}
    return render(request, temp_path, temp_dict)
