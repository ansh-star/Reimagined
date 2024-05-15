from flask import Flask, request, send_file
from api import reimagine_image
from error_handling import handle_error
import io

app = Flask(__name__)


@app.route('/reimagine', methods=['POST'])
def reimagine():
    try:
        # Get the image file from the request
        image_file = request.files['image_file']

        # Call the function to reimagine the image
        image_data, error_message = reimagine_image(image_file)
        if image_data:
            # Create a file-like object from the response content
            image_stream = io.BytesIO(image_data)

            # Send the image file as the response
            return send_file(image_stream, mimetype='image/jpeg')
        else:
            # Return error message
            return handle_error(error_message, 500)
    except KeyError:
        # Return an error message if 'image_file' is not present in the request
        return handle_error('Error: No image file provided in the request', 400)
    except Exception as e:
        # Handle any other unexpected errors
        return handle_error(f'Error: {str(e)}', 500)


if __name__ == '__main__':
    app.run(debug=True)
