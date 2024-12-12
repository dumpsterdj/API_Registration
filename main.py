from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from db_config import Base, engine
from endpoints import auth

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Mount static files and set up templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.get("/")
def home():
    return templates.TemplateResponse("home.html", {"request": {}})
