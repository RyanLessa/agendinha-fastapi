from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from nova_api.routes.tasks import router as tasks_router
from nova_api.routes.users import router as users_router

app = FastAPI()

app.include_router(tasks_router, prefix='/tasks')
app.include_router(users_router, prefix='/users')

@app.get("/check")
def check():
    return HTMLResponse('<p>Working</p>')
