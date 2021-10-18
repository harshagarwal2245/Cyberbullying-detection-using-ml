from flask import Flask, render_template, request, jsonify
import os
from flask.wrappers import Response
import yaml
import joblib
import numpy as np
from prediction_service import prediction

params_path = "params.yaml"
webapp_root = "webapp"

static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates")

app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)




@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            if request.form:
                data=dict(request.form).values() 
                text=list(data)[0]
                t=prediction.predict(text)
                if t==0:
                    response="This tweet doesn't contains cyberbullying actvities "
                else:
                    response="This tweet contains cyberbullying actvitis"

                return render_template("index.html",response=response)

        except Exception as e:
            print(e)
            error={"error":"Something went wrong"}
            return render_template("404.html",error=error)
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run()