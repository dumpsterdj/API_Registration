from db_config import Base, engine
from models import User

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
