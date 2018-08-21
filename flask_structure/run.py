from app import app, db
from app.mpdels import *

@app.shell_context_processor
def make_shell_context():
    return dict(db=db)
