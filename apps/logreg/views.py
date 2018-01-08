from __future__ import unicode_literals
from django.db import models
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from models import *
import random, re
import bcrypt


def index(request):
    if "errors" not in request.session:
        request.session['errors'] = []
    context = {
        "errors": request.session['errors'],
    }
    request.session.pop("errors")
    return render(request, "logreg/login.html", context)

def register(request):
    if "errors" not in request.session:
        request.session['errors'] = []
    context = {
        "errors": request.session['errors'],
    }
    request.session.pop("errors")
    return render(request, "logreg/register.html", context)

def adminadd(request):
    if "errors" not in request.session:
        request.session['errors'] = []
    context = {
        "errors": request.session['errors'],
    }
    request.session.pop("errors")
    return render(request, "logreg/adminadd.html", context)

def addmember(request):
    if request.method == "POST":
        errors = Member.objects.validate_reg(request.POST)
        if errors:
            request.session['errors'] = errors
            return redirect("/index")
        member = Member.objects.create_member(request.POST)
        request.session['id'] = member.id
    return redirect(reverse("dashboard"))

def edit(request):
    id=request.POST['id']
    if request.method == "POST":
        errors = Member.objects.validate_edit(request.POST)
        if errors:
            request.session['errors'] = errors
            return redirect(reverse('editmember', kwargs = {'id':id}))
    person = Member.objects.edit_member(request.POST)
    return redirect(reverse('showmember', kwargs = {'id':id}))

def delete(request):
    id=request.POST['id']
    person = Member.objects.get(id=id)
    person.delete()
    return redirect(reverse("showmembers"))


def login(request):
    if request.method == "POST":
        result = Member.objects.validate_login(request.POST)
        if len(result['errors']) > 0 :
            request.session['errors'] = result['errors']
            return redirect("/index")
        else :
            member = result['member']
            request.session['id'] = member.id
        return redirect(reverse("dashboard"))

def logout(request):
    if "id" in request.session:
        request.session.pop('id')
    return redirect('/index')
