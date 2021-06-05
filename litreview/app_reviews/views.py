from django.shortcuts import redirect, render
from itertools import chain
from django.db.models import Value, CharField

from .forms import RawCreateReviewForm, RawCreateTicketForm
from .models import Review, Ticket
from .getposts import get_reviews_for_feed, get_tickets_for_feed

# Create your views here.
def ticket_create(request):

    if request.user.is_authenticated == False:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = RawCreateTicketForm(request.POST, request.FILES)
            if form.is_valid:
                Ticket.objects.create(
                    title= request.POST['title'],
                    description= request.POST['description'],
                    user= request.user,
                    image= request.FILES.get('image', 'image/upload/NULL.jpg')
                )
                return redirect('/')
        else:
            form = RawCreateTicketForm()

        context = {
            'form': form,
        }
        return render(request, 'createticket.html', context)



def ticket_modify(request, id):

    if request.user.is_authenticated == False:
        return redirect('login')
    else:

        ticket_modify = Ticket.objects.get(pk=id)

        if ticket_modify.user_id == request.user.id:
            if request.method == 'POST':
                form = RawCreateTicketForm(request.POST, request.FILES)
                if form.is_valid:
                    Ticket.objects.filter(pk=id).update(
                        title= request.POST['title'],
                        description= request.POST['description'],
                        image= request.FILES.get('image', ticket_modify.image)
                    )
                    return redirect('/')
            else:
                form = RawCreateTicketForm()

                form.fields['title'].initial = ticket_modify.title
                form.fields['description'].initial = ticket_modify.description
                form.fields['image'].initial = ticket_modify.image

            context = {
                'form': form,
                'ticket_infos': ticket_modify,
            }

            return render(request, 'modifyticket.html', context)
        else:
            return redirect('/')


def review_create(request):

    if request.user.is_authenticated == False:
        return redirect('login')
    else:
        if request.method == 'POST':
            form_review = RawCreateReviewForm(request.POST)
            form_ticket = RawCreateTicketForm(request.POST, request.FILES)
            if form_review.is_valid and form_ticket.is_valid:
                new_ticket = Ticket.objects.create(
                    title= request.POST['title'],
                    description= request.POST['description'],
                    user= request.user,
                    image= request.FILES.get('image', 'image/upload/NULL.jpg')
                )
                Review.objects.create(
                    headline= request.POST['headline'],
                    body= request.POST['body'],
                    user= request.user,
                    ticket= new_ticket,
                    rating= request.POST['rating'],
                )
            return redirect('/')

        else:
            form_review = RawCreateReviewForm()
            form_ticket = RawCreateTicketForm()

        context = {
            'form_review': form_review,
            'form_ticket': form_ticket,
        }

        return render(request, 'createreview.html', context)

def review_create_reply(request, id):

    if request.user.is_authenticated == False:
        return redirect('login')
    else:
        print(len(Review.objects.filter(ticket_id=id).filter(user_id=request.user.id)))
        if len(Review.objects.filter(ticket_id=id).filter(user_id=request.user.id)) >= 1:

            return redirect('/')

        else:

            old_ticket = Ticket.objects.get(id=id)

            if request.method == 'POST':
                form_review = RawCreateReviewForm(request.POST)
                form_ticket = RawCreateTicketForm(request.POST, request.FILES)
                if form_review.is_valid and form_ticket.is_valid:
                    Review.objects.create(
                        headline= request.POST['headline'],
                        body= request.POST['body'],
                        user= request.user,
                        ticket= old_ticket,
                        rating= request.POST['rating'],
                    )
                return redirect('/')
            else:
                form_review = RawCreateReviewForm()

            context = {
                'form_review': form_review,
                'infos_ticket': old_ticket,
            }
            return render(request, 'replycreatereview.html', context)


def review_modify(request, id):

    if request.user.is_authenticated == False:
        return redirect('login')
    else:
        review_modify = Review.objects.get(pk=id)

        if review_modify.user_id == request.user.id:
            if request.method == 'POST':
                form = RawCreateReviewForm(request.POST)
                if form.is_valid:
                    Review.objects.filter(pk=id).update(
                        headline= request.POST['headline'],
                        body= request.POST['body'],
                        rating= request.POST['rating'],
                    )
                    return redirect('/')
            else:
                form = RawCreateReviewForm()

                form.fields['headline'].initial = review_modify.headline
                form.fields['body'].initial = review_modify.body
                form.fields['rating'].initial = review_modify.rating

            context = {
                'form': form,
                'review_infos': review_modify,
            }
            return render(request, 'modifyreview.html', context)
        else:
            return redirect('/')


def posts(request):

    if request.user.is_authenticated == False:
        return redirect('login')
    else:

        reviews = Review.objects.filter(user_id=request.user.id)  
        reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

        tickets = Ticket.objects.filter(user_id=request.user.id) 
        tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

        posts = sorted(
            chain(reviews, tickets), 
            key=lambda post: post.time_created, 
            reverse=True
        )

        ticket_list_for_review = []
        for review in reviews:
            ticket_list_for_review.append(Ticket.objects.get(id=review.ticket_id))

        context = {
            'posts': posts,
            'ticket_list_for_review': ticket_list_for_review,
        }

        return render(request, 'posts.html', context)

def feed(request):
    
    if request.user.is_authenticated == False:
        return redirect('login')
    else:

        reviews = get_reviews_for_feed(request.user)
        reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

        tickets = get_tickets_for_feed(request.user) 
        tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

        posts = sorted(
            chain(reviews, tickets), 
            key=lambda post: post.time_created, 
            reverse=True
        )

        tlfr = []
        for review in reviews:
            tlfr.append(review.ticket_id)

        ticket_list_for_review= Ticket.objects.filter(id__in=tlfr)

        context = {
            'posts': posts,
            'ticket_list_for_review': ticket_list_for_review,
        }

        return render(request, 'feed.html', context)
