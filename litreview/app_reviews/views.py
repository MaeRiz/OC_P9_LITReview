from django.shortcuts import redirect, render

from .forms import CreateTicketForm
from .models import Ticket

# Create your views here.
def ticket_create(request):

    if request.method == 'POST':
        form = CreateTicketForm(request.POST, request.FILES)
        if form.is_valid:
            Ticket.objects.create(
                headline= request.POST['headline'],
                body= request.POST['body'],
                user= request.user,
                image= request.FILES.get('image', 'image/upload/NULL.jpg')
            )

            return redirect('flux')
    else:
        form = CreateTicketForm()

    return render(request, 'createticket.html', {'form': form})




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
    