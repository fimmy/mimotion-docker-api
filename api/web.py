import random
from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from main import main as setStep

app = FastAPI(
    title="小米运动改步数API"
)
@app.get("/set-step")
async def set_step(user,password,step):
    result=setStep(user,password,step)
    return {
        "code":result[0],
        "message":result[1]
        }
@app.get("/set-step-random")
async def set_step(user,password,min:int,max:int):
    step = random.randint(min,max)
    result=setStep(user,password,step)
    return {
        "code":result[0],
        "message":result[1],
        "step":step
        }
