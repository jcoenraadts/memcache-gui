from flask import Flask, request,jsonify
from flask import render_template
from flask_moment import Moment
import memcache
import memcacheinspector

servers = ['memcached:11211']

app = Flask(__name__)
moment = Moment(app)

@app.route('/')
def index():
    data = []
    mci = memcacheinspector.MemcacheInspector(servers)

    for server, items in mci.get_items(max_value_size=0, include_values=True).items():
        for item in items:
            data.append({
                'expiration': item.expiration,
                'size': item.size,
                'key': item.key,
                'value': item.value
            })

    return render_template('index.html', items=data)


# AJAX functions
@app.route('/set/', methods=['POST'])
def set():
    content = request.get_json()
    print(content)
    mc = memcache.Client(servers)
    mc.set(content['key'], content['value'], content['time'])
    return jsonify(content)


@app.route('/delete/<key>', methods=['POST'])
def delete(key):
    mc = memcache.Client(servers)
    mc.delete(key)
    return jsonify({ 'key': key, 'status': 'ok' })


@app.route('/flush/', methods=['POST'])
def flush():
    mc = memcache.Client(servers)
    mc.flush_all()
    return jsonify({'status': 'ok'})


if __name__ == "__main__":
    app.run(debug=True)
