from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    start_year = models.IntegerField(default=1900)
    end_year = models.IntegerField(default=None, null=True, blank=True)
    
    class Meta:
        db_table = 'musicians'