from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_models import Base, Weapon
import pandas as pd

df = pd.read_csv('./DS3_weapon.csv')

engine = create_engine('sqlite:///ds3_weapons.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

for index,row in df.iterrows():
    name = row['Name']
    category = row['Category']
    reinforcement = row['Reinforcement']
    weapon = Weapon(name=name, category=category, reinforcement=reinforcement)
    session.add(weapon)

session.commit()