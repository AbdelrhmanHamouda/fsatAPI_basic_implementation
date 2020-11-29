from typing import Optional
import fastapi
import uvicorn

# Init the API
api = fastapi.FastAPI()


@api.get('/api/calculate')
def calculate(x: int, y: int, z: Optional[int] = None):
    # Check if z is Zero and return an error
    if z == 0:
        return fastapi.Response(content='{"error":"ERROR: Z cannot be zero."}',
                                media_type="application/json",
                                status_code=400)
    value = (x+y)
    if z is not None:
        value /= z
    return{
        'value': value
    }


# Run the server with specific port
uvicorn.run(api, port=8005, host="127.0.0.1")
