import pickle
from types import SimpleNamespace

import uvicorn
from aim import Run as AimRun
from aim import Image as AimImage
from aim import Distribution as AimDistribution
from fastapi import FastAPI, Request

app = FastAPI()

run_cache = dict()
global_security_token = ''

def get_run(experiment: str, repo: str, run_hash: str, security_token: str):
    if security_token != global_security_token:
        raise Exception('Wrong token')
    if not run_hash in run_cache:
        run_cache[run_hash] = AimRun(
            repo=repo,
            experiment=experiment,
            run_hash=run_hash,
            system_tracking_interval = None
        )
    return run_cache[run_hash]

def aim_track(run, item):
    data = item.data
    if hasattr(data, 'distribution'):
        data = AimDistribution(data.distribution)
    if hasattr(data, 'image'):
        data = AimImage(data.image)
    run.track(data,
        name=item.name,
        step=item.step,
        epoch=item.epoch,
        context=item.context)

@app.get("/aimremote/get_values/{name}")
async def get_values(name: str, repo: str, run_hash: str, security_token: str, experiment: str = ''):
    run = get_run(experiment, repo, run_hash, security_token)
    return run[name]

@app.post("/aimremote/set_values/{name}")
async def get_values(request: Request, name: str, repo: str, run_hash: str, security_token: str, experiment: str = ''):
    run = get_run(experiment, repo, run_hash, security_token)
    run[name] = await request.json()

@app.post("/aimremote/track")
async def track(request: Request, repo: str, run_hash: str, security_token: str, experiment: str = ''):
    run = get_run(experiment, repo, run_hash, security_token)
    data: bytes = await request.body()
    items = pickle.loads(data)
    for item in items:
        aim_track(run, SimpleNamespace(**item))

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
