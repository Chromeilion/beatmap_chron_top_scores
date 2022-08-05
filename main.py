from ossapi import Ossapi

api_key = None
beatmap_id = None


mods = [0, 64, 1024, 16, 8, 8+64, 8+16]

api = Ossapi(api_key)

all_scores = []

for i in mods:
    all_scores.append(api.get_scores(beatmap_id=beatmap_id, mods=i))

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
        top_scores.append(i)
        current_top = i.score


for i in top_scores:
    print("username:", i.username)
    print("date::", i.date, "\n")
