""" Seed file to make sample data for database."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

dog = Pet(name="Kobe", species="Dog", photo_url="https://www.hepper.com/wp-content/uploads/2021/11/German-Shepherd-Chihuahua-mix.jpg", age=5, notes="friendly and energetic")
cat = Pet(name="Garfield", species="Cat", photo_url="https://i.ytimg.com/vi/Pg4CyEmCiP0/maxresdefault.jpg", age=1, notes="likes to scratch")
bird = Pet(name="Big Bird", species="Bird", photo_url="https://www.thesprucepets.com/thmb/V_YLRlAIKfTutBEzmSYwyEJP7OU=/1975x1518/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-597187685-58ad8e7a3df78c345b864b4f.jpg" ,age=1, notes="talks a lot")
fish = Pet(name="Nemo", species="Fish", photo_url="https://s3.amazonaws.com/BRSImages/brsVideoContent/8-25-21-finding-nemo-update/nemo-ocellaris-clownfish.jpg" ,age=1, notes="always hungry")
hamster = Pet(name="Hamtaro", species="Hamster", photo_url="https://squeaksandnibbles.com/wp-content/uploads/2019/11/Boy-Hamster-Names-150-Awesome-Ideas-SN-long.jpg" ,age=2, notes="loves running on the wheel")


db.session.add_all([dog, cat, bird, fish, hamster])
db.session.commit()

