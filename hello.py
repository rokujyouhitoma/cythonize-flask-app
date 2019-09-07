from vibora import Vibora, Response

app = Vibora()

@app.route('/')
async def hello():
    return Response(b'Hello World')
