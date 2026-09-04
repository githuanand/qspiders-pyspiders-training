from django.shortcuts import render

# Create your views here.

data=[
        {
            'id': 1,
            'title':'Article 1',
            'desc':'This is the description for article 1.',
        },

        {
            'id': 2,
            'title':'Article 2',
            'desc':'This is the description for article 2.',
        },

        {
            'id': 3,
            'title':'Article 3',
            'desc':'This is the description for article 3.',
        },

        {
            'id': 4,
            'title':'Article 4',
            'desc':'This is the description for article 4.',
        },
    ]
def home(request):
    return render(request, 'home.html', context={'articles': data})

def read(request, id):
    article = next((item for item in data if item['id'] == id), None)
    return render(request, 'read.html', context={'article': article})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')
