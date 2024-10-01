

# models.py

from django.db import models

class UserDB(models.Model):
    user_id = models.CharField(max_length=100, null=True, blank=True, unique=True)
    user_roles = (("Seller", "Seller"), ("Buyer", "Buyer"))
    sellername = models.CharField(max_length=100, null=True, blank=True)
    phone_no = models.CharField(max_length=10, null=True, blank=True, unique=True)
    role = models.CharField(max_length=50, choices=user_roles, default="Buyer")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.BooleanField(default=False, null=True, blank=True)

    def key_document_verification(self):
        # Check if all required fields are not None and not empty strings
        if self.user_id and self.sellername and self.phone_no and self.role and self.created_at:
            self.status = True
        else:
            self.status = False
        self.save()

        
    # def save(self, *args, **kwargs):
        # Call key_document_verification to update status before saving the object
        # self.key_document_verification()
        # super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user_id} | {self.sellername} | {self.phone_no}"












# from django.db import models


# # Create your models here.
# class UserDB(models.Model):
#     user_id = models.CharField(max_length=100, null=True, blank=True, unique=True)
#     user_roles = (("Seller", "Seller"), ("Buyer", "Buyer"))
#     sellername = models.CharField(max_length=100, null=True, blank=True)
#     phone_no = models.CharField(max_length=10, null=True, blank=True, unique=True)
#     role = models.CharField(max_length=50, choices=user_roles, default="Buyer")
#     created_at = models.DateTimeField(auto_now_add=True ,null=True, blank=True)

#     status = models.BooleanField(default=False, null=True, blank=True, )
    
#     def key_document_verification(self):
#         if self.user_id and  self.sellername and self.phone_no and self.role and self.created_at:
#             self.status = True 
#         else:
#             self.status = False
#         # self.save()
        
        
#     def save(self, *args, **kwargs):
#         # Call key_document_verification to update status only if not manually set
        
#         self.key_document_verification()
#         super().save(*args, **kwargs)


#     def __str__(self):
#         return f" {self.user_id} | {self.sellername} | {self.phone_no}"
    
    

# class ExcelfileUpload(models.Model):
#     excel_file_upload=models.FileField(upload_to="excel")



    