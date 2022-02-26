from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database"""

    db.app = app
    db.init_app(app)



class Pet(db.Model):
    """Pets potentially available for adoption"""

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.Text, nullable = False)
    species = db.Column(db.Text, nullable = False)
    photo_url = db.Column(db.Text, default="https://its.fsu.edu/sites/g/files/upcbnu1011/files/ITS%20Website/no-image-available.png")
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable = False, default = True)

    def __repr__(self):
        return f"<Pet name={self.name} species={self.species} age={self.age} photo_url={self.photo_url} age={self.age} notes={self.notes} available={self.available}>"


