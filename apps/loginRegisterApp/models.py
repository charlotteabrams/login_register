from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
from django.contrib import messages

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Our new manager!
class UserManager(models.Manager):
	def register(self, userinfo, request):
		# userinfo is a dictionary of stuff from request.POST
		error = True
		if not EMAIL_REGEX.match(userinfo['email']):
			error = False
		if len(userinfo['first_name']) < 2:
			messages.error(request, "First name is too short.")
			error = False
		if len(userinfo['last_name']) < 2:
			messages.error(request, "Last name is too short.")
			error = False
		if len(userinfo['password']) < 8:
			messages.error(request, "Password must have 8 characters")
			error = False
		if userinfo['password'] != userinfo['confirm']:
			messages.error(request, "Passwords must match.")
			error = False
		if len(User.objects.filter(email = userinfo['email'])) > 0:
			messages.error(request, "This information is already in our database")
			error = False

		if error == True:
			messages.success(request, "You have successfully entered in the information. Now you can login!")
			password = userinfo['password']
			hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
			print hashed
			User.objects.create(first_name = userinfo['first_name'], last_name = userinfo['last_name'], email = userinfo['email'], password = hashed)
			return True
		else:
			return False
		#.filter will return an array of user objects. .get returns user object or null not mathed

	def login(self, userinfo, request,):
		error = False
		if len(User.objects.filter(email = userinfo['email'])) > 0:
			hashed = User.objects.get(email = userinfo['email']).password
			password = userinfo['password']
			hashed = hashed.encode('utf-8')
			password = password.encode('utf-8')
			# User is the table in the db, objects is the table manager, .get is a method of the manager
			#.get returns user object. calling .password gets the password on that object
			# we use email (and its relationship to the ecrypted passwordto find the ecrypted password since we do not know the value of said envrypted password
			if bcrypt.hashpw(password, hashed) == hashed:
				name = User.objects.get(email=userinfo['email']).first_name
				messages.success(request, "Success! Welcome " + name + "! You have successfully registered")
				error = True
		return error

class User(models.Model):
	userManager = UserManager()
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = models.Manager()

    # *************************
    # Connect an instance of UserManager to our User model!
    # Re-adds objects as a manager (so all the normal ORM literature matches)
    # *************************