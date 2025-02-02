from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

# write a fast api code which is post and accespts a single string and return a list of strings with response as StreamingResponse type
# the response should be a list of strings with each string being a character from the input string
# example input: "hello"
# example output: ["h", "e", "l", "l", "o"]
from fastapi.responses import StreamingResponse
import time

def stream():
    for char in "hello how are you guys! hello gow are you guys gello how ar you guys hello how are you guys hello how are you guys":
        time.sleep(5)
        #print(char)
        yield char

@app.get("/stream")
async def stream_response():
    return StreamingResponse(stream(), media_type='text/event-stream')

if(__name__ == "__main__"):
    import uvicorn
    uvicorn.run(app,host="localhost", port=8000)