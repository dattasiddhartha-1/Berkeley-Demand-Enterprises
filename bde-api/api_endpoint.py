#creates a api end point for Ruby to call on
#somehow figure this out, @omkar?

from flask import Flask, jsonify, request
from load_processed import DataWrapper

app = Flask(__name__)
query_engine = None

def initialize():
    #constructor
    #initializes and loads in data
    global query_engine
    query_engine = DataWrapper()

def get_demand(time, product):
    #does a lookup for given parameters, and returns value from 0 to 1 for demand
    assert False, "this is deprecated"
    import random
    return random.random() #fake data for now

#input: 
#output:

@app.route('/map/api/v0.2/businesses', methods=['GET'])
def api_demand():
    # print("test")
    # location = request.args.get('location')

    lat_low = float(request.args.get('lat_low'))
    lat_high = float(request.args.get('lat_high'))
    long_low = float(request.args.get('long_low'))
    long_high = float(request.args.get('long_high'))

    categories = request.args.get('categories').split(",") #NOT SECURE LOL
    assert type(categories) == list
    time = request.args.get('time')
    
    # http://127.0.0.1:5000/map/api/v0.2/businesses?lat_low=35.928757&lat_high=36.411223&long_low=-115.491963&long_high=-114.832228&categories=bubble tea, abg&time=Fri-13
    #location=37.868300,-122.258000
    #some parsing
    print(lat_low, lat_high, long_low, long_high, categories, time)
    q = query_engine.query(lat_low, lat_high, long_low, long_high, categories, time)
    print(q)
    return jsonify(q)
    

def start():
    app.run()

if __name__ == '__main__':
    print('starting')
    initialize()
    print(type(query_engine))
    start()