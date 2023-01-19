class Point(object):
    """
    Stores Points objects. Upon initiation, automatically appends itself to list_of_cities
    self.name: human readable name.
    self.price_to: dictionary of price to other cities (keys are city names, values are floats)
    """
    def __init__(self, name, lat, lon):
        # Name and coordinates:
        self.name = name
        self.lat  = lat
        self.lon  = lon