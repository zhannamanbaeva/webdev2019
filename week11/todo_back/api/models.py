from django.db import models

# Create your models here.


class TaskList(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def to_json(self):
        return{
            'name': self.name,
            'id': self.id,
        }


class Task(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    due_on = models.DateTimeField()
    status = models.CharField(max_length=50)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.due_on,self.name)

    def to_json(self):
        return {
            'id':self.id,
            'name': self.name,
            'created_at': self.created_at,
            'due_on': self.due_on,
            'status': self.status
        }


