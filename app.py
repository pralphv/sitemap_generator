from xml.dom import minidom
from xml.etree.ElementTree import tostring
import os

from flask import Flask, render_template, request, jsonify, make_response, \
    send_from_directory

from xml_generator import generate_sitemap

app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )


@app.route('/')
def landing_page():
    return render_template('index.html')


def adapter(value):
    if isinstance(value, str):
        value = value.split('\n')
    return value


@app.route('/api', methods=['POST'])
def api():
    try:
        parameters = request.json
        url = parameters['url']
        end_points_list = parameters['endPoints']
        prettify = parameters.get('prettify', False)
        languages = parameters.get('languages', [])

        end_points_list = adapter(end_points_list)
        languages = adapter(languages)

        root = generate_sitemap(url, end_points_list, languages)
        xml = tostring(root, encoding='unicode')
        if prettify:
            xml = minidom.parseString(xml).toprettyxml(
                indent="   "
            )
        res = make_response(jsonify({'xml': xml}), 200)
        return res
    except Exception as e:
        print(e)
        return make_response('Bad Request', 400)


if __name__ == '__main__':
    app.run(debug=True)
