from . import views
from django.urls import path, re_path, include

userpatterns = [
    re_path(r'orders', views.user_orders, name='user_orders')
]

app_name = 'agency'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signin/', views.SignInView.as_view(), name='signin'),
    path('signout/', views.SignOutView.as_view(), name='signout'),
    path('company/', views.CompanyView.as_view(), name='company'),
    path('news/', views.NewsView.as_view(), name='news'),
    path('faq/', views.FAQView.as_view(), name='faq'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('polytics/', views.polytics, name='polytics'),
    path('vacancies/', views.VacanciesView.as_view(), name='vacancies'),
    path('reviews/', views.reviews, name='reviews'),
    path('create_review/', views.CreateReviewView.as_view(), name='create_review'),
    path('promocodes/', views.promocodes, name='promocodes'),
    path('hotels/', views.hotels, name='hotels'),
    path('trips/', views.trips, name='trips'),
    path('countries/', views.countries, name='countries'),
    path('users/', views.users, name='users'),
    path('orders/', views.orders, name='orders'),
    path('users_admin/', views.users_admin, name='users_admin'),
    path('api/', views.api, name='api'),
    path('diagram/', views.diagram, name='diagram'),
    path('stats/', views.stats, name='stats'),
    re_path(r'trip/(?P<pk>\d+)/buy/$', views.BuyTripsView.as_view(), name='buy_trip'),
    re_path(r'user/(?P<pk>\d+)/', include(userpatterns)),
    re_path(r'review/(?P<pk>\d+)/edit/$', views.EditReviewView.as_view(), name='edit_review'),
    re_path(r'review/(?P<pk>\d+)/delete/$', views.delete_review, name='delete_review')
]