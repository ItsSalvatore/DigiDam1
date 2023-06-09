from flask import Flask, render_template, request, jsonify
from models import db, Medewerkers_rol, Medewerkers
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
        "sm" : Medewerkers_rol.query.filter_by(rol_id='1').count(),
        "ac" : Medewerkers_rol.query.filter_by(rol_id='2').count(),
        "po" : Medewerkers_rol.query.filter_by(rol_id='3').count(),
        "pgm" : Medewerkers_rol.query.filter_by(rol_id='4').count(),
        "rte" : Medewerkers_rol.query.filter_by(rol_id='5').count(),
        "ate" : Medewerkers_rol.query.filter_by(rol_id='6').count(),
        "pjm" : Medewerkers_rol.query.filter_by(rol_id='7').count(),
        "pmo" : Medewerkers_rol.query.filter_by(rol_id='8').count(),
        "totaal" : Medewerkers_rol.query.count(),
        "totaalmedewerkers": Medewerkers.query.count()
    }

    opdrachten = get_allopdracht()
    count_list = {}
    # kijk naar alle opdrachten
    for opdracht in opdrachten:
        year1 = opdracht[3].year
        # check of begindatum/beginjaar al in de dictionary zit
        if year1 not in count_list:
            # zo nee, voeg toe
            count_list[year1] = 1
        else: 
            # zo ja, verhoog waarde met 1
            count_list[year1] = count_list[year1] + 1


    # Krijg alle rollen vanuit database
    scrummasters = get_scrummasters()
    agilecoaches = get_agilecoaches()
    productowners = get_productowners()
    rte = get_rte()
    ate = get_ate()
    pjm = get_pjm()
    pmo = get_pmo()
    pgm = get_pgm()

    return render_template('index.html', opdrachten=count_list, agilecoaches=agilecoaches, productowners=productowners, rte=rte, ate=ate, pjm=pjm, pmo=pmo, pgm=pgm, data=data, scrummasters=scrummasters, )

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


# functie om alle opdrachten ooit uit de database te halen
def get_allopdracht():
    query = """SELECT *
               FROM opdracht
               WHERE einddatum BETWEEN '2020-01-01' AND '2027-12-31' 
               AND startdatum BETWEEN '2020-01-01' AND '2027-12-31'
               ORDER BY startdatum, einddatum
             """
    result = db.session.execute(query)
    return result.all()

# Voorspellingen filter query
@app.route('/voorspellingen')
def view_voorspellingen():
    data = {
        "sm" : Medewerkers_rol.query.filter_by(rol_id='1').count(),
        "ac" : Medewerkers_rol.query.filter_by(rol_id='2').count(),
        "po" : Medewerkers_rol.query.filter_by(rol_id='3').count(),
        "pgm" : Medewerkers_rol.query.filter_by(rol_id='4').count(),
        "rte" : Medewerkers_rol.query.filter_by(rol_id='5').count(),
        "ate" : Medewerkers_rol.query.filter_by(rol_id='6').count(),
        "pjm" : Medewerkers_rol.query.filter_by(rol_id='7').count(),
        "pmo" : Medewerkers_rol.query.filter_by(rol_id='8').count(),
        "totaal" : Medewerkers_rol.query.count(),
        "totaalmedewerkers": Medewerkers.query.count()
    }
    return render_template('voorspellingen.html', data = data)

# handleiding pagina
@app.route('/handleiding')
def view_handleiding():
    return render_template('handleiding.html')