
# Contains a population of Route() objects
from typing import Dict, List
from .Point import Point
from .Route import Route


class RoutePop(object):
    """
    Contains a list of route objects and provides info on them.
    self.rt_pop: list of Route objects
    self.size: size of rt_pop 
    self.fittest: Route() object with best total_price from self.rt_pop
    self.get_fittest(): Calcualtes fittest route, sets self.fittest to it, and returns the Route. Use if routes have changed manually.
    """
    def __init__(self, size, initialise,start:Point=None,points:List[Point]=None,paths_price:Dict[str,Dict[str,float]]=None):
        self.rt_pop = []
        self.size = size
        # If we want to initialise a population.rt_pop:
        if initialise:
            for x in range(0,size):
                new_rt = Route(start=start,points=points)
                new_rt.recalc_rt_price(paths_price)
                self.rt_pop.append(new_rt)
            self.get_fittest()

    def get_fittest(self):
        '''
        self --> Route()
        Returns the two shortest routes in the population, in a list called self.top_two
        '''
        # sorts the list based on the routes' total prices
        sorted_list  = sorted(self.rt_pop, key=lambda x: x.total_price, reverse=False)
        sorted_list[0].pr_cits_in_rt()
        self.fittest = sorted_list[0]
        return self.fittest

