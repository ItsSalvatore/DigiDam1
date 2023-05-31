from flask import Flask, render_template, request, jsonify
from models import db, Medewerkers_rol
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://kromhov:5/nwWCUEFqokge@oege.ie.hva.nl/zkromhov'
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
         'pool_recycle': 280,
         'pool_pre_ping': True,
         'connect_args' : {'ssl': {'fake_flag_to_enable_tls': True}}
     }

db.init_app(app)

@app.route('/')
def view_scrummasters():
    data = {
        "scrummasters" : Medewerkers_rol.query.filter_by(rol_id='1').count(),
        "AC" : Medewerkers_rol.query.filter_by(rol_id='2').count(),
        "AM" : Medewerkers_rol.query.filter_by(rol_id='7').count(),
        "PJ" : Medewerkers_rol.query.filter_by(rol_id='6').count(),
        "PO" : Medewerkers_rol.query.filter_by(rol_id='3').count(),
        "RTE" : Medewerkers_rol.query.filter_by(rol_id='4').count()
    }

    totaalRollen = {
        "smTotal" : {
            2020: 35,
            2021: 40,
            2022: 50,
            2023: 25,
            2024: 35,
            2025: 40,
            2026: 45,
            2027: 45,
        },
        "acTotal" : {
            2020: 2,
            2021: 3,
            2022: 2,
            2023: 4,
            2024: 5,
            2025: 10,
            2026: 15,
            2027: 15,
        },
        "poTotal" : {
            2020: 10,
            2021: 10,
            2022: 10,
            2023: 10,
            2024: 10,
            2025: 10,
            2026: 10,
            2027: 10,
        },
        "rteTotal" : {
            2020: 4,
            2021: 4,
            2022: 4,
            2023: 4,
            2024: 4,
            2025: 4,
            2026: 4,
            2027: 4,
        },
        "ateTotal" : {
            2020: 7,
            2021: 7,
            2022: 7,
            2023: 7,
            2024: 7,
            2025: 7,
            2026: 7,
            2027: 7,
        },
        "pjmTotal" : {
            2020: 200,
            2021: 150,
            2022: 130,
            2023: 100,
            2024: 110,
            2025: 90,
            2026: 70,
            2027: 60,
        },
        "pmoTotal" : {
            2020: 11,
            2021: 11,
            2022: 11,
            2023: 11,
            2024: 11,
            2025: 11,
            2026: 11,
            2027: 11,
        },
        "pgmTotal" : {
            2020: 12,
            2021: 12,
            2022: 13,
            2023: 14,
            2024: 12,
            2025: 12,
            2026: 12,
            2027: 12,
        }


    }
    print(totaalRollen)
    scrummasters = get_scrummasters()
    agilecoaches = get_agilecoaches()
    productowners = get_productowners()
    rte = get_rte()
    ate = get_ate()
    pjm = get_pjm()
    pmo = get_pmo()
    pgm = get_pgm()

    return render_template('index.html',totaalRollen=totaalRollen, agilecoaches=agilecoaches, productowners=productowners, rte=rte, ate=ate, pjm=pjm, pmo=pmo, pgm=pgm, data=data, scrummasters=scrummasters)

# definitieve test.

# functie om het aantal scrummasters op te halen
def get_scrummasters():
    query = """SELECT *
               FROM medewerkers
               WHERE startdatum_contract BETWEEN '1980-01-01' AND '2027-12-31'
               AND id IN (SELECT medewerker_id
                           FROM medewerkers_has_rol
                           WHERE rol_id = (SELECT id
                                           FROM rol
                                           WHERE rolnaam = 'SM'))"""
    
    result = db.session.execute(query)
    return result.all()

# functie om het aantal agile coaches op te halen
def get_agilecoaches():
    query = """SELECT *
               FROM medewerkers
               WHERE startdatum_contract BETWEEN '1980-01-01' AND '2027-12-31'
               AND id IN (SELECT medewerker_id
                           FROM medewerkers_has_rol
                           WHERE rol_id = (SELECT id
                                           FROM rol
                                           WHERE rolnaam = 'AC'))"""
    
    result = db.session.execute(query)
    return result.all()

# functie om het aantal PRODUCTOWNERS op te halen
def get_productowners():
    query = """SELECT *
               FROM medewerkers
               WHERE startdatum_contract BETWEEN '1980-01-01' AND '2027-12-31'
               AND id IN (SELECT medewerker_id
                           FROM medewerkers_has_rol
                           WHERE rol_id = (SELECT id
                                           FROM rol
                                           WHERE rolnaam = 'PO'))"""
    
    result = db.session.execute(query)
    return result.all()

# functie om het aantal rte op te halen
def get_rte():
    query = """SELECT *
               FROM medewerkers
               WHERE startdatum_contract BETWEEN '1980-01-01' AND '2027-12-31'
               AND id IN (SELECT medewerker_id
                           FROM medewerkers_has_rol
                           WHERE rol_id = (SELECT id
                                           FROM rol
                                           WHERE rolnaam = 'RTE'))"""
    
    result = db.session.execute(query)
    return result.all()

# functie om het aantal ate op te halen
def get_ate():
    query = """SELECT *
               FROM medewerkers
               WHERE startdatum_contract BETWEEN '1980-01-01' AND '2027-12-31'
               AND id IN (SELECT medewerker_id
                           FROM medewerkers_has_rol
                           WHERE rol_id = (SELECT id
                                           FROM rol
                                           WHERE rolnaam = 'ATE'))"""
    
    result = db.session.execute(query)
    return result.all()

# functie om het aantal project managers op te halen
def get_pjm():
    query = """SELECT *
               FROM medewerkers
               WHERE startdatum_contract BETWEEN '1980-01-01' AND '2027-12-31'
               AND id IN (SELECT medewerker_id
                           FROM medewerkers_has_rol
                           WHERE rol_id = (SELECT id
                                           FROM rol
                                           WHERE rolnaam = 'PJM'))"""
    
    result = db.session.execute(query)
    return result.all()

# functie om het aantal PGM in 2019 op te halen
def get_pgm():
    query = """SELECT *
               FROM medewerkers
               WHERE startdatum_contract BETWEEN '1980-01-01' AND '2027-12-31'
               AND id IN (SELECT medewerker_id
                           FROM medewerkers_has_rol
                           WHERE rol_id = (SELECT id
                                           FROM rol
                                           WHERE rolnaam = 'PGM'))"""
    
    result = db.session.execute(query)
    return result.all()

# functie om het aantal PMO in 2019 op te halen
def get_pmo():
    query = """SELECT *
               FROM medewerkers
               WHERE startdatum_contract BETWEEN '1980-01-01' AND '2027-12-31'
               AND id IN (SELECT medewerker_id
                           FROM medewerkers_has_rol
                           WHERE rol_id = (SELECT id
                                           FROM rol
                                           WHERE rolnaam = 'PMO'))"""
    
    result = db.session.execute(query)
    return result.all()

# route voor de indexpagina

# eind definitieve test.


@app.route('/users')
def view_users():
    data = {
        "scrummasters" : Medewerkers_rol.query.filter_by(rol_id='1').count(),
        "AC" : Medewerkers_rol.query.filter_by(rol_id='2').count(),
        "AM" : Medewerkers_rol.query.filter_by(rol_id='7').count(),
        "PJ" : Medewerkers_rol.query.filter_by(rol_id='6').count(),
        "PO" : Medewerkers_rol.query.filter_by(rol_id='3').count(),
        "RTE" : Medewerkers_rol.query.filter_by(rol_id='4').count()
    }
    return render_template('userlist.html', data = data)

@app.route('/voorspellingen')
def view_voorspellingen():
    data = {
        "scrummasters" : Medewerkers_rol.query.filter_by(rol_id='1').count(),
        "ac" : Medewerkers_rol.query.filter_by(rol_id='2').count(),
        "am" : Medewerkers_rol.query.filter_by(rol_id='7').count(),
        "pjmgr" : Medewerkers_rol.query.filter_by(rol_id='6').count(),
        "po" : Medewerkers_rol.query.filter_by(rol_id='3').count(),
        "rte" : Medewerkers_rol.query.filter_by(rol_id='4').count(),
        "totaal" : Medewerkers_rol.query.count()
    }
    return render_template('voorspellingen.html', data = data)