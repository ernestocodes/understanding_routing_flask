from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def hi_name(name):
    return f"Hi {name.capitalize()}!"

@app.route('/repeat/<int:num>/<string:str>')
def repeat_string(num,str):
    output = ""
    for i in range(num):
        output+= str +"\n"
    return output


if __name__ == "__main__":
    app.run(debug=True)