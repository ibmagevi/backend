from django.db import models


class Test:
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, editable=False)
    # True means positive
    status = models.BooleanField(default=False)
    hospital = models.CharField(max_length=30)
