from flask import Flask,  jsonify
import subprocess
import redis
from kafka import KafkaAdminClient

app = Flask(__name__)

# Configure Redis
redis_client = redis.StrictRedis(
    host='localhost',
    port=6379,
    db=0
)

# Configure Kafka
kafka_admin_client = KafkaAdminClient(bootstrap_servers='localhost:9092')

@app.route('/start', methods=['POST'])
def start_services():
    try:
        print("Starting services...")  # Debug
        # Start Microservice 1
        subprocess.Popen(['python', 'C:\\Users\\user\\Finvedic_Hackathon\\MarketDataSimulator\\MarketDataSimulator\\MarketDataSimulator\\app.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)
        # Start Microservice 2
        subprocess.Popen(['python', 'C:\\Users\\user\\Finvedic_Hackathon\\DataConsumer\\DataConsumer\\DataConsumer\\app.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)
        # Start Microservice 3
        subprocess.Popen(['python', 'C:\\Users\\user\\Finvedic_Hackathon\\DataConsumer\\DataConsumer\\DataConsumer\\consumer.py\\consumer.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)
        print("Microservices started")  # Debug
        return jsonify({"message": "Microservices started successfully!"}), 200
    except Exception as e:
        print(f"Error starting services: {e}")  # Debug
        return jsonify({"error": str(e)}), 500

@app.route('/stop', methods=['POST'])
def stop_services():
    try:
        print("Stopping services...")  # Debug
        # Stop all running microservices using taskkill for Windows
        subprocess.call(['taskkill', '/IM', 'python.exe', '/F'])
        return "Microservices has been stopped"
    except Exception as e:
        print(f"Error stopping services: {e}")  # Debug
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True,port=5003)
