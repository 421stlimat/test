from time import sleep
from pyngrok import ngrok

ngrok.set_auth_token('2P0zOs6CcjHOdJC3gVEiFaet5rn_3v6NEFF8L8wax9oYqMCmS')
tunnel =ngrok.connect(80, 'tcp')

while True:
    sleep(10)
