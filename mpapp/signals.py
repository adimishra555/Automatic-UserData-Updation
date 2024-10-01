# ! this code is for display data in google drive sheet from admin db

from django.utils import timezone
import pandas as pd
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserDB
from .google_sheets import update_google_sheet


@receiver(post_save, sender=UserDB)
def update_google_sheet_on_save(sender, instance, created, **kwargs):
    if created:
        # Call key_document_verification to update the status
        instance.key_document_verification()

        # Format the data to be added to the Google Sheet
        data = [instance.user_id, instance.sellername, instance.phone_no,
                instance.role, instance.created_at, instance.status]

        # Update Google Sheet
        update_google_sheet(data)


# ? this code is export data from admin database and display in excel file when new data is comes in db
# signals.py


@receiver(post_save, sender=UserDB)
def export_to_excel(sender, instance, created, **kwargs):
    if created:
        data = UserDB.objects.all().values('user_id', 'sellername',
                                           'phone_no', 'role', 'created_at', 'status')
        df = pd.DataFrame(data)

        # Convert created_at to timezone-unaware datetime
        df['created_at'] = df['created_at'].apply(
            lambda x: x.replace(tzinfo=None) if x else None)

        df.to_excel('DBdata.xlsx', index=False)  # Export to Excel file
        print(df)
