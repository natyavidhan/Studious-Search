from flask import Flask, request, jsonify, send_from_directory
import json

app = Flask(__name__)

routes = json.load(open('routes.json'))
print(routes)

@app.route('/')
def main():
    for route in routes.keys():
        if route == "":
            return send_from_directory('', f"Files/{routes[route]}.json")


@app.route('/<route>')
def routing(route):
    if route in routes.keys():
        return send_from_directory('', f"Files/{routes[route]}.json")
    else:
        return 'Route not found'
    
if __name__ == '__main__':
    app.run(debug=True)