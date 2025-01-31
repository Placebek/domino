import uvicorn

if __name__ == "__main__":
    # Замените host="0.0.0.0" на ваш IP-адрес, если хотите использовать конкретный IP
    # uvicorn.run("main:app", host="localhost", port=8000, reload=True)
    # uvicorn.run("main:app", host="192.168.34.31", port=8000, reload=True, ssl_keyfile="key.pem", ssl_certfile="cert.pem")   
    uvicorn.run("main:app", host="192.168.34.31", port=8000, reload=True)
    # uvicorn.run("main:app", host="192.168.237.182", port=8000, reload=True)ккЫ
