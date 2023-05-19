from django.db import models

class TasksModel(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In progress', 'In progress'),
        ('In QA', 'In QA'),
        ('Ready', 'Ready'),
        ('Done', 'Done'),
    ]
    title = models.CharField(max_length=64)
    discription = models.TextField()
    tag = models.CharField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, default='New')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.title
    

    class Meta:
        ordering = ['created']
