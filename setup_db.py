from models import Base, engine

# This script creates the database tables
Base.metadata.create_all(engine)
print("Tables created successfully.")