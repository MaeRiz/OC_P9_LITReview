from .models import UserFollows
from .forms import FollowUser
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError

def home(request):

    if request.method == 'POST':
        form = FollowUser(request.POST)
        if form.is_valid:
            if request.user == User.objects.get(username=request.POST['followed_user']):
                messages.error(request, 'Vous ne pouvez pas vous ajouter vous même.')
            else:
                try:
                    UserFollows.objects.create(
                        user = request.user,
                        followed_user = User.objects.get(username=request.POST['followed_user']),
                    )
                except IntegrityError:
                    messages.error(request, 'Vous avez déjà ajouter cet utilisateur.')

    else:
        form = FollowUser()

    following_list = []
    followers_list = []

    for f in UserFollows.objects.filter(user_id=request.user):
        following_list.append(User.objects.get(id=f.followed_user_id))

    for f in UserFollows.objects.filter(followed_user_id=request.user):
        followers_list.append(User.objects.get(id=f.user_id))

    context= {
        'form': form,
        'following': following_list,
        'followers': followers_list,
    }

    return render(request, 'subs.html', context)

def unsubscribe(request, id):
    UserFollows.objects.filter(user_id=request.user).filter(followed_user_id=id).delete()
    return redirect('subs')