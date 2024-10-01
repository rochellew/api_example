import requests
from api_models import BaseModel, WeaponModel

weapon = WeaponModel(name="Blasphemous Blade", category="Greatsword",reinforcement="Boss")
uri = "http://localhost:8000/weapons/"

# response = requests.post(url=uri, json=weapon.model_dump(mode='json'))
# response = requests.get(url=uri)
response = requests.patch(f'{uri}288/?name=The Blasphemous Blade')