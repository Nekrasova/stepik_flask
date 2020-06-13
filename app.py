from flask import Flask, render_template, request
import json
import os
import random
import string

app = Flask(__name__)

goals = json.load(open("static/goals.json", "r"))
teachers = json.load(open("static/teachers.json", "r"))
days = {'mon': 'Понедельник',
        'tue': 'Вторник',
        'wed': 'Среда',
        'thu': 'Четверг',
        'fri': 'Пятница',
        'sat': 'Суббота',
        'sun': 'Воскресение'}

goals_pics = {'relocate': '🚜',
              'study': '🏫',
              'travel': '⛱',
              'work': '🏢',
              'programming': '‍💻',
              'other': '📮'
              }


@app.route('/')
def render_main():
    return render_template('index.html',
                           goals=goals,
                           goals_pics=goals_pics,
                           teachers=random.sample(teachers, k=6))


@app.route('/teachers/')
def render_teachers():
    sorted_teachers = sorted(list([x for x in teachers]), key=lambda i: i['rating'], reverse=True)
    return render_template('teachers.html',
                           goals=goals,
                           goals_pics=goals_pics,
                           teachers=sorted(list([x for x in sorted_teachers]), key=lambda i: i['price'], reverse=True)
                           )


@app.route('/goals/<id_goal>')
def render_goal(id_goal):
    sorted_teachers = sorted(list([x for x in teachers if id_goal in x['goals']]), key=lambda i: i['rating'],
                             reverse=True)
    if id_goal in goals.keys():
        return render_template('goal.html',
                               id_goal=id_goal,
                               goals_pics=goals_pics,
                               goal=goals[id_goal],
                               goal_picture='../static/' + id_goal + '.png',
                               teachers=sorted(list([x for x in sorted_teachers]), key=lambda i: i['price'],
                                               reverse=True)
                               )

    else:
        return '404 Not Found', 404


@app.route('/profiles/<int:id_teacher>/')
def render_profile(id_teacher):
    id_teacher = id_teacher
    teacher_schedule = teachers[id_teacher]['free']
    sch = {}
    for day in teacher_schedule.keys():
        hours = [teacher_schedule[x] for x in teacher_schedule if x == day][0]
        if len(list([y for y in hours if hours[y] == True])) == 0:
            sch.update({day: 'No classes'})
        else:
            sch.update({day: list([y for y in hours if hours[y] == True])})
    if id_teacher in range(len(teachers)):
        return render_template('profile.html',
                               goals=goals,
                               days=days,
                               teacher_schedule=teacher_schedule,
                               id_teacher=id_teacher,
                               teacher_name=teachers[id_teacher]['name'],
                               teacher_goals=teachers[id_teacher]['goals'],
                               teacher_rating=teachers[id_teacher]['rating'],
                               teacher_price=teachers[id_teacher]['price'],
                               teacher_picture=teachers[id_teacher]['picture'],
                               teacher_about=teachers[id_teacher]['about']
                               )
    else:
        return '404 Not Found', 404


@app.route('/request/')
def render_request():
    return render_template('request.html')


@app.route('/request_done/', methods=['POST'])
def render_request_done():
    clientName = request.form.get("clientName")
    clientPhone = request.form.get("clientPhone")
    if len(clientName) == 0 or len(clientPhone) == 0:
        return 'Name and phone cannot be empty!'
    elif len(clientName) <= 1 or not clientPhone.translate({ord(c): None for c in string.whitespace}).isnumeric():
        return 'Please check that your name contains at least 2 characters, and that your phone number contains ' \
               'only digits and no characters!'
    else:
        if not os.path.isfile("static/request.json"):
            with open("static/request.json", 'w') as outfile:
                outfile.write(str(list()))
            with open("static/request.json", "r+") as file:
                data = json.load(file)
                data.append(request.form)
                file.seek(0)
                json.dump(data, file)
        else:
            with open("static/request.json", "r+") as file:
                data = json.load(file)
                data.append(request.form)
                file.seek(0)
                json.dump(data, file)
            return render_template('request_done.html',
                                   clientName=request.form.get("clientName"),
                                   clientPhone=request.form.get("clientPhone"),
                                   clientGoal=goals[request.form.get("goal")],
                                   clientTime=request.form.get("time")
                                   )


@app.route('/booking/<int:id_teacher>/<id_week_day>/<time>/')
def render_booking(id_teacher, id_week_day, time):
    id_teacher = teachers[id_teacher]['id']
    return render_template('booking.html',
                           hour=time,
                           id_week_day=id_week_day,
                           id_teacher=id_teacher,
                           teacher_name=teachers[id_teacher]['name'],
                           teacher_picture=teachers[id_teacher]['picture'],
                           days=days
                           )


@app.route('/booking_done/', methods=['POST'])
def render_booking_done():
    clientName = request.form.get("clientName")
    clientPhone = request.form.get("clientPhone")
    if len(clientName) == 0 or len(clientPhone) == 0:
        return 'Name and phone cannot be empty!'
    elif len(clientName) <= 1 or not clientPhone.translate({ord(c): None for c in string.whitespace}).isnumeric():
        return 'Please check that your name contains at least 2 characters, and that your phone number contains ' \
               'only digits and no characters!'
    else:
        if not os.path.isfile("static/booking.json"):
            with open("static/booking.json", 'w') as outfile:
                outfile.write(str(list()))
            with open("static/booking.json", "r+") as file:
                data = json.load(file)
                data.append(request.form)
                file.seek(0)
                json.dump(data, file)
        else:
            with open("static/booking.json", "r+") as file:
                data = json.load(file)
                data.append(request.form)
                file.seek(0)
                json.dump(data, file)
        return render_template('booking_done.html',
                               clientWeekday=request.form.get("clientWeekday"),
                               clientTime=request.form.get("clientTime"),
                               clientName=request.form.get("clientName"),
                               clientPhone=request.form.get("clientPhone"),
                               clientTeacher=request.form.get("clientTeacher")
                               )


if __name__ == '__main__':
    app.run(debug=True)
