import flask
from flask import jsonify
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["DEBUG"] = True

@app.route('/veganise', methods=['POST'])
@cross_origin()
def getVeganisedSite(url):

    return jsonify({'<body><h1>Hi</hi></body>'})

app.run(debug=True, use_reloader=False)