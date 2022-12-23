from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/download', methods=["GET", "POST"])
def download():
  if request.method == "POST":
    inputURL = request.form.get("link")
    download.inputURL = request.form.get("link")
    return render_template('videos.html', download=getSource(inputURL), title=getTitle(inputURL), player=getPlayer(inputURL), duration=getDuration(inputURL), uploaded=getUploaded(inputURL))

@app.route('/redirect', methods=["GET", "POST"])
def redirect():
  if request.method == "POST":
    quality = request.form.get("quality")
    return render_template('redirect.html', download=getSource(download.inputURL).replace("720.mp4", (quality + ".mp4")))



#####Functions for fetching data#####

# Fetches video source url
def getSource(inputURL):
  return BeautifulSoup(requests.get(inputURL).text, "html.parser").find("meta", {"property": "og:video:url", "content": True})['content']

# Fetches video title
def getTitle(inputURL):
  return BeautifulSoup(requests.get(inputURL).text, "html.parser").find("h1", class_="uni-headline--2").text.strip()

# Fetches player info (name + location)
def getPlayer(inputURL):
  return BeautifulSoup(requests.get(inputURL).text, "html.parser").find("a", class_="video-owner").text.strip()

# Fetches video duration
def getDuration(inputURL):
  return BeautifulSoup(requests.get(inputURL).text, "html.parser").find("div", class_="metadata-duration").text.strip()

# Fetches video upload date
def getUploaded(inputURL):
  return BeautifulSoup(requests.get(inputURL).text, "html.parser").find("div", class_="metadata-updated").text.strip()

# Fetches video thumbnail
# def getThumbnail(inputURL):
  # thumbnail is dynamically loaded, so beautifulsoup cant scrape it
  
  


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8080)



# future plans
  # hudl watermark remover
  # thumnail on download page