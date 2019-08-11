from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/post_field", methods=["POST"])
def need_input():

    str_html = ""

    """for key in request.form:
        #if key.startswith('comment.'):
            ##id_ = key.partition('.')[-1]
            #value = request.form[key]
            #return value
        return key"""
    #form = StateForm(request.form)
    for k, v in request.form.items():
        str_html = str_html + "<br>" + k + " " + v

    return str_html

@app.route("/", methods=["GET"])
def get_form():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8000", debug=True)