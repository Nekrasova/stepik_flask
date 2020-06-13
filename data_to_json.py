import json
import static.data as data

with open('static/teachers.json', 'w') as f:
    json.dump(data.teachers, f, indent=4)
    f.close()

with open('static/goals.json', 'w') as f:
    json.dump(data.goals, f, indent=4)
    f.close()