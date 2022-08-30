from ossapi import Ossapi
import signal


class BeatmapAnal:
    """
    Grab data for a beatmap and analyze it.
    """

    def __init__(self, api_key: str):
        self.api = Ossapi(api_key)
        # What mods to use, numbers come from
        # https://github.com/ppy/osu-api/wiki#mods For mod combinations,
        # just add them together
        self.mods = [0, 64, 1024, 16, 8, 8+64, 8+16]

    def top_scores_chron(self, beatmap_id: int):
        """
        Return all top scores in the order they happened.
        """
        # "All scores" is a list containing all known scores on the beatmap
        # across all leaderboards.
        all_scores = []

        for i in self.mods:
            with timeout(20):
                scores = self.api.get_scores(beatmap_id=beatmap_id, mods=i)

            all_scores.append(scores)

        all_scores_combined = []

        for i in all_scores:
            for j in i:
                all_scores_combined.append(j)

        all_scores_combined.sort(key=lambda x: x.date)

        top_scores = []
        current_top = 0

        for i in all_scores_combined:
            score = i.score
            if score >= current_top:
                top_scores.append({"username": str(i.username),
                                   "date": str(i.date),
                                   "score": str(i.score)})
                current_top = i.score

        return top_scores


class timeout:
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message

    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_message)

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)

    def __exit__(self, type, value, traceback):
        signal.alarm(0)
