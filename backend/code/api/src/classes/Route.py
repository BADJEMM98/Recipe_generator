import random
from typing import Dict, List
from .Point import Point

class Route(object):

    """
    Stores an ordered list of all the Point objects in the global list_of_cities.
    Also stores information about the route.
    self.route: list of cities in list_of_cities. Randomly shuffled upon __init__
    self.total_price: float total_price of route (full loop)
    self.is_valid_route(): Returns True if the route contains all cities in list_of_cities ONCE and ONLY ONCE
    self.pr_cits_in_rt(): Prints all the cities in the route, in the form <cityname1,cityname2,cityname3...>
    self.pr_vrb_cits_in_rt: Prints all the coordinate pairs of the cities in the route, in the form <|x,y|x,y|x,y|...>
    """
    def __init__(self,start:Point,points:List[Point]):
        # initiates a route attribute equal to a randomly shuffled list_of_cities
        choices = [point for point in points if (point.lat != start.lat and point.lon != start.lon)]
        self.route = sorted(choices, key=lambda *args: random.random())
        self.route.insert(0,start)

    def recalc_rt_price(self,paths_price:Dict[str,Dict[str,float]] ):
        '''
        self --> None
        Method to re-calculate the route total_price
        if the self.route attribute has been changed manually.
        '''
        # Zeroes its length
        self.total_price = 0.0
        # for every city in its route attribute:
        for point in self.route:
            # set up a next city variable that points to the next city in the list 
            # and wraps around at the end:
            next_point = self.route[self.route.index(point)-len(self.route)+1]
            # Uses the first city's price_to attribute to find the distance to the next city:
            price_to_next = paths_price[f"{point.lat},{point.lon}"][f"{next_point.lat},{next_point.lon}"]
            # adds this total_price to its total_price attr.
            self.total_price += price_to_next

    def pr_cits_in_rt(self, print_route=False):
        '''
        self --> None
        Prints all the cities in the route, in the form <cityname1,cityname2,cityname3...>
        '''
        points_str = ''
        for point in self.route:
            points_str += point.name + ','
        points_str = points_str[:-1] # chops off last comma
        if print_route:
            print('    ' + points_str)

    def pr_vrb_cits_in_rt(self):
        '''
        self --> None
        Prints all the coordinate pairs of the cities in the route, in the form <|x,y|x,y|x,y|...>
        '''
        points_str = '|'
        for point in self.route:
            points_str += str(point.lat) + ',' + str(point.lon) + '|'
        print(points_str)

    def is_valid_route(self,points:List[Point]):
        '''
        self --> Bool()
        Returns True if the route contains all cities in list_of_cities ONCE and ONLY ONCE
        i.e. returns False if there are duplicates.
        Use: if there are multiples of the same city in a route,
        it will converge until all the cities are that same city (length = 0)
        '''
        for point in points:
            # helper function defined up to
            if self.count_mult(self.route,lambda c: (point.lat == c.lat and point.lon == c.lon)) > 1:
                return False
        return True

    # Returns the number of pred in sequence (duplicate checking.)
    def count_mult(self, seq, pred):
        return sum(1 for v in seq if pred(v))

