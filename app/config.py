import os

# MongoDB Configuration
MONGO_HOST = os.getenv("MONGO_HOST", "localhost")  # Default to local MongoDB
MONGO_PORT = os.getenv("MONGO_PORT", "27017")  # Default MongoDB port
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "quiz_db")  # Database name

# MongoDB Connection URI
MONGO_URI = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB_NAME}"
