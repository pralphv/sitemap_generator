from xml.dom import minidom
from xml.etree.ElementTree import tostring

from flask import Flask, render_template, request, jsonify, make_response

from xml_generator import generate_sitemap

app = Flask(__name__)


@app.route('/')
def landing_page():
    return render_template('index.html')


@app.route('/api', methods=['POST'])
def api():
    try:
        parameters = request.json
        url = parameters['url']
        end_points_list = parameters['endPoints'].split('\n')
        root = generate_sitemap(url, end_points_list)
        xml = tostring(root, encoding='unicode')
        xml = minidom.parseString(xml).toprettyxml(
            indent="   "
        )
        res = make_response(jsonify({'xml': xml}), 200)
        return res
    except Exception:
        return make_response('Bad Request', 400)


if __name__ == '__main__':
    app.run(debug=True)
