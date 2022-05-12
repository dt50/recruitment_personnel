from django.db import models

# Create your models here.


class Departments(models.Model):
    department_name = models.CharField(max_length=80, default='department name')

    count_person = models.IntegerField(default=0)

    MAX_PERSON = models.IntegerField(default=0)
    MIN_PERSON = models.IntegerField(default=0)

    def __str__(self):
        return self.department_name

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'


class Positions(models.Model):
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)

    position = models.CharField(max_length=30, default='position')

    count_person = models.IntegerField(default=0)

    MAX_PERSON = models.IntegerField(default=0)
    MIN_PERSON = models.IntegerField(default=0)

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'
