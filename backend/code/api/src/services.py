import datetime
from typing import List
from .utils import predict
import uuid

HEADERS = {'Accept': 'application/json'}

def ReceipesService(data):
    """
    """
    print(data)
    print("In service post")
    list_ing = ' '.join(data["ingredients"])
    seed_text = list_ing
    max_sequence_len = 227
    predicted_receipies = predict(seed_text = seed_text, next_words=100,max_sequence_len= max_sequence_len)

    #call model

    #call model
   # url = "https://api.external.citymapper.com/api/1/directions/transit"
   # headers = {
   # 'Citymapper-Partner-Key': 'ELJjUBoCXSqxD4HSMRXDVDWttHRy5A68'}
   # paths_price,route_datas = get_min_prices(url,headers,path_data)
    
    response = """ soupe veloute potimarron pomme terre,45 min,4,4,2 pomme terre 2 oignon hache   3 gousse ail hache   10 cl creme frais   1 c.a.c curry   1 pincee muscade 1 feuille laurier 1 potimarron 1 cube bouillon poule,louche mixeur plonger blender chauffer couteau econome poele couvercle mixeur mijoteur electrique balance cuisine,etape 1 enlever ecorce pepin potimarron obligatoire peler cas choisir bio bien laver couper chair gros morceau etape 2 eplucher pomme terre couper gros morceau etape 3 faire revenir oignon ail hacher beurre feu doux etape 4 ajouter pomme terre potimarron faire revenir 5 min etape 5 couvrir eau ajouter bouillon poule emiette curry muscade feuille laurier mijoter 30 min feu doux etape 6 legume cuire verifier aide couteau mixer preparation etape 7 verifier assaisonnement saler poivrer gout ajouter creme frais mijoter 2 3 min bon appetit,soupe veloute potimarron pomme terre  2 pomme terre 2 oignon hache   3 gousse ail hache   10 cl creme frais   1 c.a.c curry   1 pincee muscade 1 feuille laurier 1 potimarron 1 cube bouillon poule  louche mixeur plonger blender chauffer couteau econome poele couvercle mixeur mijoteur electrique balance cuisine  etape 1 enlever ecorce pepin potimarron obligatoire peler cas choisir bio bien laver couper chair gros morceau etape 2 eplucher pomme terre couper gros morceau etape 3 faire revenir oignon ail hacher beurre feu doux etape 4 ajouter pomme terre potimarron faire revenir 5 min etape 5 couvrir eau ajouter bouillon poule emiette curry muscade feuille laurier mijoter 30 min feu doux etape 6 legume cuire verifier aide couteau mixer preparation etape 7 verifier assaisonnement saler poivrer gout ajouter creme frais mijoter 2 3 min bon appetit """
    return predicted_receipies


