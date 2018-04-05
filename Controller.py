from flask import Flask, render_template, request
from Compute import compute
from Model import InputForm

app = Flask(__name__)


@app.route('/hw3', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        a = form.expressionInX.data
        b = form.domain.data
        c = form.eCurves.data
        result = compute(a, b, c)
    else:
        result = None

    return render_template("view_plain.html", form=form, result=result)


if __name__ == '__main__':
    app.run(debug=True)