from .endpoints import Home, Receipes
import falcon

 
app = application = falcon.App(cors_enable=True)



home = Home()
receipes = Receipes()


app.add_route("/homes", home)
app.add_route('/receipes', receipes)
