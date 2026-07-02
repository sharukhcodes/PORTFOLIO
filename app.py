from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Sharuk Portfolio</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #020617, #0f172a);
            color: white;
            scroll-behavior: smooth;
        }

        header {
            display: flex;
            justify-content: space-between;
            padding: 20px 50px;
            background: rgba(0,0,0,0.3);
            position: sticky;
            top: 0;
            backdrop-filter: blur(10px);
        }

        header h1 {
            color: #38bdf8;
        }

        nav a {
            margin-left: 20px;
            color: white;
            text-decoration: none;
        }

        nav a:hover {
            color: #38bdf8;
        }

        .hero {
            text-align: center;
            padding: 100px 20px;
        }

        .hero h2 {
            font-size: 45px;
            background: linear-gradient(to right, #38bdf8, #22c55e);
            -webkit-background-clip: text;
            color: transparent;
        }

        .hero p {
            margin-top: 10px;
            font-size: 18px;
            opacity: 0.8;
        }

        .btn {
            margin-top: 20px;
            padding: 12px 25px;
            background: #38bdf8;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            transition: 0.3s;
        }

        .btn:hover {
            background: #0ea5e9;
            transform: scale(1.05);
        }

        .section {
            padding: 60px 20px;
            text-align: center;
        }

        .cards {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
        }

        .card {
            background: rgba(255,255,255,0.05);
            margin: 15px;
            padding: 25px;
            border-radius: 12px;
            width: 260px;
            backdrop-filter: blur(10px);
            transition: 0.3s;
        }

        .card:hover {
            transform: translateY(-10px);
            background: rgba(255,255,255,0.1);
        }

        .projects .card {
            cursor: pointer;
        }

        footer {
            text-align: center;
            padding: 20px;
            background: rgba(0,0,0,0.3);
        }

        /* Mobile responsive */
        @media(max-width: 768px) {
            header {
                flex-direction: column;
                align-items: center;
            }

            nav {
                margin-top: 10px;
            }

            .hero h2 {
                font-size: 30px;
            }
        }
    </style>
</head>

<body>

<header>
    <h1>Sharuk</h1>
    <nav>
        <a href="#">Home</a>
        <a href="#skills">Skills</a>
        <a href="#projects">Projects</a>
        <a href="#contact">Contact</a>
    </nav>
</header>

<section class="hero">
    <h2>I Build Cool Websites 🚀</h2>
    <p>Aspiring Software Developer | Python | Web Dev</p>
    <button class="btn">Hire Me</button>
</section>

<section id="skills" class="section">
    <h2>Skills</h2>
    <div class="cards">
        <div class="card">Python</div>
        <div class="card">Java</div>
        <div class="card">HTML, CSS, JS</div>
        <div class="card">DSA</div>
    </div>
</section>

<section id="projects" class="section projects">
    <h2>Projects</h2>
    <div class="cards">
        <div class="card">Portfolio Website</div>
        <div class="card">To-Do App</div>
        <div class="card">Calculator</div>
    </div>
</section>

<section id="contact" class="section">
    <h2>Contact</h2>
    <p>Email: sharukh7117@email.com</p>
</section>

<footer>
    <p>© 2026 Sharuk Prashanth</p>
</footer>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)