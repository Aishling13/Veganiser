import flask
from flask import jsonify, request
from flask_cors import CORS, cross_origin
import urllib.request
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

app = flask.Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["DEBUG"] = True

def getHtml(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    return mystr

def replaceHtml(page_html):
    dict = {}
    dict["meat"] = "veg"
    dict["spaghetti"] = "spaggo"
    for key, value in dict.items():
        for i in page_html.findAll():
            if key in i.text:
                if i.string != None:
                    i.string = i.string.replace(key, value)

def page_Css(page_html, url):
    #find all the external CSS style
    external_css= page_html.find_all('link', rel="stylesheet")
    base_url = '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(url))
    for css in external_css:
        css.attrs['href'] = base_url + css.attrs['href']

def page_javaScript(page_html, url):
    #list all the scripts tags
    all_link_script_tags = page_html.find_all('link', rel="preload")
    # all_script_tags = page_html.find_all('script',{"src":True})
    base_url = '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(url))
    
    
    for js in all_link_script_tags:
        js.attrs['href'] = base_url + js.attrs['href']

    # for js in all_script_tags:
    #     if js['src'].startswith('/static/'):
    #         js['src'] = base_url + js['src']

def page_svg(page_html, url):
    #find all the external CSS style
    svg_use_tags= page_html.find_all('use', {'xlink:href': True})
    base_url = '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(url))
    for svg in svg_use_tags:
        svg.attrs['xlink:href'] = base_url + svg.attrs['xlink:href']

@app.route('/veganise', methods=['POST'])
def getVeganisedSite():
    if request.method == 'POST':
        url = request.form.get("url", "")
        #send get request to the url 
        response = requests.get(url)

        #parse the response HTML page
        page_html = BeautifulSoup(response.text, 'html.parser')

        #Extract CSS from the HTML page
        page_Css(page_html, url)

        page_javaScript(page_html, url)

        page_svg(page_html, url)

        replaceHtml(page_html)

        return page_html.prettify()

    return ""

app.run(debug=True)