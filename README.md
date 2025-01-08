python manage.py runserver

mysql.server start

mysql -u root

use events

select * from event_eventconfig;

select * from event_createddate;

select * from event_date;

truncate table event_eventconfig;

truncate table event_createddate;

truncate table event_date;

poetry shell

python manage.py makemigrations event

python manage.py migrate
