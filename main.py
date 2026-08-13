from fastapi import FastAPI
from fastapi.responses import FileResponse
from controllers.AuthenticationController import router

app = FastAPI()

app.include_router(router)


# setting up the favicon
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("favicon.ico")