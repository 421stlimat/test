import signal
from time import sleep
from pyngrok import ngrok

# Define a signal handler to catch the SIGTERM signal
def sigterm_handler(signal, frame):
    print("SIGTERM received, stopping ngrok...")
    ngrok_process = ngrok.get_ngrok_process()
    if ngrok_process:
        ngrok.kill()
    # Perform any necessary cleanup or shutdown tasks here
    exit(0)

# Register the signal handler with the signal module
signal.signal(signal.SIGTERM, sigterm_handler)

# Start ngrok
tunnel = ngrok.connect(80, 'tcp')
print(f"ngrok tunnel established at {tunnel.public_url}")

# Keep the script running indefinitely
while True:
    sleep(10)
