
from flask import Flask, render_template, request

app = Flask(__name__)

# Initial stock value
stock = 50
daily_usage = 5   # items used per day

# Function to predict days left
def predict_days(stock):
    if daily_usage == 0:
        return 0
    return stock // daily_usage

@app.route('/')
def home():
    global stock
    
    message = ""
    alert_type = ""

    # Basic Alert
    if stock < 20:
        message = "⚠️ Low Stock Alert!"
        alert_type = "low"

    # Predictive Alert
    days_left = predict_days(stock)
    prediction_msg = f"Estimated stock will last for {days_left} days"

    if days_left <= 3:
        prediction_msg += " ⚠️ (Critical: Reorder soon!)"

    return render_template(
        'index.html',
        stock=stock,
        message=message,
        prediction=prediction_msg,
        days_left=days_left
    )

@app.route('/update', methods=['POST'])
def update():
    global stock
    stock = int(request.form['stock'])
    return home()

if __name__ == '__main__':
    app.run(debug=True)

