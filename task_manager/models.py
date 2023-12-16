from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Task(models.Model):
    class TaskPriority(models.TextChoices):
        CRITICAL = 'Critical', _('Critical')
        HIGH = 'High', _('High')
        TRIVIAL = 'Trivial', _('Trivial')
        LOW = 'Low', _('Low')
    
    class TaskStatus(models.TextChoices):
        WAITING = 'Waiting', _('Waiting')
        IN_PROGRESS = 'In Progress', _('In Progress')
        DONE = 'Done', _('Done')
        
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    priority = models.CharField(
        max_length=8,
        choices=TaskPriority.choices,
        default=TaskPriority.TRIVIAL
    )

    status = models.CharField(
        max_length=11,
        choices=TaskStatus.choices,
        default=TaskStatus.WAITING
    )
    
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    modified_at = models.DateTimeField(auto_now=True, null=False)

    assigned_to = models.ForeignKey(User, related_name='assigned_tasks', on_delete=models.CASCADE, null=False)
    created_by = models.ForeignKey(User, related_name='created_tasks', on_delete=models.CASCADE, blank=True, null=False)


    def __str__(self):
        return self.title
