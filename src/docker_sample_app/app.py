from flask import Flask
import redis

app = Flask(__name__)
client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def hello():
    count = client.incr('hits')
    return f'Hello World! This page has been visited {count} times.'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    