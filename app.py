
from flask import Flask, render_template, request
from scraper.scrapper import WikiScrapper




app=Flask(__name__)

@app.route("/",methods=["GET", "POST"])
def index():
  if request.method=='POST':
    keyword = request.form["keyword"]
    scrapper = WikiScrapper(keyword)
    results = scrapper.scrape()
    return render_template("results.html", results=results)
  return render_template('index.html')


if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)



