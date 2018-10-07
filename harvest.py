############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)

        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code
        # Fill in the rest


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    casaba = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    crenshaw = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    yelllow_watermelon = MelonType('yw', 2013, 'yellow', False, True, 'yw')

    musk.add_pairing('mint')
    all_melon_types.append(musk)

    casaba.add_pairing('strawberry')
    casaba.add_pairing('mint')
    all_melon_types.append(casaba)

    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)

    yelllow_watermelon.add_pairing('ice cream')
    all_melon_types.append(yelllow_watermelon)

    # Fill in the rest

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon in melon_types:
    	print("{} pairs with".format(melon.name))
    	for pairing in melon.pairings:
    		print("- {}".format(pairing))


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    dict_melon = {}

    for melon in melon_types:
    	dict_melon[melon.code] = melon

    return dict_melon

print(make_melon_type_lookup(make_melon_types()))

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape_rating, color_rating, harvest_field, harvest_person):

    	self.melon_type = melon_type
    	self.shape_rating = shape_rating
    	self.color_rating = color_rating
    	self.harvest_field = harvest_field
    	self.harvest_person = harvest_person
    	self.is_sellable = T


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



