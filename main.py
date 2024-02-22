from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response

from db.database import SessionLocal
from routers import router

app = FastAPI()

app.include_router(router)

# @app.middleware("http")
# async def db_session_middleware(request: Request, call_next):
#     response = Response("Internal server error", status_code=500)
#     try:
#         request.state.db = SessionLocal()
#         response = await call_next(request)
#     finally:
#         request.state.db.close()
#     return response



@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
