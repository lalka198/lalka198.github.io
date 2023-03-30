from django.db import models

class Task(models.Model):
    title = models.CharField('Задача:', max_length=100)
    task = models.TextField('Описание задачи')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"


class City(models.Model):
    name = models.CharField(max_length=20)

    def __srt__(self):
        return self.name