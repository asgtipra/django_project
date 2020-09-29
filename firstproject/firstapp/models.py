from django.db import models
from datetime import date

# Create your models here.
class Login(models.Model):
	name = models.CharField(max_length = 30)
	email = models.EmailField(max_length = 40, primary_key=True)
	password = models.CharField(max_length = 40)

    # include "verbose_name_plural", if this isn’t given, Django will use verbose_name + "s".
	class Meta:
		verbose_name_plural = "Login"

	def __str__(self):
		return self.email


class Python(models.Model):
	session = models.CharField(max_length = 30)

	# include "verbose_name_plural", if this isn’t given, Django will use verbose_name + "s".
	class Meta:
		verbose_name_plural = "Python"

	def __str__(self):
		return self.session


class Student(models.Model):
	name = models.CharField(max_length = 30, unique=False)
	# in case we delete parent class, PROTECT would enable us to retain the data from parent class.
	session = models.ForeignKey("Python", on_delete=models.PROTECT)

	# include "verbose_name_plural", if this isn’t given, Django will use verbose_name + "s".
	class Meta:
		verbose_name_plural = "Student"

	def __str__(self):
		return self.name

# TASK_1 - many-to-one relationship
# A Reporter can have multiple articles but an article can have only one Reporter.
# If you delete a reporter, his articles will be deleted (assuming that the ForeignKey was defined with django.db.models.ForeignKey.on_delete set to CASCADE, which is the default)

class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    class Meta:
    	verbose_name_plural = "Reporter"

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

# TASK_2 - many-to-many relationship
# visit "https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_many/" to learn more
# In this example, an Article can be published in multiple Publication objects, and a Publication has multiple Article objects:

class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
    	verbose_name_plural = "Publication"
    	ordering = ['title']

    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    publications = models.ManyToManyField("Publication")

    def __str__(self):
        return self.headline

    class Meta:
    	verbose_name_plural = "Article"
    	ordering = ['headline']