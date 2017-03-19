from flask import Flask, render_template, request
import devgif

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/gif')
def gif():
    q = request.args.get('q', '')
    r = devgif.get(q=q)
    return render_template('gif.html',
                           title=r[0],
                           url=r[1],
                           likes=r[2])


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8888)
