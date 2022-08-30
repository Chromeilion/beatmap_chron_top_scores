from sanic import Sanic, json
import osuapi
from dotenv import load_dotenv
import os
from sanic.exceptions import SanicException


load_dotenv()

# Set up everything from the given env variables
app = Sanic("SimpleAPI")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
api = osuapi.BeatmapAnal(os.getenv("API_KEY"))


@app.get("/getbeatmap")
async def get_rows(request):
    """
    Take a beatmap ID and return the top plays in chronological order.
    """
    try:
        beatmap_id = int(request.args["beatmap_id"][0])
        leaderboard = api.top_scores_chron(beatmap_id=beatmap_id)
        response = {"status": 200,
                    "data": {"scores": leaderboard}}
        return json(response)

    except KeyError or IndexError:
        raise SanicException("No beatmap_id argument provided",
                             status_code=400)

    except ValueError:
        raise SanicException("beatmap_id is not an integer",
                             status_code=400)

    except TimeoutError:
        raise SanicException("osu! API seems to be down", status_code=500)

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)
