from os import name
from flask import Flask, request, json
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
import base64
from PIL import Image
import io
from flask_restful import Api
from facenet_module import predict
import json
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

@app.route('/api', methods = ['POST'])
def postDemo():
    request_data = json.loads(request.data)
    image = request_data['image']
    imageBased = base64.b64decode(image)
    img = Image.open(io.BytesIO(imageBased))
    response = predict(img)
    return {"result": response["results"],
            "image": response["img"].decode('utf-8')}

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002)