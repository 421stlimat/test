import pyautogui
import requests
import base64

# take screenshot
screenshot = pyautogui.screenshot()

# convert image to base64 string
img_buffer = io.BytesIO()
screenshot.save(img_buffer, format='PNG')
img_str = base64.b64encode(img_buffer.getvalue()).decode('ascii')

# set API endpoint and parameters
url = 'https://freeimage.host/api/1/upload'
params = {
    'key': '6d207e02198a847aa98d0a2a901485a5',
    'action': 'upload',
    'source': img_str,
    'format': 'json'
}

# send POST request to API
response = requests.post(url, data=params)

# print response
print(response.json())
