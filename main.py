from typing import Optional
import fastapi
import uvicorn

# Init the API
api = fastapi.FastAPI()


@api.get('/api/calculate')
def calculate(x: int, y: int, z: Optional[int] = None):
    value = (x+y)*z
    return{
        'value': value
    }


# Run the server with specific port
uvicorn.run(api, port=8005, host="127.0.0.1")
