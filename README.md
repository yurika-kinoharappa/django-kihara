python manage.py runserver

mysql.server start

mysql -u root

use events

poetry shell


2002-10-10 20:00 10:10


select * from event_eventconfig;

select * from event_createddate;

select * from event_date;


truncate table event_eventconfig;

truncate table event_createddate;

truncate table event_date;


python manage.py makemigrations event

python manage.py migrate




日付を複数登録
編集できる