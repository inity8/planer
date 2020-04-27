import os
from celery import Celery
from sqlalchemy import create_engine, MetaData, Table, select

NAME_sql = os.environ.get("POSTGRES_DB")
USER_sql = os.environ.get("POSTGRES_USER")
PASSWORD_sql = os.environ.get("POSTGRES_PASSWORD")
HOST_sql = os.environ.get("POSTGRES_HOST")
PORT_sql = os.environ.get("POSTGRES_PORT")

app = Celery(
    'fests', 
    broker = 'redis://redis:6379/0'
    )

app.conf.update(
    result_backend = 'redis://redis:6379/0'
    )



@app.task
def events():
	DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{USER_sql}:{PASSWORD_sql}@{HOST_sql}:{PORT_sql}/{NAME_sql}'
	engine = create_engine(DATABASE_CONNECTION_URI)
	connection = engine.connect()
	metadata = MetaData()
	myapp_event = Table('myapp_event', metadata, autoload=True, autoload_with=engine)
	myapp_remindtime = Table('myapp_remindtime', metadata, autoload=True, autoload_with=engine)

	query = select([myapp_event.join(myapp_remindtime, myapp_event.c.time_id==myapp_remindtime.c.id)])
	ResultProxy = connection.execute(query)
	ResultSet = ResultProxy.fetchall()
	return "Done"


app.conf.beat_schedule = {
    "fests-task": {
        "task": "fests.events",
        "schedule": 30.0,
   }
}

