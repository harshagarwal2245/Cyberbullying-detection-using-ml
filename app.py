from flask import Flask, render_template, request, jsonify
import os
from flask.wrappers import Response
import yaml
import joblib
import numpy as np
from prediction_service import prediction
import time

params_path = "params.yaml"
webapp_root = "webapp"

static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates")

app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)


@app.route("/", methods=["GET", "POST"])
def index():
    t1=time.time()
    if request.method == "POST":
        try:

            if request.form:
                data = dict(request.form).values()
                t = prediction.form_response(data)
                if t == 0:
                    response = "This tweet doesn't contains cyberbullying activites"
                else:
                    response = "This tweet contains cyberbullying activites"
                print(time.time()-t1)
                return render_template("index.html", response=response)
            elif request.json:
                response = prediction.api_response(request.json)
                return jsonify(response)
        except Exception as e:
            print(e)
            error = {"error": e}
            print(time.time()-t1)
            return render_template("404.html", error=error)
    else:
        print(time.time()-t1)
        return render_template("index.html")


if __name__ == '__main__':
    app.run()
