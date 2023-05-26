from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
    
class Medewerkers(db.Model):
    __tablename__ = "medewerkers"

    id = db.Column(db.Integer, primary_key = True)
    naam = db.Column(db.String(100))
    startdatum_contract = db.Column(db.Date())
    einddatum_contract = db.Column(db.Date())
    contract_soort = db.Column(db.String(100))

    def __init__(self, naam, startdatum_contract, einddatum_contract, contract_soort) -> None:
        self.naam = naam
        self.startdatum_contract = startdatum_contract
        self.einddatum_contract = einddatum_contract
        self.contract_soort = contract_soort

    def __repr__(self) -> str:
        return f"{self.naam}"
  
class Medewerkers_rol(db.Model):
    __tablename__ = "medewerkers_has_rol"

    id = db.Column(db.Integer, primary_key = True)
    medewerker_id = db.Column(db.Integer())
    rol_id = db.Column(db.Integer())

    def __init__(self, medewerker_id, rol_id):
        self.medewerker_id = medewerker_id
        self.rol_id = rol_id

    def __repr__(self):
        return f"{self.rol_id}"
    
