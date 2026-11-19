from flask import Flask, render_template, request

app = Flask(__name__)

balance_amount = 10000



# LOGIN


@app.route('/', methods=['GET', 'POST'])
def login():

    message = ""

    if request.method == 'POST':

        account_number = request.form['account-number']
        pin = request.form['pin']

        if account_number == '123456' and pin == '1234':

            return render_template('dashboard.html')

        else:

            message = 'Invalid account number or PIN. Please try again.'

    return render_template('login.html', message=message)



# BALANCE


@app.route('/balance')
def balance():

    return f"Your current balance is ₹{balance_amount}"



# DEPOSIT


@app.route('/deposit', methods=['GET', 'POST'])
def deposit():

    global balance_amount

    message = ""

    if request.method == 'POST':

        amount = int(request.form['amount'])

        balance_amount = balance_amount + amount

        message = f"₹{amount} deposited successfully! Current Balance: ₹{balance_amount}"

    return render_template('deposit.html', message=message)



# WITHDRAW


@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():

    global balance_amount

    message = ""

    if request.method == 'POST':

        amount = int(request.form['amount'])

        if amount > 20000:

            message = "You cannot withdraw more than ₹20,000"

        elif amount > balance_amount:

            message = "Insufficient balance!"

        else:

            balance_amount = balance_amount - amount

            message = f"₹{amount} withdrawn successfully! Current Balance: ₹{balance_amount}"

    return render_template('withdraw.html', message=message)



# START FLASK


if __name__ == '__main__':

    app.run(debug=True)