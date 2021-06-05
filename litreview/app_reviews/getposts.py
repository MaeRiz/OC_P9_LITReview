
from django.db.models.fields import FloatField
from .models import Review, Ticket
from  app_subs.models import UserFollows
from itertools import chain


def get_reviews_for_feed(userid):
    followers = UserFollows.objects.filter(user_id=userid)
    followers_ids = [userid.id]
    for follower in followers:
        followers_ids.append(follower.followed_user_id)

    self_tickets = Ticket.objects.filter(user_id=userid)
    for self_ticket in self_tickets:
        reply_reviews = Review.objects.filter(ticket_id=self_ticket.id)
        for reply_review in reply_reviews:
            followers_ids.append(reply_review.id)

    return (Review.objects.filter(user_id__in=followers_ids).distinct())


def get_tickets_for_feed(userid):
    followers = UserFollows.objects.filter(user_id=userid)
    followers_ids = [userid.id]
    for follower in followers:
        followers_ids.append(follower.followed_user_id)
    return (Ticket.objects.filter(user_id__in=followers_ids))