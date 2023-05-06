import requests
from PIL import ImageGrab
import base64

# Take a screenshot
screenshot = ImageGrab.grab()

# Convert the image to base64
with open('screenshot.png', 'wb') as f:
    screenshot.save(f, format='PNG')
with open('screenshot.png', 'rb') as f:
    image_data = f.read()
image_base64 = base64.b64encode(image_data).decode('utf-8')

# Upload the image to Imgur
url = 'https://api.imgur.com/3/image'
headers = {'Authorization': 'Client-ID 7d4122d89e16b07'}
payload = {'image': image_base64}
response = requests.post(url, headers=headers, data=payload)

# Print the URL of the uploaded file
print(response.json())
