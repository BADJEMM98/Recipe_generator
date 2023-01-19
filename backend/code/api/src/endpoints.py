import falcon, json
from .services import  ReceipesService
import json


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o) 

class Home(object):
    def on_get(self,req,resp):
        resp.body = json.dumps({'status': falcon.HTTP_200, 'message': "home"})
        resp.status=falcon.HTTP_200
        return resp


class Receipes(object):

    #
    def on_post(self,req,resp):
        '''
         This method will recevie the list of ingredients and send receipes generated
        :param req: It contains json of list of ingredients.......
        :param resp:
        :return:
        '''
        ingredients_list = req.media
        print(ingredients_list)
        resp_from_service= ReceipesService(ingredients_list)
        resp.body = json.dumps({'status': falcon.HTTP_200, 'message':'Receipies generated with success', 'recipies': resp_from_service})
        resp.status=falcon.HTTP_200

