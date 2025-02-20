from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    
    full_name = "Akash Kumar"  

    username = os.getenv("USER", "Unknown")

    
    ist_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    
    top_output = subprocess.getoutput('top -b -n 1 | head -10')

    
    return f"""
    <h1>Name: {full_name}</h1>
    <h2>Username: {username}</h2>
    <h3>Server Time (IST): {ist_time}</h3>
    <h4>TOP Output:</h4>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
