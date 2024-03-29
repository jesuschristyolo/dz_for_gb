from django.shortcuts import render
from django.http import HttpResponse
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
