rom flask import Flask
\n\napp = Flask(__name__)\n\
n@app.route(\'/\')\ndef square_root():\n 
   n = 25  # Default value for n\n  
  return f"The square root of {n} is: {n ** 0.5}"\n\n
if __name__ == \'__main__\':\n 
   app.run(debug=True, 
host=\'0.0.0.0\', port=5000)
