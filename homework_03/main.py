from fastapi import FastAPI, status
import uvicorn

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello Index"}


@app.get(
    "/ping/",
    status_code=status.HTTP_200_OK,
)
def ping():
    return {"message": "pong"}


# if __name__ == '__main__':
#     uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8080)