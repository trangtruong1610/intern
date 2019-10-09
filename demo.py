import sqlalchemy as db

engine = db.create_engine('postgresql+psycopg2://postgres:trangtruong@localhost:5432/ggbenefits')
connection = engine.connect()
metadata = db.MetaData()
clinics = db.Table('clinics', metadata, autoload=True, autoload_with=engine)


query = db.select([clinics])
ResultProxy = connection.execute(query)
clinics_columns = ResultProxy.fetchall()

for i in clinics_columns:
    print(i)