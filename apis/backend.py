import uvicorn
from settings import Settings
from fastapi import FastAPI
app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

if __name__ == '__main__':
    try:
        uvicorn.run(app=app, host=str(Settings().get('host')), port=int(Settings().get('port')))
    except Exception as e:
        print(e)