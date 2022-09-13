from django.db import models

# Create your models here.

class Prestamo(models.Model):
    loan_id = models.UUIDField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.DateTimeField(auto_now_add = True)
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    def __str__(self):
        return self.loan_id

    class Meta:
        ordering=["loan_id"]
        managed = False
        db_table = 'prestamo'
