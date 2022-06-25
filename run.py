from uvicorn.main import run


if __name__ == "__main__":
    from service.config import HOST, PORT 
    from service.app import startup

    app = startup()
    run(app=app, host=HOST, port=PORT)
