# gst_api/views.py
# This API endpoints is return all deatils of user which enter in datail of info we used Django & REST API to fetch details enter gst_number and hit endpoints

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponseBadRequest
import requests
from bs4 import BeautifulSoup


@api_view(['POST'])
def get_gst_details(request):
    gst_number = request.data.get('gst_num')
    if not gst_number:
        return HttpResponseBadRequest("GST number is required.")

    api_url = f'https://irisgst.com/gstin-filing-detail/?gstinno={gst_number}'
    response = requests.get(api_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all elements with the class "four columns"
        elements = soup.find_all(class_='four columns')

        # Data structure to store key-value pairs
        gst_details = {}

        for element in elements:
            p_tags = element.find_all('p')
            for p in p_tags:
                if p.strong:  # Ensure there is a strong tag
                    key = p.strong.get_text(strip=True).strip(
                        ':').strip('-').strip()
                    # Get all text in p, then replace the strong text with nothing to isolate the rest
                    value = p.get_text(strip=True).replace(
                        p.strong.get_text(strip=True), '').strip()
                    gst_details[key + '-'] = value

        return Response({
            'gst_num': gst_number,
            'gst_details': gst_details
        })
    else:
        return Response({
            'error': 'Failed to fetch GST details',
            'status_code': response.status_code
        })
