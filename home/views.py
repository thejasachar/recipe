from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    peoples = [
    {'Name': 'thejas', 'age': 11},
    {'Name': 'pradyumna', 'age': 20},
    {'Name': 'fida', 'age': 20},
    {'Name': 'kishore', 'age': 15},
    {'Name': 'naga', 'age': 20},
    {'Name': 'suraj', 'age': 21},
    {'Name': 'yashwanth', 'age': 23},
    {'Name': 'bharath', 'age': 30},
    {'Name': 'sujjal', 'age': 19},
    {'Name': 'sangya', 'age': 17},
    {'Name': 'chinmay', 'age': 16},
    {'Name': "vaigyanathn",'age':1},
]

    return render(request ,"home\index.html",{'page':'Django tutorial','peoples':peoples})
def about(request):
    context = {'page':'About'}
    return render(request ,"home/about.html",context)

def contact(request):
    context = {'page':'contact'}
    return render(request ,"home/contact.html",context)

def success_page(request):
    print("*" *10)
    return HttpResponse("<h1>This is success page</h1>")