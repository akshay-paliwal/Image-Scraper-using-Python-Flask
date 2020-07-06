from flask_cors import cross_origin
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import urllib
import os
from PIL import Image
from flask import Flask, render_template, request,jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])  # route for redirecting to the home page
@cross_origin()
def home():
    return render_template('main.html')


@app.route('/searchImages', methods=['GET','POST'])
def searchImages():
    if request.method == 'POST':
        try:
            print("entering post")
            keyWord = request.form['search'].replace(" ","")
  
            url ="https://yandex.com/images/search?text={}".format(keyWord)
            print(url)
            header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
            req = urllib.request.Request(url, headers=header)
            resp = urllib.request.urlopen(req)
            respData = resp.read()
            html = bs(respData, 'html.parser')
            all_images = html.find_all("img", {"class": 'serp-item__thumb justifier__thumb'})
            i = 1
            lst =[]
            for images in all_images:
                 link = [images.get("src")]
                 l = "https:" + link[0]
                 lst.append(l)
       
                 image_name = "./static/image{}".format(i) + ".webp"
                 urllib.request.urlretrieve(l, image_name)

                 im = Image.open("./static/image{}.webp".format(i)).convert("RGB")
                 im.save("./static/image{}.jpg".format(i), "jpeg")
                 os.remove("./static/image{}".format(i) + ".webp")
                 i += 1
                 if i == 16:
                      break
            return render_template('show.html', lst=lst)
    
        except:
            return('Something Went Wrong')
    else:
        return render_template("main.html")

port = int(os.getenv("PORT"))# For cloud deployment
if __name__ == "__main__":
    # app.run(debug = True) # For running on local host
    app.run(host="0.0.0.0", port=port)# For cloud deployment
