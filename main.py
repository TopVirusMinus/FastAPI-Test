from fastapi import FastAPI
import uuid
from pydantic import BaseModel


class Log(BaseModel):
    message : str

app = FastAPI()

logs = [
        {"id":"5d58449d-092f-4096-8f78-a810d0179653", "message": "saba7 el gamal"}
    ]

@app.get("/getLogs")
async def getLogs():
    return logs

@app.get("/getLogs/{log_id}")
async def getLog(log_id: str):
    for log in logs:
        if log.get("id") == log_id:
            return log  
        
@app.post("/addLog", status_code=201)
async def addLog(message):
    newLog = {}
    newLog["id"] = uuid.uuid4()
    newLog["message"] = message
    
    logs.append(newLog)
    return newLog

@app.delete("/deleteLog/{log_id}", status_code=204)
async def deleteLog(log_id):
    for log in logs:
        if log.get("id") == log_id:
            logs.remove(log)
            return 
        
@app.put("/updateLog/{log_id}")
async def updateLog(log_id: str, newMessage: Log):
     for log in logs:
            if log.get("id") == log_id:
                log["message"] = newMessage
            return