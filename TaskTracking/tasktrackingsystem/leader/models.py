from django.db import models
from user.models import User

class Leader(User):
    LeaderID = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.LeaderID)
