from django.db import models

from main.helperMethod import action_on_delete_puchase

class PurchaseModelManager(models.Manager):
    def delete(self):
        
        action_on_delete_puchase(self)
        super().delete()

# class YourModel(models.Model):
#     objects = PurchaseModelManager()