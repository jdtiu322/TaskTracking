from django.db import models
from leader.models import Leader
from user.models import User

class Member(User):
    MemberID = models.AutoField(primary_key=True)
    RoleName = models.CharField(max_length=100)
    LeaderID = models.ForeignKey(Leader, on_delete=models.CASCADE)
    AssignDate = models.DateField()

    def __str__(self):
        return str(self.MemberID)

