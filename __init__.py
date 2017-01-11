from flask import Flask, render_template
app = Flask(__name__)

def shutdown_server():
	func = request.environ.get('werkzeug.server.shutdown')
	if func is None:
		raise RuntimeError('Not running with the werkzeug server')
	func()


@app.route("/", methods=['GET'])
def index():
	return render_template("index.html")


if __name__ == "__main__":
	app.debug = True
	try:
		app.run()
	except KeyboardInterrupt:
		shutdown_server()
