from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ProductPhotoForm
from django.utils import timezone
from datetime import timedelta
from .models import Client, Product, Order

import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Пользователь посетил главную страницу')

    html = """
    <html>
    <head><title>Главная страница</title></head>
    <body>
        <h1>Добро пожаловать на мой первый Django-сайт!</h1>
        <p>Здесь вы найдете информацию обо мне и о моем сайте.</p>
    </body>
    </html>
    """
    return HttpResponse(html)


def about(request):
    logger.info('Пользователь посетил страницу "О себе"')

    html = """
    <html>
    <head><title>О себе</title></head>
    <body>
        <h1>Обо мне</h1>
        <p>Здесь вы найдете информацию обо мне.</p>
    </body>
    </html>
    """
    return HttpResponse(html)


def client_orders(request, client_id):
    client = Client.objects.get(pk=client_id)

    # Определение дат для фильтрации заказов
    today = timezone.now()
    week_ago = today - timedelta(days=7)
    month_ago = today - timedelta(days=30)
    year_ago = today - timedelta(days=365)

    # Фильтрация заказов клиента за последнюю неделю, месяц и год
    orders_week = client.order_set.filter(order_date__gte=week_ago)
    orders_month = client.order_set.filter(order_date__gte=month_ago)
    orders_year = client.order_set.filter(order_date__gte=year_ago)

    context = {
        'client': client,
        'orders_week': orders_week,
        'orders_month': orders_month,
        'orders_year': orders_year,
    }

    return render(request, 'client_orders.html', context)


def upload_product_photo(request):
    if request.method == 'POST':
        form = ProductPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('about')
    else:
        form = ProductPhotoForm()
    return render(request, 'upload_product_photo.html', {'form': form})
