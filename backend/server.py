import flask
from flask import jsonify, request
from flask_cors import CORS, cross_origin
import urllib.request
from urllib.parse import urlparse
import requests
import re
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
    dict["meaty"] = "veggy"
    dict['\w+(?=\s+stock)'] = 'vegetable'
    dict["beef"] = "quorn"
    dict['chicken'] = 'tofu'
    dict['cheese'] = 'vegan cheese'
    dict['pork'] = 'tofu'
    
    for key, value in dict.items():
        for currentTag in page_html.findAll(['p', 'a', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7']):
            if currentTag.string != None:
                if re.search(key, currentTag.string):
                    split_string = re.split(key, currentTag.string)
                    currentTag.clear()
                    
                    for index in range(0, len(split_string) - 1):
                        # Text before what we want bold
                        tagNotBold = page_html.new_tag("text")
                        tagNotBold.string = split_string[index]
                        currentTag.append(tagNotBold)

                        # Text we want bold
                        tagBold = page_html.new_tag("strong")
                        tagBold.string = value
                        tagBold['class'] = 'veganised'
                        currentTag.append(tagBold)

                    # Final tag
                    tagNotBold = page_html.new_tag("text")
                    tagNotBold.string = split_string[-1]
                    currentTag.append(tagNotBold)

                    
                #i.string = re.sub(key, f'<strong>{value}</strong>', i.string)
                # i.string = i.string.replace(key, value)

def page_Css(page_html, url):
    #find all the external CSS style
    external_css= page_html.find_all('link', rel="stylesheet")
    base_url = '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(url))
    for css in external_css:
        css.attrs['href'] = base_url + css.attrs['href']

    #add additional css
    new_css = page_html.new_tag("style")
    new_css['type'] = 'text/css'
    new_css.string = '.veganised { color: green; }'
    page_html.head.append(new_css)

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

        # page_javaScript(page_html, url)

        page_svg(page_html, url)

        replaceHtml(page_html)

        return page_html.prettify()

    return ""

app.run(debug=True)