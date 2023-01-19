import random
from typing import Dict, List
from .Point import Point
from .Route import Route
from .RoutePop import RoutePop
from ..params import k_mut_prob, tournament_size, elitism


# Class for bringing together all of the methods to do with the Genetic Algorithm
class GA(object):
    """
    Class for running the genetic algorithm. Do not __init__ - Class only provides methods. 
    crossover(parent1, parent2): Returns a child route after breeding the two parent routes. 
    """
    def __init__(self,points:List[Point],paths_price:Dict[str,Dict[str,float]],start:Point) -> None:
        self.points=points
        self.paths_price=paths_price
        self.start=start

    def crossover(self, parent1:Route, parent2:Route):
        '''
        Route(), Route() --> Route()
        Returns a child route Route() after breeding the two parent routes. 
        Routes must be of same length.
        Breeding is done by selecting a random range of parent1, and placing it into the empty child route (in the same place).
        Gaps are then filled in, without duplicates, in the order they appear in parent2.
        '''



        # new child Route()
        child_rt = Route(start=parent1.route[0],points=self.points)

        for x in range(1,len(child_rt.route)):
            child_rt.route[x] = None

        # Two random integer indices of the parent1:
        start_pos = random.randint(1,len(parent1.route))
        end_pos = random.randint(1,len(parent1.route))


        #### takes the sub-route from parent one and sticks it in itself:
        # if the start position is before the end:
        if start_pos < end_pos:
            # do it in the start-->end order
            for x in range(start_pos,end_pos):
                child_rt.route[x] = parent1.route[x] # set the values to eachother
        # if the start position is after the end:
        elif start_pos > end_pos:
            # do it in the end-->start order
            for i in range(end_pos,start_pos):
                child_rt.route[i] = parent1.route[i] # set the values to eachother


        # Cycles through the parent2. And fills in the child_rt
        # cycles through length of parent2:
        for i in range(len(parent2.route)):
            # if parent2 has a city that the child doesn't have yet:
            if not parent2.route[i] in child_rt.route:
                # it puts it in the first 'None' spot and breaks out of the loop.
                for x in range(len(child_rt.route)):
                    if child_rt.route[x] == None:
                        child_rt.route[x] = parent2.route[i]
                        break
        # repeated until all the cities are in the child route

        # returns the child route (of type Route())
        child_rt.recalc_rt_price(paths_price=self.paths_price)
        return child_rt

    def mutate(self, route_to_mut:Route,)->Route:
        '''
        Route() --> Route()
        Swaps two random indexes in route_to_mut.route. Runs k_mut_prob*100 % of the time
        '''
        # k_mut_prob %
        if random.random() < k_mut_prob:
            mut_pos1 = random.randint(1,len(route_to_mut.route)-1)
            mut_pos2 = random.randint(1,len(route_to_mut.route)-1)

            if mut_pos1 == mut_pos2:
                return route_to_mut

            # swap two randomly picked indexes:
            point1 = route_to_mut.route[mut_pos1]
            point2 = route_to_mut.route[mut_pos2]

            route_to_mut.route[mut_pos2] = point1
            route_to_mut.route[mut_pos1] = point2

        # Recalculate the total price of the route (updates it's .total_price)
        route_to_mut.recalc_rt_price(paths_price=self.paths_price)

        return route_to_mut

    def tournament_select(self, population)->Route:
        '''
        RoutePop() --> Route()
        Randomly selects tournament_size amount of Routes() from the input population.
        Takes the fittest from the smaller number of Routes(). 
        Principle: gives worse Routes() a chance of succeeding, but favours good Routes()
        '''

        # New smaller population (not intialised)
        tournament_pop = RoutePop(size=tournament_size,initialise=False)

        # fills it with random individuals (can choose same twice)
        for i in range(tournament_size-1):
            tournament_pop.rt_pop.append(random.choice(population.rt_pop))
        return tournament_pop.get_fittest()

    def evolve_population(self, init_pop:RoutePop):
        '''
        RoutePop() --> RoutePop()
        Takes a population and evolves it then returns the new population. 
        '''

        #makes a new population:
        descendant_pop = RoutePop(size=init_pop.size, initialise=True,start=self.start,points=self.points,paths_price=self.paths_price)

        # Elitism offset (amount of Routes() carried over to new population)
        elitismOffset = 0

        # if we have elitism, set the first of the new population to the fittest of the old
        if elitism:
            descendant_pop.rt_pop[0] = init_pop.fittest
            elitismOffset = 1

        # Goes through the new population and fills it with the child of two tournament winners from the previous populatio
        for x in range(elitismOffset,descendant_pop.size):
            # two parents:
            tournament_parent1 = self.tournament_select(init_pop)
            tournament_parent2 = self.tournament_select(init_pop)

            # A child:
            tournament_child = self.crossover(tournament_parent1, tournament_parent2)

            # Fill the population up with children
            descendant_pop.rt_pop[x] = tournament_child

        # Mutates all the routes (mutation with happen with a prob p = k_mut_prob)
        for route in descendant_pop.rt_pop:
            self.mutate(route)

        # Update the fittest route:
        descendant_pop.get_fittest()

        return descendant_pop


