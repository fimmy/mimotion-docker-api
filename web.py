from typing import Optional

from fastapi import FastAPI

from main import main as setStep

app = FastAPI()


@app.get("/set-step")
async def set_step(user,password,step):
    print()
    result=setStep(user,password,step)
    return {
        "message":result
        }
