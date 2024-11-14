from flask import Flask, render_template
import subprocess
import shutil

app = Flask(__name__)

def run_docker(container_name):
    if not shutil.which("docker"):
        return "Error: Docker no disponible en este contenedor."
    try:
        result = subprocess.check_output(["docker", "run", container_name], text=True)
        return result.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}, Code: {e.returncode}"

@app.route('/')
def home():
    results = {
        "Python": run_docker("kas19/content_task:apppython"),
        "JavaScript": run_docker("kas19/content_task:appjavascript"),
        "Java": run_docker("kas19/content_task:appjava"),
        "Ruby": run_docker("kas19/content_task:appruby"),
        "Go": run_docker("kas19/content_task:appgo")
    }
    return render_template('index.html', results=results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


