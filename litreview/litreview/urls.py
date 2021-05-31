"""litreview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path

from . import views
from app_accounts import views as v_acc
from app_reviews import views as v_rev
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', LoginView.as_view(template_name='login.html', redirect_authenticated_user = True), name='login'),
    path('register/', v_acc.register, name='register'),
    path('account/', v_acc.account, name='account'),

    path('ticket/create/', v_rev.ticket_create, name='create_ticket'),
    path('ticket/modify/', v_rev.ticket_modify, name='modify_ticket'),
    path('review/create/', v_rev.review_create, name='create_review'),
    path('review/modify/', v_rev.review_modify, name='modify_review'),
    path('flux/', v_rev.flux, name="flux"),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns