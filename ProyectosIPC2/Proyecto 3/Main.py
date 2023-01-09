from backend.app import app
from backend.app import Update_database
if __name__ == "__main__":
    Update_database()
    app.run(port=4000)