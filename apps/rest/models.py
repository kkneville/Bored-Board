from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from models import *
from django.db import models
import random, re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from ..logreg.models import Member

class AuthorManager(models.Manager):
    def validate(self, formdata):
        errors = []
        if (len(formdata['firstname']) < 2) or (not formdata['firstname'].isalpha()):
            errors.append("Invalid first name.")
        if (len(formdata['lastname']) < 2) or (not formdata['lastname'].isalpha()):
            errors.append("Invalid last name.")
        return errors


    def create_author(self, formdata):
        author = self.create (
            firstname = formdata['firstname'],
            middlename = formdata['middlename'],
            lastname = formdata['lastname'],
            sex = formdata['sex'],
            span = formdata['span'],
            bio = formdata['bio'],
            link = formdata['link'],

        )
        return author

    def edit(self, formdata):
        author = Author.objects.get(id=formdata['id'])
        author.firstname = formdata['firstname']
        author.middlename = formdata['middlename']
        author.lastname = formdata['lastname']
        author.sex = formdata['sex']
        author.span = formdata['span']
        author.bio = formdata['bio']
        author.link = formdata['link']
        author.save()
        return author


    def likeauthor(self, formdata, current_member):
        author = Author.objects.get(id=formdata['authorid'])
        member = Member.objects.get(id=current_member.id)
        author.liked_by.add(member)
        author.save()
        return author   

class Author(models.Model):
    firstname = models.CharField(max_length=255)
    middlename = models.CharField(max_length=255, default="")
    lastname = models.CharField(max_length=255)
    sex = models.CharField(max_length=20, default="female")
    span = models.CharField(max_length=20, default="")
    bio = models.CharField(max_length=1000, default="")
    link = models.CharField(max_length=100, default="")
    liked_by = models.ManyToManyField(Member, related_name="liked_author")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AuthorManager()

class WorkManager(models.Manager):
    def validate(self, formdata):
        errors = []
        if len(formdata['title']) < 1 :
            errors.append("New works must have a title.")
        return errors

    def create_work(self, formdata):
        work = self.create (
            title = formdata['title'],
            year = formdata['year'],
            worktype = formdata['worktype'],
            author = Author.objects.get(id=formdata['author']),
            desc = formdata['desc'],
            excerpt = formdata['excerpt']
        )
        return work

    def edit(self, formdata):
        work = Work.objects.get(id=formdata['workid'])
        work.title = formdata['title']
        work.year = formdata['year']
        work.worktype = formdata['worktype']
        work.desc = formdata['desc']
        work.link = formdata['link']
        work.excerpt = formdata['excerpt']
        work.save()
        return work


    def likework(self, formdata, current_member):
        work = Work.objects.get(id=formdata['workid'])
        member = Member.objects.get(id=current_member.id)
        work.liked_by.add(member)
        work.save()
        return work

class Work(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    desc = models.CharField(max_length=255)
    worktype = models.CharField(max_length=100, default="")
    author = models.ForeignKey(Author, related_name="works")
    excerpt = models.CharField(max_length=1500, default="")
    link = models.CharField(max_length=200, default="")
    liked_by = models.ManyToManyField(Member, related_name="liked_work")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = WorkManager()

class Tag(models.Model):
    value = models.CharField(max_length=50)
    work = models.ManyToManyField(Work, related_name="tags")
    author = models.ManyToManyField(Author, related_name="tags")

class CommentManager(models.Manager):
    def create_comment(self, formdata):
        comment = self.create (
            content = formdata['content'],
            member = Member.objects.get(id=formdata['workid']),
            work = Work.objects.get(id=formdata['workid']),
        )
        return comment

class Comment(models.Model):
    content = models.CharField(max_length=1000)
    member = models.ForeignKey(Member, related_name="comments")
    work = models.ForeignKey(Work, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CommentManager()

class ReplyManager(models.Manager):
    def create_reply(self, formdata):
        reply = self.create (
            content = formdata['content'],
            member = Member.objects.get(id=formdata['memberid']),
            comment = Comment.objects.get(id=formdata['commentid']),
        )
        return comment

class Reply(models.Model):
    content = models.CharField(max_length=1000)
    member = models.ForeignKey(Member, related_name="replies")
    comment = models.ForeignKey(Comment, related_name="replies")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ReplyManager()
