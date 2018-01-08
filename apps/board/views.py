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

def dashboard(request):
    if "id" in request.session:
        member = current_member(request)

    context = {
        "member": member,
    }
    return render(request, "board/dashboard.html", context)
