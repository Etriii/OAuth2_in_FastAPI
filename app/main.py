from fastapi import FastAPI, APIRouter
from fastapi.responses import HTMLResponse
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from app.db import create_db_and_tables


from app.routers import (
    auth_route,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Connecting to DB...")
    try:
        create_db_and_tables()
        print("Tables created.")
    except Exception as e:
        print(f"Failed to create DB tables: {e}")

    yield

    print("Disconnecting from DB...")


version = "v1"

app = FastAPI(
    lifespan=lifespan, title="API NP", description="An API for Secret", version=version
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>API Landing Page</title>
            <style>
                body { background-color: #f4f4f9; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; font-family: Arial, sans-serif; } .container { text-align: center; background-color: white; padding: 40px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); } 
                h1 { margin-bottom: 10px; color: #333; } p { margin-bottom: 20px; color: #555; } a { display: inline-block; margin: 0 10px; padding: 10px 20px; background-color: #007bff; color: white; text-decoration: none; border-radius: 6px; transition: background-color 0.3s ease; } a:hover { background-color: #0056b3; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Welcome to API NP</h1>
                <p>Use the links below to access the API documentation:</p>
                <a href="/docs">Swagger Docs</a>
                <a href="/redoc">Redoc</a>
            </div>
        </body>
    </html>
    """


router = APIRouter()

app.include_router(router)
app.include_router(auth_route.router, prefix=f"/api/{version}")
