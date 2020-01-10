from postgres import Postgres
from random import randint

db = Postgres("postgres://postgres:password@x.x.x.x:5432/tutorial")

for i in range(100000000000):
    print(db.run("INSERT INTO conditions(time, location, temperature, humidity) VALUES (NOW(), 'office', " + str(float(randint(0, 100))) + ", " + str(float(randint(0, 100))) + ")"))
