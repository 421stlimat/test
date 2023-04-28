from time import sleep
from pyngrok import ngrok

host =ngrok.connect(80, 'http')
print('Connected to: ', host.public_url)
while True:
    sleep(10)
