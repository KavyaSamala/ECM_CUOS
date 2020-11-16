import csv
from decouple import config

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(config("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


def main():
    f = open("control_units.csv")
    reader = csv.reader(f)
    for control_unit in reader:
        db.execute("INSERT INTO control_units (control_unit) VALUES (:control_unit)", {"control_unit": control_unit})
        print(f"Added control unit {control_unit}.")
    db.commit()


if __name__ == "__main__":
    main()
