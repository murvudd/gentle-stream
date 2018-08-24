python manage.py makemessages -l pl
python manage.py compilemessages -l pl
python manage.py makemigrations
heroku run python manage.py migrate
echo ""
git status
echo ""
git add .
git commit -m "automated push"
git push heroku master
git push origin master

heroku open
