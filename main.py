import os
import xml.etree.ElementTree as ET

from flask import Flask, send_file, render_template

app = Flask(__name__)

@app.route("/xml")
def xml_goster():
    tree = ET.parse('templates/yemek.xml')
    root = tree.getroot()

    gunler = {}
    for gun in root.findall('day'):
        gun_adi = gun.get('name')
        yemekler = [{'type': yemek.get('type'), 'content': yemek.text } for yemek in gun.findall('meal')]
        gunler[gun_adi] = yemekler
    xml_data = ET.tostring(root, encoding='unicode')
    return render_template('index.html', gunler=gunler)

if __name__ == "__main__":
    app.run(debug=True)
