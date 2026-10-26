from fastapi import FastAPI

app = FastAPI(title="Copiloto de Operações")

@app.get("/health")
def health():
    return {"status": "ok"}