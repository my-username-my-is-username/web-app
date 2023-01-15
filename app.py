from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
#why is flask syntax so funky
def dex():
	return render_template("index.html")
	
@app.route("/p2", methods=['POST'])
def thing():
	pyname = request.form.get("formname")
	if pyname == None: pyname = ""
	return render_template("p2.html", htmlname=pyname)


#yknow i dont fully understand what the below line means
#but whatever lmao
if __name__ == "__main__":
	app.run(debug=True)