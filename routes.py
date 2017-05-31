from flask import Flask, render_template, request, abort, jsonify
import devgif

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/gif', methods=['GET'])
def gif():
    gif = devgif.get(q=request.args.get('q'))
    return render_template('gif.html',
                           title=gif[0],
                           url=gif[1],
                           likes=gif[2])


@app.route('/slack', methods=['POST'])
def slack():
    slack_token = 'LjEN3AoSaR4Jur51qKxAEVkU'
    if request.form.get('token') != slack_token:
        return abort(403)

    gif = devgif.get(q=request.form.get('text'))
    response = {
        'response_type': 'in_channel',
        'attachments': [{
            'title': gif[0],
            'image_url': gif[1]
        }]
    }
    return jsonify(response)


@app.route('/twist', methods=['POST'])
def twist():
    twist_token = '9_c3a15aac02fb8742157484d4'

    if request.form.get('verify_token') != twist_token:
        return abort(403)

    if request.form.get('event_type') == 'ping':
        return jsonify({'content': 'pong'})

    arg = request.form.get('command_argument')
    gif = devgif.get(q=arg)
    return jsonify({
        'content': '%s\n**%s**' % (request.form.get('content'), gif[0]),
        'attachments': [{
            'url': gif[1],
            'url_type': 'image',
            'image': gif[1],
        }]
    })


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8888)
