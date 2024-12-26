import redis
import os

redis_client = redis.StrictRedis(
    host=os.getenv('REDIS_HOST', 'localhost'),  # Default to 'localhost'
    port=6379,
    db=0
)

# Test the connection
try:
    redis_client.ping()
    print("Connected to Redis successfully!")
except redis.ConnectionError:
    print("Failed to connect to Redis.")
