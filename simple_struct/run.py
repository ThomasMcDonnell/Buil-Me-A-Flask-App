from app import app, db
from app.models import *

@app.shell_context_processor
def make_shell_context():
    return dict(db=db)
