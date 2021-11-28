from django.shortcuts import render, get_object_or_404
from .models import Portfolio


def feed(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'main/feed.html', {'portfolios': portfolios})


def portfolio_detail(request, id):
    portfolio = get_object_or_404(Portfolio, id=id)
    return render(request, 'main/detail.html', {'portfolio': portfolio})