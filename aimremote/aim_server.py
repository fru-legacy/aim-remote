from fastapi import FastAPI, Request
from aim import Run as AimRun
import uvicorn
import pickle

app = FastAPI()

run_cache = dict()
global_security_token = ''

def get_run(experiment: str, run_hash: str):
    if not run_hash in run_cache:
        run_cache[run_hash] = AimRun(
            repo='/home/administrator/tools',
            experiment=experiment,
            run_hash=run_hash,
            system_tracking_interval = None
        )
    return run_cache[run_hash]

@app.get("/aimremote/get_values/{name}")
async def get_values(name: str, run_hash: str, security_token: str, experiment: str = ''):
    if security_token != global_security_token:
        raise Exception('Wrong token')
    return get_run(experiment, run_hash)[name]

@app.post("/aimremote/set_values/{name}")
async def get_values(request: Request, name: str, run_hash: str, security_token: str, experiment: str = ''):
    if security_token != global_security_token:
        raise Exception('Wrong token')
    get_run(experiment, run_hash)[name] = await request.json()

@app.post("/aimremote/track")
async def track(request: Request, run_hash: str, security_token: str, experiment: str = ''):
    if security_token != global_security_token:
        raise Exception('Wrong token')
    data: bytes = await request.body()
    items = pickle.loads(data)
    run = get_run(experiment, run_hash)
    for item in items:
        run.track(
            item['data'],
            name=item['name'],
            step=item['step'],
            epoch=item['epoch'],
            context=item['context']
        )


async def up(host, port, security_token):
    global global_security_token
    global_security_token = security_token
    config = uvicorn.Config(
            app,
            host=host,
            port=port,
            lifespan="off",
            access_log=False)
    server = uvicorn.Server(config=config)
    await server.serve()
