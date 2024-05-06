from datetime import datetime
from flask import Flask, redirect, render_template, request, url_for
import requests

app = Flask(__name__)


def fetch_data():
    url = "http://uptime-auction-api.azurewebsites.net/api/Auction"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.RequestException:
        return None


@app.route('/')
def index():
    data = fetch_data()
    return render_template('index.html', items=data)


@app.route('/make-bid', methods=['POST'])
def make_bid():
    if request.method == 'POST':
        name = request.form['name']
        sum_amount = request.form['sum']
        product_id = request.form['productId']

        file1 = open("db.txt", "a") 
        file1.write(product_id + ' = ' + name + '-' + sum_amount + '-' + str(datetime.now())+ '\n')
        file1.close()

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
