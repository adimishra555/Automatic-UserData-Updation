
from django.shortcuts import render
from .models import UserDB

from django.db.models import Q

def index(request):
    if request.method == 'POST':
        from_date = request.POST.get('from_date') or '1900-01-01'
        to_date = request.POST.get('to_date') or '2050-01-01'
        order = request.POST.get('order', 'asc') 
        
        
        if order == 'asc':
            data = UserDB.objects.filter(
                Q(created_at__range=[from_date, to_date]) | Q(created_at__isnull=True)
            ).order_by('created_at')
        else:
            data = UserDB.objects.filter(
                Q(created_at__range=[from_date, to_date]) | Q(created_at__isnull=True)
            ).order_by('-created_at')
            
        for item in data:
            item.key_document_verification()  # Update status for each filtered item
    else:
        data = UserDB.objects.all()
        
    
    return render(request, 'index.html', {'data': data})





import pandas as pd
from django.conf import settings
import uuid
def get(self,request):
    user_data=UserDB.objects.all()
    df = pd.DataFrame(user_data.data)
    print(df)
    df.to_csv(f"public/static/excel/{uuid.uuid4()}.csv", encoding="UTF-8")
    return Response({"status" : True, "data": df })





