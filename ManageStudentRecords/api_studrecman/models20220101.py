from django.db import models

# Create your models here.

class StudentRecord(models.Model):
    StudIdNum = models.AutoField(primary_key=True)
    Firstname = models.CharField(max_length=50)
    Surname = models.CharField(max_length=50)
    AvScore = models.DecimalField(5,2)
    StudGrade = models.CharField(max_length=4)

class CollegeSubject(models.Model):
    SubjectCode = models.Charfield(max_lenght=20, primary_key=True)
    SubjectName = models.Charfield(max_length=50)

class StudentSubjectRec(models.Model):
    StudentSubjRecId = models.AutoField(Primary_key =True)
    SubjectCode = models.CharField(max_length=20, foreign_key=True)
    SubjectScore = models.IntegerField
    StudIdNum = models.IntegerField(foreign_key=True)
