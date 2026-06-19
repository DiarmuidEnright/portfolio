import os
from flask import Flask, render_template
from dotenv import load_dotenv

from . import data

load_dotenv()
app = Flask(__name__)

PAGES = [
    {"endpoint": "index", "label": "Home"},
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
