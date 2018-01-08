from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib import messages
from models import *
import random, re, datetime
from django.db import models
from ..logreg.models import Member


class QuoteManager(models.Manager):
    def validate(self, formdata):
        errors = []
        if len(formdata['speaker']) < 3 :
            errors.append("Speaker name must be at least 3 characters long.")
        if len(formdata['message']) < 10 :
            errors.append("Quotes must be at least 10 characters long.")
        return errors

    def create_quote(self, formdata):
        quote = self.create (
            speaker = formdata['speaker'],
            message = formdata['message'],
            posted_by = Member.objects.get(id=formdata['member']),
        )
        return quote

    def addfav(self, formdata, current_member):
        quote = Quote.objects.get(id=formdata['id'])
        member = Member.objects.get(id=current_member.id)
        quote.liked_by.add(member)
        quote.save()
        return quote

    def removefav(self, formdata, current_member):
        quote = Quote.objects.get(id=formdata['id'])
        member = Member.objects.get(id=current_member.id)
        quote.liked_by.remove(member)
        quote.save()
        return quote

class Quote(models.Model):
    speaker = models.CharField(max_length=100, default="")
    message = models.CharField(max_length=255, default="")
    posted_by = models.ForeignKey(Member, related_name="posts")
    liked_by = models.ManyToManyField(Member, related_name="favs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = QuoteManager()
