from fastapi import FastAPI
from fastapi.responses import FileResponse
from controllers.AuthenticationController import router
from controllers.GiftCardBuyingController import gift_card_buying_router

app = FastAPI()

app.include_router(router)
app.include_router(gift_card_buying_router)


# setting up the favicon
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("favicon.ico")