from flask import Flask
import time
import threading

app = Flask(__name__)

# CPU-intensive function to simulate load (Fibonacci calculation)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Function that simulates load every 10 seconds
def simulate_cpu_load():
    while True:
        # Simulate high CPU usage by calculating Fibonacci(35)
        fibonacci(35)  # You can increase this number for more CPU load
        time.sleep(10)  # Wait for 10 seconds before running again

@app.route('/')
def hello_world():
    return 'Hello, World from abhishek! CPU load simulation running...'

if __name__ == '__main__':
    # Start the CPU load simulation in a separate thread
    threading.Thread(target=simulate_cpu_load, daemon=True).start()
    
    # Run the Flask app
    app.run(host="0.0.0.0", port=80)
