from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib import messages
from models import *
import random, re
from django.db import models
from ..logreg.models import Member
from ..quotes.models import Quote
from ..rest.models import Work, Author


def current_member(request):
    id = request.session['id']
    return Member.objects.get(id=id)

def logout(request):
    request.session.pop('id')
    return redirect(reverse('/'))

def index(request):
    if "id" in request.session:
        member = current_member(request)
    people = Member.objects.all()
    context = {
        "member": member,
        "people": people,
    }
    return render(request, "manager/index.html", context)

def showmember(request, id):
    member = current_member(request)
    person = Member.objects.get(id=id)
    quotes = Quote.objects.filter(liked_by__id=id)[:3]
    posts = Quote.objects.filter(posted_by__id=id)[:2]
    works = Work.objects.filter(liked_by__id=id)
    authors = Author.objects.filter(liked_by__id=id)
    print member.level
    context = {
        "member": member,
        "person": person,
        "quotes": quotes,
        "posts": posts,
        "works": works,
        "authors": authors,
    }
    return render(request, "manager/showmember.html", context)

def editmember(request, id):
    if "errors" in request.session :
        errors = request.session['errors']
    else :
        errors = []
    member = current_member(request)
    person = Member.objects.get(id=id)
    context = {
        "person": person,
        "member": member,
        "errors": errors,
    }
    request.session.pop("errors")
    return render(request, "manager/edit.html", context)

def deletecheck(request, id):
    person = Member.objects.get(id=id)
    context = {
        "person": person,
    }
    return render(request, "manager/deletecheck.html", context)
