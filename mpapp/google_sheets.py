import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from .models import UserDB



def serialize_data(data):
    serialized_data = []
    for item in data:
        if isinstance(item, datetime):
            serialized_data.append(item.strftime('%Y-%m-%d %H:%M:%S'))  # Convert datetime to string
        else:
            serialized_data.append(item)
    return serialized_data



def update_google_sheet(data):
    # Set up credentials
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(r"C:\Users\lenovo\Downloads\prodata-418012-a1fdb99756a8.json", scope)
    gc = gspread.authorize(credentials)

    # Open the Google Sheet
    sheet = gc.open("prodata").sheet1  
   
    if sheet.row_count == 0:
        
        headers = ['User ID', 'Seller Name', 'Phone Number', 'Role', 'Created At', 'Status']
        sheet.append_row(headers)

    # Serialize data
    serialized_data = serialize_data(data)

    # Append data to the sheet
    sheet.append_row(serialized_data)

    
    sheet_url = f"https://docs.google.com/spreadsheets/d/{sheet.id}"
    
    return sheet_url











# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
# from datetime import datetime

# def serialize_data(data):
#     serialized_data = []
#     for item in data:
#         if isinstance(item, datetime):
#             serialized_data.append(item.strftime('%Y-%m-%d %H:%M:%S'))  # Convert datetime to string
#         else:
#             serialized_data.append(item)
#     return serialized_data

# def update_google_sheet(data):
#     # Serialize data
#     serialized_data = serialize_data(data)

#     # Set up credentials
#     scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
#     credentials = ServiceAccountCredentials.from_json_keyfile_name(r"C:\Users\lenovo\Downloads\prodata-418012-a1fdb99756a8.json", scope)
#     gc = gspread.authorize(credentials)

#     # Open the Google Sheet
#     sheet = gc.open("prodata").sheet1  # Replace "drivedata" with your actual sheet name

    
    
#     # Add headers
#     # headers = ['User ID', 'Seller Name', 'Phone Number', 'Role', 'Created At', 'Status']
#     # sheet.append_row(headers)

#     # Serialize data
#     serialized_data = serialize_data(data)

#     # Append data to the sheet
#     sheet.append_row(serialized_data)

    

#     # Get the URL of the Google Sheet
#     sheet_url = f"https://docs.google.com/spreadsheets/d/{sheet.id}"
    
#     return sheet_url

