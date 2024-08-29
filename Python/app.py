from flask import Flask

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello' : 'world'}

api.add_resource(HelloWorld,'/')

if __name__ ==  "__main__":
    helloworld.run(host="0.0.0.0", debug=True)