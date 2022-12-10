from fastapi import FastAPI

app = FastAPI(title="Trabalho Pratico 01")

# metodo get / all models-user
@app.get('/')
async def raiz():
    return {'message': 'Trabalho Pratico 01'}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="info") 