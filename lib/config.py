from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Database setup
DATABASE_URL = "sqlite:///task_manager.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# Create tables in the database
Base.metadata.create_all(engine)
