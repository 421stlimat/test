import requests
from PIL import ImageGrab
import io

# Take a screenshot
screenshot = ImageGrab.grab()

# Convert the image to bytes
with io.BytesIO() as output:
    screenshot.save(output, format='PNG')
    image_bytes = output.getvalue()

# Upload the image to Gofile
url = "https://srv-store4.gofile.io/uploadFile"

response = requests.post(url, files={"file": ("screenshot.png", image_bytes)})

# Print the URL of the uploaded file
print(response.json())
