from flask import Flask, render_template
import keys

app = Flask(__name__)

# Print the secret keys to the console
print("API Key 1:", keys.MY_SECRET_API_KEY_1)
print("API Key 2:", keys.MY_SECRET_API_KEY_2)

@app.route("/")
def index():
    all_fruits = [
        {"name": "apples", "quantity": 3},
        {"name": "oranges", "quantity": 2},
        {"name": "strawberries", "quantity": 6}
    ]
   
    fruits = [fruit for fruit in all_fruits if fruit["name"].startswith("o") and fruit["quantity"] < 3]
    return render_template("index.html", fruits=fruits)