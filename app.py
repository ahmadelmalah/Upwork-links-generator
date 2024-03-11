from flask import Flask, render_template
from urllib.parse import urlencode


app = Flask(__name__)

rare_skills = ['fastapi', 'langchain', 'boto3', 'apollo']
avg_skills = [ 'flask', 'aws', 'gcp', 'azure', 'celery']
general_skills = ['python', 'restful', 'api']
keywords = ['python', 'flask', 'restful', 'api', 'fastapi', 'aws']
upwork_link = 'https://www.upwork.com/nx/search/jobs/?sort=recency&q='


def basic_links_generator():
    links = [upwork_link + item for item in rare_skills]
    return links

def links_verified_generator():
    params = {"payment_verified": "1"}
    encoded_params = urlencode(params)
    links = [upwork_link + item + '&' + encoded_params for item in keywords]
    return links

@app.route("/")
def hello_world():
    basic_links = basic_links_generator()
    links_verified = links_verified_generator()

    return render_template("index.html",
                            basic_links=basic_links,
                            links_verified=links_verified)