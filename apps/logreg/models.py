from __future__ import unicode_literals
from django.db import models
from django.shortcuts import render, redirect
from django.contrib import messages
from models import *
import random, re
import bcrypt
import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class MemberManager(models.Manager):
    def validate_reg(self, formdata):
        errors = []
        if len(formdata['firstname']) < 1 :
            errors.append("First name is required.")
        if len(formdata['lastname'])  < 1 :
            errors.append("Last name is required.")
        if len(formdata['email'])  < 1 :
            errors.append("Email is required.")
        if len(formdata['password'])  < 1 :
            errors.append("Password is required.")
        if formdata['password'] != formdata['passwordconfirm'] :
            errors.append("Passwords must match.")
        return errors

    def validate_login(self, formdata):
        errors = []
        if len(formdata['email']) < 1 :
            errors.append("Email is required.")
        if len(formdata['password']) < 1 :
            errors.append("Password is required.")
        member = Member.objects.filter(email=formdata['email']).first()
        if member:
            if not bcrypt.checkpw(formdata['password'].encode(), member.password.encode()) :
                errors.append("Email and password do not match.")
        result = {
            "errors": errors,
            "member": member,
        }
        return result

    def create_member(self, formdata):
        password = str(formdata['password'])
        hashedpw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        member = self.create (
            firstname = formdata['firstname'],
            lastname = formdata['lastname'],
            dob = formdata['dob'],
            email = formdata['email'],
            password = hashedpw,
        )
        return member

    def validate_edit(self, formdata):
        errors = []
        if len(formdata['firstname']) < 1 :
            errors.append("First name is required.")
        if len(formdata['lastname'])  < 1 :
            errors.append("Last name is required.")
        if len(formdata['email'])  < 1 :
            errors.append("Email is required.")
        if len(formdata['oldpassword']) > 0 :
            member = Member.objects.filter(email=formdata['email']).first()
            if member:
                if not bcrypt.checkpw(formdata['oldpassword'].encode(), member.password.encode()) :
                    errors.append("Old password is incorrect.")
            if len(formdata['newpw'])  < 1 :
                errors.append("New password is required.")
            if formdata['newpw'] != formdata['newpwconfirm'] :
                errors.append("Confirm your new password.")
        return errors

    def edit_member(self, formdata):
        member = Member.objects.get(id=formdata['id'])
        member.firstname = formdata['firstname']
        member.lastname = formdata['lastname']
        if formdata['newdob']:
            member.dob = formdata['newdob']
        member.email = formdata['email']
        if formdata['newpw']:
            password = str(formdata['password'])
            member.password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        member.level = formdata['level']
        member.save()
        return member

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    dob = models.DateField(default=datetime.date.today)
    level = models.CharField(max_length=10, default="normal")
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MemberManager()
