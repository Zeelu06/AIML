from flask import Flask, render_template, request, redirect
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def add():

    loyalty_data = []

    if request.method == 'POST':

        loyalty = request.form.get('loyalty')
        cusdata = pd.read_csv('customers.csv')
        loyalty_data = cusdata[cusdata['loyalty_tier'] == loyalty]
        l = len(loyalty_data)
        return render_template('index.html', loyalty=l)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)