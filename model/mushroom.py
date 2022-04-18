from enum import Enum


class Mushroom:
    def __init__(
        self,
        classification,
        cap_shape,
        cap_surface,
        cap_color,
        bruises,
        odor,
        gill_attachment,
        gill_spacing,
        gill_size,
        gill_color,
        stalk_shape,
        stalk_root,
        stalk_surface_above_ring,
        stalk_surface_below_ring,
        stalk_color_above_ring,
        stalk_color_below_ring,
        veil_type,
        veil_color,
        ring_number,
        ring_type,
        spore_print_color,
        population,
        habitat,
    ):
        """_summary_

        Args:
            target (_type_): _description_
            cap_shape (_type_): _description_
            cap_surface (_type_): _description_
            cap_color (_type_): _description_
            bruises (_type_): _description_
            odor (_type_): _description_
            gill_attachment (_type_): _description_
            gill_spacing (_type_): _description_
            gill_size (_type_): _description_
            gill_color (_type_): _description_
            stalk_shape (_type_): _description_
            stalk_root (_type_): _description_
            stalk_surface_above_ring (_type_): _description_
            stalk_surface_below_ring (_type_): _description_
            stalk_color_above_ring (_type_): _description_
            stalk_color_below_ring (_type_): _description_
            veil_type (_type_): _description_
            veil_color (_type_): _description_
            ring_number (_type_): _description_
            ring_type (_type_): _description_
            spore_print_color (_type_): _description_
            population (_type_): _description_
            habitat (_type_): _description_
        """

        self.classification = classification
        self.cap_shape = cap_shape
        self.cap_surface = cap_surface
        self.cap_color = cap_color
        self.bruises = bruises
        self.odor = odor
        self.gill_attachment = gill_attachment
        self.gill_spacing = gill_spacing
        self.gill_size = gill_size
        self.gill_color = gill_color
        self.stalk_shape = stalk_shape
        self.stalk_root = stalk_root
        self.stalk_surface_above_ring = stalk_surface_above_ring
        self.stalk_surface_below_ring = stalk_surface_below_ring
        self.stalk_color_above_ring = stalk_color_above_ring
        self.stalk_color_below_ring = stalk_color_below_ring
        self.veil_type = veil_type
        self.veil_color = veil_color
        self.ring_number = ring_number
        self.ring_type = ring_type
        self.spore_print_color = spore_print_color
        self.population = population
        self.habitat = habitat


class Classification(Enum):
    p = "POISONOUS"
    e = "EDIBLE"


class CapShape(Enum):
    b = "BELL"
    c = "CONICAL"
    x = "CONVEX"
    f = "FLAT"
    k = "KNOBBED"
    s = "SUNKEN"


class CapSurface(Enum):
    f = "FIBROUS"
    g = "GROOVES"
    y = "SCALY"
    s = "SMOOTH"


class CapColor(Enum):
    n = "BROWN"
    b = "BUFF"
    c = "CINNAMON"
    g = "GRAY"
    r = "GREEN"
    p = "PINK"
    u = "PURPLE"
    e = "RED"
    w = "WHITE"
    y = "YELLOW"


class Bruises(Enum):
    t = "BRUISES"
    f = "NO"


class Odor(Enum):
    a = "ALMOND"
    l = "ANISE"
    c = "CREOSOTE"
    y = "FISHY"
    f = "FOUL"
    m = "MUSTY"
    n = "NO ODOR"
    p = "PUNGENT"
    s = "SPICY"


class GillAttachment(Enum):
    a = "ATTACHED"
    d = "DESCENDING"
    f = "FREE"
    n = "NOTCHED"


class GillSpacing(Enum):
    c = "CLOSE"
    w = "CROWDED"
    d = "DISTANT"


class GillSize(Enum):
    b = "BROAD"
    n = "NARROW"


class GillColor(Enum):
    k = "BLACK"
    n = "BROWN"
    b = "BUFF"
    h = "CHOCOLATE"
    g = "GRAY"
    r = "GREEN"
    o = "ORANGE"
    p = "PINK"
    u = "PURPLE"
    e = "RED"
    w = "WHITE"
    y = "YELLOW"


class StalkShape(Enum):
    e = "ENLARGING"
    t = "TAPERING"


class StalkRoot(Enum):
    b = "BULBOUS"
    c = "CLUB"
    u = "CUP"
    e = "EQUAL"
    z = "RHIZOMORPHS"
    r = "ROOTED"
    m = "MISSING"


class StalkSurfaceAboveRing(Enum):
    f = "FIBROUS"
    y = "SCALY"
    k = "SILKY"
    s = "SMOOTH"


class StalkSurfaceBelowRing(Enum):
    f = "FIBROUS"
    y = "SCALY"
    k = "SILKY"
    s = "SMOOTH"


class StalkColorAboveRing(Enum):
    n = "BROWN"
    b = "BUFF"
    c = "CINNAMON"
    g = "GRAY"
    o = "ORANGE"
    p = "PINK"
    e = "RED"
    w = "WHITE"
    y = "YELLOW"


class StalkColorBelowRing(Enum):
    n = "BROWN"
    b = "BUFF"
    c = "CINNAMON"
    g = "GRAY"
    o = "ORANGE"
    p = "PINK"
    e = "RED"
    w = "WHITE"
    y = "YELLOW"


class VeilType(Enum):
    p = "PARTIAL"
    u = "UNIVERSAL"


class VeilColor(Enum):
    n = "BROWN"
    o = "ORANGE"
    w = "WHITE"
    y = "YELLOW"


class RingNumber(Enum):
    n = "ZERO"
    o = "ONE"
    t = "TWO"


class RingType(Enum):
    c = "COBWEBBY"
    e = "EVANESCENT"
    f = "FLARING"
    l = "LARGE"
    n = "NO RING"
    p = "PENDANT"
    s = "SHEATHING"
    z = "ZONE"


class SporePrintColor(Enum):
    k = "BLACK"
    n = "BROWN"
    b = "BUFF"
    h = "CHOCOLATE"
    r = "GREEN"
    o = "ORANGE"
    u = "PURPLE"
    w = "WHITE"
    y = "YELLOW"


class Population(Enum):
    a = "ABUNDANT"
    c = "CLUSTERED"
    n = "NUMEROUS"
    s = "SCATTERED"
    v = "SEVERAL"
    y = "SOLITARY"


class Habitat(Enum):
    g = "GRASSES"
    l = "LEAVES"
    m = "MEADOWS"
    p = "PATHS"
    u = "URBAN"
    w = "WASTE"
    d = "WOODS"
