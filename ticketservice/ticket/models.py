from django.db import models

class Ticket(models.Model):
    tickettime = models.DateTimeField(auto_now_add = True)
    userid = models.IntegerField(null = False, default=0)
    contains = models.CharField(max_length = 999, unique = False, blank = True, null = False, default="")
    
    class Meta:
        ordering = ('tickettime',)
