import signal
from time import sleep
from pyngrok import ngrok

ngrok.set_auth_token('2P0zOs6CcjHOdJC3gVEiFaet5rn_3v6NEFF8L8wax9oYqMCmS')

def loop():
    # Start ngrok
    tunnel = ngrok.connect(80, 'tcp')
    print(f"ngrok tunnel established at {tunnel.public_url}")

    # Keep the script running indefinitely
    while True:
        sleep(10)


# Define a signal handler to catch the SIGTERM signal
def sigterm_handler(signal, frame):
    print("SIGTERM received, stopping ngrok...")
    ngrok_process = ngrok.get_ngrok_process()
    if ngrok_process:
        ngrok.kill()
    # Perform any necessary cleanup or shutdown tasks here
    loop()

# Register the signal handler with the signal module
signal.signal(signal.SIGTERM, sigterm_handler)
loop()
