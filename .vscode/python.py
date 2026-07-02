from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <title>My Portfolio</title>
    <style>
        body {
            font-family: Arial;
            background: #111;
            color: white;
            text-align: center;
        }
        h1 {
            color: #00ffcc;
        }
        .container {
            margin-top: 50px;
        }
        .card {
            background: #222;
            padding: 20px;
            margin: 10px;
            border-radius: 10px;
            display: inline-block;
            width: 250px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>My Portfolio</h1>
        <h2>Hi, I'm Sharuk 👋</h2>
        <p>Aspiring Software Developer</p>

        <h3>Skills</h3>
        <div class="card">Python</div>
        <div class="card">Java</div>
        <div class="card">Web Development</div>

        <h3>Projects</h3>
        <div class="card">Portfolio Website</div>
        <div class="card">To-Do App</div>
        <div class="card">Calculator</div>

        <h3>Contact</h3>
        <p>Email: your@email.com</p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)