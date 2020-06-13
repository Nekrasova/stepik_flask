## Stepik Flask Week 3
------          
### Project Description
This project is aimed creating a website, where people can find an English teacher given specific goal and time available for study.

### Main rules     
1) Currently the database for this website is presented by json files, such as `static/request.json` and `static/booking.json`. These files contain the information
received after the web visitor has fulfilled and submitted one of the two available forms:
* Make a request for finding a suitable teacher
* Make a booking within the available timeslots for a specific teacher

2) The input data is also stored in json files, such as `static/teachers.json` and `static/goals.json` that are generated from `static/data.py`file.

3) There is only 1 static picture that is stored as `static/other.png` and represents a picture for the `other` tab goal that was not there from the beginning.

4) The rest of the sample pictures (apart from `static/check.png`) have been deleted and replated by the picture that were listed in the data.py file.

### How to run this project

1) If you want to test the general functionality of the website, you do not need to do anything else, just go to [herokuapp](stepik-flask-petrova-week-3.herokuapp.com)
and test whatever you want.

2) If you want to test the json data base maintanance, please do the following:
* Delete these following files:<br>
  ** `static/booking.json`<br>
  ** `static/request.json`<br>
  ** `static/teachers.json`<br>
  ** `static/goals.json`<br>
* Run first the data_to_json.py file to recreate the input json data( `static/teachers.json` and `static/goals.json`)
* Run app.py file to test the recreation of the output json data (`static/booking.json` and `static/request.json`) 
* Check that every time you fill out the form, it is stored without being overwritten in one of these files (depending on the initial web page
where you fill out the form (booking.html or request.html)

### Have fun!
