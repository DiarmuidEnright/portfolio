import os
from flask import Flask, render_template
from dotenv import load_dotenv

from . import data

load_dotenv()
app = Flask(__name__)

# Registry of pages shown in the dynamic nav menu. Each entry maps a view
# function ("endpoint") to the label shown in the menu bar. Add a page here and
# the menu updates automatically — see base.html.
PAGES = [
    {"endpoint": "index", "label": "Home"},
]


@app.context_processor
def inject_globals():
    """Make these values available to every template automatically."""
    return {
        "pages": PAGES,
        "url": os.getenv("URL"),
        "about": data.ABOUT,
    }


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow")
