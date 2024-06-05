from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden
from django.shortcuts import render, redirect
from .forms import * 
from .models import *

from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.models import auth
from django.contrib.auth.views import LoginView
from django.views.generic import *
from django.utils import timezone

from statistics import median, mean

import logging
import requests
import plotly.graph_objs as go

logging.basicConfig(
    level=logging.INFO, filename='logging.log', filemode='a', format='%(asctime)s %(levelname)s %(message)s')

# Create your views here.
class SignUpView(CreateView):
    form_class = AgencyUserCreationForm
    success_url = reverse_lazy('agency:home')
    template_name = 'signup.html'

def home(request):
    latest = PieceOfNews.objects.latest('added')
    return render(request, 'home.html', { 'latest': latest, 'localtime': timezone.localtime })

class CompanyView(TemplateView):
    template_name = 'company.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company = Company.objects.first()
        context['company'] = company
        return context
    
class NewsView(TemplateView):
    template_name = 'news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news = PieceOfNews.objects.all()
        context['news'] = news
        return context

class FAQView(TemplateView):
    template_name = 'faq.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        faq = FAQ.objects.all()
        context['faq'] = faq
        return context
    
class ContactsView(TemplateView):
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contacts = Contact.objects.all()
        context['contacts'] = contacts
        return context
    
def polytics(request):
    return render(request, 'polytics.html', {})
    
class VacanciesView(TemplateView):
    template_name = 'vacancies.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vacancies = Vacancy.objects.all()
        context['vacancies'] = vacancies
        return context
    
def reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews.html', {'reviews': reviews})
    
class CreateReviewView(View):
    template_name = 'create_review.html'
    form = CreateReviewForm()

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'create_review.html', { 'form': self.form })
        return redirect('/signin')
    
    def post(self, request):
        if request.user.is_authenticated and request.user.role == UserRoleTypes.CLIENT:
            form = CreateReviewForm(request.POST)
            if form.is_valid():

                rating = form.cleaned_data['rating']
                text = form.cleaned_data['text']

                review = Review.objects.create(name=request.user.username, rating=rating, text=text)
                logging.info(f"Review '{review.name}' was created by {request.user.username} ")
                return redirect('/reviews')
        return redirect('/signin')
    
def promocodes(request):
    promocodes = Promocode.objects.all()
    return render(request, 'promocodes.html', { 'promocodes': promocodes })

class SignInView(LoginView):
    redirect_authenticated_user = True
    template_name = 'signin.html'

    def get_success_url(self):
        return reverse_lazy('agency:home')
    
class SignOutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logging.info(f"{request.user.username} LOGOUT (status: {request.user.role})")
            auth.logout(request)
        return redirect('/home')
    
def hotels(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotels.html', { 'hotels': hotels })

def user_orders(request, pk):
    if request.user.is_authenticated and int(pk) == request.user.id:
        orders = Order.objects.filter(user_id=pk)
        return render(request, 'user_orders.html', { 'orders': orders })
    return render(request, 'user_orders.html', {})

def trips(request):
    if request.method == 'POST':
        duration = request.POST['duration']
        stars = request.POST['stars']
        filter = Q()
        if duration != "0":
            filter &= Q(duration=duration)
        if stars != "0":
            filter &= Q(hotel__stars=stars)

        trips = Trip.objects.filter(filter)
    else:
        trips = Trip.objects.all()
    return render(request, 'trips.html', { 'trips': trips })

def countries(request):
    countries = Country.objects.all()
    return render(request, 'countries.html', { 'countries': countries })

class BuyTripsView(View):
    def get(self, request, pk):
        if request.user.is_authenticated and request.user.role == UserRoleTypes.CLIENT:
            trip = Trip.objects.get(pk=pk)
            form = BuyTripForm()

            return render(request, 'buy.html', { 'trip': trip, 'form': form })
        return HttpResponseNotFound()
    
    def post(self, request, pk):
        if not request.user.is_authenticated:
            return HttpResponseNotFound()
        if not request.user.role == UserRoleTypes.CLIENT:
            return HttpResponseNotFound()

        trip = Trip.objects.get(pk=pk)
        form = BuyTripForm(request.POST)

        if form.is_valid():
            amount = form.cleaned_data['amount']
            promocode = form.cleaned_data['promocode']
            date = form.cleaned_data['departure']

            if amount < trip.available:
                code = Promocode.objects.filter(value=promocode).first()
                Order.objects.create(amount=amount, promocode=code, trip=trip, user=request.user, departure=date)
                trip.available -= amount
                trip.users.add(request.user)
                trip.save()

                return redirect('/home')
            else:
                return HttpResponse('wrong amount of orders')
        return HttpResponse('wrong form')

def users(request):
    if request.user.is_authenticated and request.user.role == UserRoleTypes.STAFF:
        users = User.objects.filter(role=UserRoleTypes.CLIENT)
        return render(request, 'users.html', { 'users': users })
    return HttpResponseForbidden()

def orders(request):
    if request.user.is_authenticated and request.user.role == UserRoleTypes.STAFF:
        orders = Order.objects.all()
        return render(request, 'orders.html', { 'orders': orders })
    return HttpResponseForbidden()

def users_admin(request):
    if request.user.role == UserRoleTypes.STAFF:
        users = User.objects.filter(role=UserRoleTypes.CLIENT).prefetch_related('orders')
        return render(request, 'users_admin.html', { 'users': users })
    return HttpResponseForbidden()

def api(request):
    url = 'https://uselessfacts.jsph.pl/api/v2/facts/random'
    response = requests.get(url)
    if response.status_code != 200:
        return HttpResponseNotFound()
    fact = response.json()

    url = 'https://api.thecatapi.com/v1/images/search'
    response = requests.get(url)
    if response.status_code != 200:
        return HttpResponseNotFound()
    cat = response.json()

    return render(request, 'api.html', { 'fact': fact['text'], 'cat': cat[0]['url'] })

class EditReviewView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            form = UpdateReviewForm()
            review = Review.objects.filter(pk=pk).first()
            return render(request, 'edit.html', { 'form': form, 'review': review })
        return HttpResponseForbidden()
    
    def post(self, request, pk):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        
        form = UpdateReviewForm(request.POST)
        if form.is_valid():
            review = Review.objects.filter(pk=pk).first()
            review.rating = form.cleaned_data['rating']
            review.text = form.cleaned_data['text']
            review.save()

        return redirect('/reviews')
    
def delete_review(request, pk):
    Review.objects.filter(pk=pk).delete()
    return redirect('/reviews')

def diagram(request):
    users = User.objects.filter(role=UserRoleTypes.CLIENT)

    users_in_group = [users.filter(age__range=(18, 35)).count(), users.filter(age__range=(36, 60)).count(),
                        users.filter(age__range=(61, 100)).count()]

    labels = ['19-35', '36-60', '61-100']
    values = users_in_group

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_layout(title='Age Distribution')

    chart = fig.to_html(full_html=False)
    return HttpResponse(chart)

def stats(request):
    clients = User.objects.filter(role=UserRoleTypes.CLIENT)
    ages = [user.age for user in clients]

    avg_age = round(mean(ages), 3)
    median_age = round(median(ages), 3)

    trips = Trip.objects.all()
    prices = [trip.price() for trip in trips]

    avg_price = round(mean(prices), 3)
    median_price = round(median(prices), 3)

    sales = [trip.users.count() for trip in trips]

    avg_sales = round(mean(sales), 3)
    median_sales = round(median(sales), 3)

    return render(request, 'stats.html', 
                  {
                    'avg_age': avg_age,
                    'md_age': median_age,
                    'avg_price': avg_price,
                    'md_price': median_price,
                    'avg_sales': avg_sales,
                    'md_sales': median_sales
                  })
    
