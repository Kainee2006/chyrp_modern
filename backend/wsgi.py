# wsgi.py
from app import create_app
import os

app = create_app()

if __name__ == "__main__":
    # Get the port from Railway's environment variable
    port = int(os.environ.get("PORT", 5000))
    # Don't specify host - Railway handles this
    app.run(port=port)
