import json
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect
from gardens_app.forms import VisitorCreationForm
from gardens_app.models import Visitor, Feed, Category


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = VisitorCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = VisitorCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def profile(request):
    name = request.user.username
    visitor = Visitor.objects.get(username=name)
    if not visitor.profile:
        visitor.profile = 'static/img/test_tube.png'
    data = {
        'user': visitor,
        'feeds': Feed.objects.filter(visitor=visitor)
    }
    return render(request, 'profile.html', data)


# javascript files

def view_rss(request):
    feedUrl = request.user.feeds.all()
    allUrls = []
    for url in feedUrl:
        allUrls.append({
            'feedUrl': url.feed_url
        })
    return HttpResponse(json.dumps(allUrls), content_type='application/json')


def add_rss(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        newFeed = Feed.objects.create(
            visitor=request.user,
            feed_url=data,
        )
        response = serializers.serialize('json', [newFeed])
        print response
    return HttpResponse(response, content_type='application/json')

