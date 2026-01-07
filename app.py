from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    profile = {
        "name": "Alihan",
        "description": "12-year-old student who loves learning, chess, football and dreams of becoming an engineer at MIT.",
        "tags": ["Chess", "Football", "Engineering", "BMW", "Science", "MIT"],
        "dreams": [
            {
                "title": "MIT Engineer",
                "image": "https://upload.wikimedia.org/wikipedia/commons/0/0c/MIT_logo.svg"
            },
            {
                "title": "Chess",
                "image": "https://www.ubergames.co.uk/wp-content/uploads/uber-games-armoured-staunton-sheesham-chess-set-and-box-4-ug668.jpg"
            },
            {
                "title": "Football",
                "image": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Football_%28soccer_ball%29.svg"
            },
            {
                "title": "BMW",
                "image": "https://upload.wikimedia.org/wikipedia/commons/4/44/BMW.svg"
            }
        ]
    }

    return render_template("index.html", profile=profile)

if __name__ == "__main__":
    print("NEW PROFILE PROJECT RUNNING")
    app.run(debug=True)
if __name__ == "__main__":
    app.run(debug=True)