from sanic import Sanic, json
import backend


app = Sanic("SimpleAPI")
rows = []
HOST = "localhost"
PORT = 8000


@app.post("/getbeatmap")
async def get_rows(request):
    return json(backend.top_scores(beatmap_id=int(request.json["beatmap_id"])))

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)
