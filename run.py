from uvicorn.main import run


if __name__ == "__main__":
    from service.app import startup

    app = startup()
    run(app=app, host="0.0.0.0", port=8000)
