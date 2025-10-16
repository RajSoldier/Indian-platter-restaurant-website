from django.urls import path
from . import views
from .views import reservation_view
from django.conf import settings

urlpatterns = [ 
    path("", views.index, name='index'),
    path("about/", views.about, name='about'),
    path("starter/", views.starter, name='starter'),
    path("maincourse/", views.maincourse, name='maincourse'),
    path("deserts/", views.deserts, name='deserts'),
    path("drinks/", views.drinks, name='drinks'),
    path("reservation/", views.reservation_view, name='reservation'),
    path('our_chefs/', views.our_chefs, name='our_chefs'),
     path('book-ticket/<int:event_id>/', views.book_ticket, name='book_ticket'),
    
]


