from typing import Optional
import fastapi
import uvicorn

# Init the API
api = fastapi.FastAPI()


# The home page
@api.get('/')
def index():
    body = "<html>" \
           "<body style='padding: 10px;'>" \
           "<h1>Welcome to the API</h1>" \
           "<div>" \
           "Try it: <a href='/api/calculate?x=7&y=11'>/api/calculate?x=7&y=11</a>" \
           "</div>" \
           "</body>" \
           "</html>"
    return fastapi.responses.HTMLResponse(content=body)

# The calculate api endpoint


@api.get('/api/calculate')
def calculate(x: int, y: int, z: Optional[int] = None):
    # Check if z is Zero and return an error
    if z == 0:
        return fastapi.responses.JSONResponse(content={"error": "ERROR: Z cannot be zero."},
                                              status_code=400)

    value = (x+y)
    if z is not None:
        value /= z
    return{
        'value': value
    }


# Run the server with specific port
uvicorn.run(api, port=8005, host="127.0.0.1")
