from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

import debugpy
debugpy.listen(("0.0.0.0",5678))
debugpy.wait_for_client()


@app.route('/')
def hello():
    redis.incr('hit')
    return f"Hello World! I have been seen {redis.get('hit')} times.ddd\n"

@app.route('/hit')
def hit():
    redis.incr('hit')
    return f"{redis.get('hit')}"
    
    # count = get_hit_count()
    # return 'Hello World! I have been seen {} times.\n'.format(count)
