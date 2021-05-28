from django.shortcuts import render

# Create your views here.
def ticket_create(request):
    return render(request, 'createticket.html')

def ticket_modify(request):
    return render(request, 'modifyticket.html')

def review_create(request):
    return render(request, 'createreview.html')

def review_modify(request):
    return render(request, 'modifyreview.html')

def posts(request):
    return render(request, 'posts.html')

def flux(request):

    tickets = [
        {'id': 1, 'title': 'Titre du livre 1', 'body': 'Description 1'},
        {'id': 2, 'title': 'Titre du livre 2', 'body': 'Description 2'},
        {'id': 3, 'title': 'Titre du livre 3', 'body': 'Description 3'},
    ]

    return render(request, 'flux.html', {'tickets': tickets})
    