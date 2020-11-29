import fastapi
import uvicorn

# Init the API
api = fastapi.FastAPI()


@api.get('/api/calculate')
def calculate():
    value = 2+2
    return{
        'value': value
    }


# Run the server with specific port
uvicorn.run(api, port=8005, host="127.0.0.1")
