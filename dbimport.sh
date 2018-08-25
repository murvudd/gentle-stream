
dropdb mylocalcopy
heroku pg:pull DATABASE mylocalcopy
python run ~/PycharmProjects/spotipy/main.py copy_db

