from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib import messages
from models import *
import random, re
from django.db import models
from ..logreg.models import Member


def current_member(request):
    id = request.session['id']
    return Member.objects.get(id=id)

def logout(request):
    request.session.pop('id')
    return redirect(reverse('/'))

def quotelist(request):
    if "id" in request.session:
        member = current_member(request)
    if "errors" in request.session:
        errors = request.session['errors']
        request.session['errors'] = []
    else :
        errors = []
    quotes = Quote.objects.exclude(liked_by=member.id).order_by("-created_at")
    favs = Quote.objects.filter(liked_by=member.id)

    context = {
        "member": member,
        "quotes": quotes,
        "favs": favs,
        "errors": errors,
    }

    return render(request, "quotes/quotelist.html", context)


def addquote(request):
    if request.method == "POST":
        errors = Quote.objects.validate(request.POST)
        if errors:
            request.session['errors'] = errors
            return redirect('/quotelist')
    Quote.objects.create_quote(request.POST)
    return redirect(reverse("quotelist"))

def addfav(request):
    member = current_member(request)
    quote = Quote.objects.addfav(request.POST, member)
    print quote.liked_by
    return redirect(reverse("quotelist"))

def removefav(request):
    member = current_member(request)
    quote = Quote.objects.removefav(request.POST, member)
    print quote.liked_by
    return redirect(reverse("quotelist"))

def memberquotes(request, id):
    count = len(Quote.objects.filter(posted_by=id))
    member = Member.objects.get(id=id)
    posts = Quote.objects.filter(posted_by=id).order_by("-created_at")
    context = {
        "member": member,
        "posts": posts,
        "count": count,
    }
    return render(request, "quotes/memberquotes.html", context)
