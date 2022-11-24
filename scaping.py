import requests
from bs4 import BeautifulSoup
import csv


def recette_links(link, number_of_page):
    recette_links = []
    for page_number in range(1,number_of_page):
        link = f"{link}{page_number}"
        soup = BeautifulSoup(requests.get(link).text, "html.parser")
        recettes = soup.find_all("div", class_="recipe-card__picture")
        
        for recette in recettes:
            recette_links.append(recette.parent.get("href"))

    return recette_links

def recette(link,recettes,type_recette):

    soup = BeautifulSoup(requests.get(link).text, "html.parser", exclude_encodings=["utf-8"])

    nom= soup.find("h1",class_="SHRD__sc-10plygc-0 itJBWW").text
    duree = soup.find("p", class_="RCP__sc-1qnswg8-1 iDYkZP").text

    personnes = soup.find("div", class_="SHRD__sc-w4kph7-5 gHA-dzn").find("span").text


    etapes = []
    [etapes.append({etape.text:etape.find_parents("li")[0].find("p", class_="RCP__sc-1wtzf9a-3 jFIVDw").text}) for etape in soup.find_all("h3",class_="RCP__sc-1wtzf9a-1 ikYBNp")]

    images_ingredients = soup.find_all("div", class_="RCP__sc-vgpd2s-2 fNmocT")
    ingredients = []
    
    for image in images_ingredients:
        all =[ nom.text for nom in image.next_sibling.find_all("span")]
        tmp = all[0].split('\xa0')
        tmp= str(tmp[0]+tmp[len(tmp)-1]).replace('[','').replace(']','').replace("'","")
        all[0] = tmp
        [ingredients.append(str(all[i])) for i in range(int(len(all)/2))]



    images_ustensiles = soup.find_all("div", class_="RCP__sc-1641h7i-3 iLcXC")
    ustensiles = []

    [ustensiles.append(ustensile.text[2:]) for ustensile in images_ustensiles]

    recettes.append((nom,duree,personnes,type_recette,ingredients,ustensiles,etapes))

    return recettes

types={
    "Plat principal":["platprincipal",300],
    "Entrées":["",300],
    "Dessert":["dessert",300],
    "Amuse gueule":["amusegueule",300],
    "Sauce":["sauce",80],
    "Accompagnement":["accompagnement",100],
    "Boisson":["boisson",49]
}

[print(type,types[type][0],types[type][1]) for type in types]
recettes =[]
for type in types :
    receip_type = types[type][0]
    number_of_page = types[type][1]
    links = recette_links(f"https://www.marmiton.org/recettes?type={receip_type}&page=",number_of_page)
    for link in links:
        recette(link,recettes,type)
        print(link,recettes,type)

with open('recettes.csv', 'w', newline='',encoding='utf-8') as r:    
    writer = csv.writer(r)    
    writer.writerow(["Nom", "Duree", "Personnes","Type","Ingredients","Ustensiles","Etapes"])
    for recette in recettes:
        writer.writerow(recette)
