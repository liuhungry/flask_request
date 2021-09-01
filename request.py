from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template('form.html')
    

@app.route('/first')
def first():
	return render_template('first.html')

@app.route('/second')
def second():
	return render_template('second.html')

@app.route('/third')
def third():
	return render_template('third.html')

@app.route('/key', methods=['GET'])
def key():
    key = request.args.get('fname')

    if key == '1':
        return render_template('first.html')
    elif key == '2':
        return render_template('second.html')
    else:
        return render_template('third.html')           
    
   
if __name__ == '__main__':
	app.run(host='192.168.10.104',port='5000',debug=True)