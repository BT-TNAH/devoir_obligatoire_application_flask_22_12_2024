import requests
from ..app import app
from flask import render_template
 
def fetch_wikidata(params):
    url = 'https://www.wikidata.org/w/api.php'
    try:
        return requests.get(url, params=params)
    except:
        return "Aucune donnée valide n'a été retournée pour l'ID."
    
@app.route("/")
def accueil():
    return render_template("pages/accueil.html")

@app.route("/retrieve_wikidata/<string:id>")
def retrieve_wikidata(id:str):
    identifiant = id
    params = {
                'action': 'wbgetentities',
                'ids': identifiant,
                'format': 'json',
                'languages': 'en'
            }
    data = fetch_wikidata(params)
    data = data.json()
    return render_template("pages/wikidata_fichier.html", id=identifiant, data_json=data)