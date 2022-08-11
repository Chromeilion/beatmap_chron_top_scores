from sanic import Sanic, json
import backend
from dotenv import load_dotenv
import os


load_dotenv()

# Set up everything from the given env variables
app = Sanic("SimpleAPI")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
analyzer = backend.beatmapanal(os.getenv("API_KEY"))


@app.post("/getbeatmap")
async def get_rows(request):
    """
    Take a beatmap ID and return the top plays in chronological order.
    """
    return json(analyzer.top_scores_chron(beatmap_id=int(request.json["beatmap_id"])))

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)
