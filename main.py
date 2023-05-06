import requests
from PIL import ImageGrab

# Take a screenshot
screenshot = ImageGrab.grab()

# Upload the image to FreeImage.host
url = "https://freeimage.host/api/1/upload"
headers = {"Authorization": "Bearer 6d207e02198a847aa98d0a2a901485a5"}
files = {"image": ("screenshot.png", screenshot.tobytes(), "image/png")}
response = requests.post(url, headers=headers, files=files)

# Print the URL of the uploaded file
if response.status_code == 200:
    response_json = response.json()
    print(response_json.get("image").get("url"))
else:
    print(response.text)
