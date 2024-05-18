run:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py flush --noinput
	python manage.py loaddata initdb.json