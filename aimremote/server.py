from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

async def up(host, port):
    print(host, port)
    config = uvicorn.Config(
            app,
            host=host,
            port=port,
            lifespan="off",
            access_log=False)
    server = uvicorn.Server(config=config)
    #server.install_signal_handlers = lambda: None
    await server.serve()
