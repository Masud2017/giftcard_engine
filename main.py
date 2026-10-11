from fastapi import FastAPI
from fastapi.responses import FileResponse
from controllers.AuthenticationController import router
from controllers.GiftCardBuyingController import gift_card_buying_router

from middlewares.AuthenticationMiddleware import AuthenticationMiddleware

app = FastAPI()

# Attaching all the router together
app.include_router(router)
app.include_router(gift_card_buying_router)

# Attaching all the middlewares together
app.add_middleware(AuthenticationMiddleware)

# setting up the favicon
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("favicon.ico")