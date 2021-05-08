docker-makemigrations:
	docker-compose exec web python manage.py makemigrations --noinput
docker-migrate:
	docker-compose exec web python manage.py migrate
docker-collectstatic:
	docker-compose exec web python manage.py collectstatic --no-input --clear
