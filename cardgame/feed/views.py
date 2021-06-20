from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import feed, feedtable
from math import ceil
# Create your views here.


def feed(response, id):
    #    if response.method == "POST":
    #       id_new = id+1
    #        return HttpResponseRedirect("/feed/"+str(id_new))
    feed_table = feedtable.objects.get(id=1)
    feed_set = feed_table.feed_set.all()
    last_page = ceil(feed_set.count()/2)
    if ceil(id/2) >= last_page:
        return redirect("../feed/1")
    else:
        return render(response, "feed/feed_page.html", {'feed_set': feed_set, "id": id, "id1": 2*id-1, "id2": 2*id, "id_next": id+1, "id_prev": id-1})


def blog_open(response, name):
    feed_table = feedtable.objects.get(id=1)
    feed_set = feed_table.feed_set.all()
    blog = feed_set.filter(display_link=name)[0]
    id = int(ceil(blog.id/2))
    return render(response, "feed/blog_page.html", {"blog": blog, "id_prev": id})
