from pydantic import BaseModel

class WeaponModel(BaseModel):
    name: str
    category: str
    reinforcement: str

    class Config:
        orm_mode = True