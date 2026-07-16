import os
import datetime
import hashlib
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
from playhouse.shortcuts import model_to_dict

from . import data

load_dotenv()
app = Flask(__name__)

PAGES = [
    {"endpoint": "index", "label": "Home"},
    {"endpoint": "hobbies", "label": "Hobbies"},
    {"endpoint": "map", "label": "Map"},
    {"endpoint": "timeline", "label": "Timeline"},
]

@app.context_processor
def inject_globals():
    return {
        "pages": PAGES,
        "url": os.getenv("URL"),
        "about": data.ABOUT,
    }

@app.route('/')
def index():
    return render_template(
        'index.html',
        title="MLH Fellow",
        experiences=data.EXPERIENCES,
        education=data.EDUCATION,
    )

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies", hobbies=data.HOBBIES)

@app.route('/map')
def map():
    return render_template('map.html', title="Map", locations=data.LOCATIONS)

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306
    )

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form.get('name')
    email = request.form.get('email')
    content = request.form.get('content')

    if not name or not name.strip():
        return 'Invalid name', 400
    if not content or not content.strip():
        return 'Invalid content', 400
    if not email or '@' not in email:
        return 'Invalid email', 400

    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/api/timeline_post/<int:post_id>', methods=['DELETE'])
def delete_time_line_post(post_id):
    post = TimelinePost.get_by_id(post_id)
    post.delete_instance()
    return ''

@app.route('/timeline')
def timeline():
    timeline_posts = [
        model_to_dict(p)
        for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
    ]
    
    for post in timeline_posts:
        email_hash = hashlib.md5(post['email'].strip().lower().encode('utf-8')).hexdigest()
        post['gravatar'] = f"https://www.gravatar.com/avatar/{email_hash}?s=50&d=identicon"
        
    return render_template('timeline.html', title="Timeline", timeline_posts=timeline_posts)
