import redis
import json

# Connect to Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def export_redis_data(output_file):
    """
    Fetch all keys with the pattern 'market_data:*' and export their values to a file.
    """
    try:
        # Fetch keys matching the pattern
        keys = redis_client.keys('market_data:*')
        data = {}

        # Retrieve and store data for each key
        for key in keys:
            value = redis_client.get(key)
            if value:
                data[key.decode('utf-8')] = json.loads(value.decode('utf-8'))

        # Write data to a file
        with open(output_file, 'w') as file:
            json.dump(data, file, indent=4)

        print(f"Data exported successfully to {output_file}")

    except Exception as e:
        print(f"Error exporting data: {e}")

if __name__ == "__main__":
    # Specify the output file name
    output_file = "redis_data.json"
    export_redis_data(output_file)
