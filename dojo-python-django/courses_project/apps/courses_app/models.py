from __future__ import unicode_literals
from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['course_name']) <= 5:
            errors["course_name"] = "Course Name should be more than 5 characters"
        if len(postData['course_desc']) <= 15:
            errors["course_description"] = "Course Description should be more than 15 characters"
        return errors


class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # *************************
    # Connect an instance of BlogManager to our Blog model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = CourseManager()
    # *************************

    def __repr__(self):
        return "<Course object: {} {}>".format(self.course_name, self.course_desc)
