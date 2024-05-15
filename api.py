import requests
import io
import os
from dotenv import load_dotenv

load_dotenv()

REIMAGINE_API_ENDPOINT = 'https://clipdrop-api.co/reimagine/v1/reimagine'
API_KEY = os.getenv('API_KEY')


def reimagine_image(image_file):
    try:
        # Make the POST request to the reimagine API
        r = requests.post(REIMAGINE_API_ENDPOINT,
                          files={'image_file': (image_file.filename, image_file.read(), 'image/jpeg')},
                          headers={'x-api-key': API_KEY})

        if r.ok:
            # Return the response content
            return r.content, None
        else:
            # Return an error message if the request to the reimagine API fails
            return None, f'Error: {r.status_code} - {r.text}'
    except Exception as e:
        # Handle any other unexpected errors
        return None, f'Error: {str(e)}'
