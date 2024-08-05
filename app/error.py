from app import app


@app.errorhandler(404)
def error404(e):
    return 'Error 404'