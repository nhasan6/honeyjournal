from fastapi import FastAPI 
from routes import honey, auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(honey.router)
app.include_router(auth.router)

@app.get('/')
def home():
    return {
        "message" : "we are in the home page"
    }