from django.db import models
from leader.models import Leader

class Project(models.Model):
    ProjectID = models.AutoField(primary_key=True)  # Correct usage of AutoField
    ProjectName = models.CharField(max_length=255)
    LeaderID = models.ForeignKey(Leader, on_delete=models.CASCADE)
    StartDate = models.DateField()
    Deadline = models.DateField()

    def __str__(self):
        return self.ProjectName
