from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from db_models import Base, Weapon
from api_models import WeaponModel

app = FastAPI()

# Start database session with bindings
engine = create_engine("sqlite:///./ds3_weapons.db")
Base.metadata.create_all(engine)

# Dependency for database session
def get_db():
	db = Session(engine)
	try:
		yield db
	finally:
		db.close()

@app.get("/weapons")
async def get_weapons(db: Session = Depends(get_db)):
	results = db.query(Weapon).filter().all()
	return results

@app.post("/weapons")
async def post_weapon(weapon:WeaponModel, db:Session=Depends(get_db)):
	orm_weapon = Weapon(**weapon.dict())
	results = db.add(orm_weapon)
	db.commit()
	return {'message': 'success :)'}

@app.patch("/weapons/{weapon_id}")
async def patch_weapon_name(weapon_id: int, name: str, db:Session=Depends(get_db)):
	weapon = db.query(Weapon).filter(Weapon.id == weapon_id).first()
	if weapon is None:
		raise HTTPException(status_code=400,detail="Weapon not found.")
	
	old_name = weapon.name

	db.query(Weapon).filter(Weapon.id == weapon_id).update({"name": name})
	db.commit()

	return {"message":f'"{old_name}" updated to "{name}" successfully.'}
