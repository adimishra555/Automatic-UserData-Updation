1. Repository Automatic-UserData-Updation is based on Automatic data is saved and update in Excel file and Google spreadsheet.
2. I used Python Django and Django rest API to create backend logic through signals.
3. We can use this API endpoint to update one or more rows or columns in our google and excel sheet.
4. To create access_token we can go https://developers.google.com/.
5. We use signals and request method is POST 'https://sheets.googleapis.com/v4/spreadsheets/{spreadsheetId}/values:batchUpdate' \
--header 'Authorization: Bearer {access_token}' \
--header 'Content-Type: application/json'
