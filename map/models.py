from django.db import models

# Create your models here.

from django.utils.timezone import now
class Pensum(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField()
    created_at = models.DateTimeField(
        auto_now_add=True,
        default=now(),
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        default=now(),
        editable=False,
    )

    @models.permalink
    def get_absolute_url(self):
        return ('map_pensum_detail', (), {'pk': self.pk})

class Teacher(models.Model):
    code = models.IntegerField()
    email = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(
        auto_now_add=True,
        default=now(),
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        default=now(),
        editable=False,
    )

    @models.permalink
    def get_absolute_url(self):
        return ('map_teacher_detail', (), {'pk': self.pk})

class Student(models.Model):
    code = models.IntegerField()
    email = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    student_status = models.IntegerField()
    total_approved_credits = models.IntegerField()
    total_credits_actual_semester = models.IntegerField()
    total_credits_actual_semester = models.IntegerField()
    created_at = models.DateTimeField(
        auto_now_add=True,
        default=now(),
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        default=now(),
        editable=False,
    )

    @models.permalink
    def get_absolute_url(self):
        return ('map_student_detail', (), {'pk': self.pk})

class Course(models.Model):
    code = models.CharField(max_length=200)
    credits = models.IntegerField()
    name = models.CharField(max_length=200)
    summer = models.BooleanField()
    pensum = models.ForeignKey('Pensum')
    created_at = models.DateTimeField(
        auto_now_add=True,
        default=now(),
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        default=now(),
        editable=False,
    )

    @models.permalink
    def get_absolute_url(self):
        return ('map_course_detail', (), {'pk': self.pk})

class Section(models.Model):
    crn = models.IntegerField()
    name = models.CharField(max_length=200)
    semester = models.IntegerField()
    year = models.IntegerField()
    teacher = models.ForeignKey('Teacher')
    course = models.ForeignKey('Course')
    created_at = models.DateTimeField(
        auto_now_add=True,
        default=now(),
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        default=now(),
        editable=False,
    )

    @models.permalink
    def get_absolute_url(self):
        return ('map_section_detail', (), {'pk': self.pk})

class Subject(models.Model):
    grade = models.DecimalField(max_digits=10, decimal_places=5)
    student_status = models.BooleanField()
    student = models.ForeignKey('Student')
    section = models.ForeignKey('Section')
    created_at = models.DateTimeField(
        auto_now_add=True,
        default=now(),
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        default=now(),
        editable=False,
    )

    @models.permalink
    def get_absolute_url(self):
        return ('map_subject_detail', (), {'pk': self.pk})
