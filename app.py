import os 
from flask import send_from_directory    
from flask import Flask, jsonify
import time
app = Flask(__name__)
  
@app.route('/')
def hello_world():
   return jsonify({"Time to call": time.time()})

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

  
if __name__ == '__main__':
   app.run(debug=True)
   