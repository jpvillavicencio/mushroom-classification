from enum import Enum


class Mushroom:
    def __init__(
        self,
        target,
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

        self.target = target
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
    P = "POISONOUS"
    E = "EDIBLE"


class CapShape(Enum):
    B = "BELL"
    C = "CONICAL"
    X = "CONVEX"
    F = "FLAT"
    K = "KNOBBED"
    S = "SUNKEN"


class CapSurface(Enum):
    F = "FIBROUS"
    G = "GROOVES"
    Y = "SCALY"
    S = "SMOOTH"


class CapColor(Enum):
    N = "BROWN"
    B = "BUFF"
    C = "CINNAMON"
    G = "GRAY"
    R = "GREEN"
    P = "PINK"
    U = "PURPLE"
    E = "RED"
    W = "WHITE"
    Y = "YELLOW"


class Bruises(Enum):
    T = "BRUISES"
    F = "NO"


class Odor(Enum):
    A = "ALMOND"
    L = "ANISE"
    C = "CREOSOTE"
    Y = "FISHY"
    F = "FOUL"
    M = "MUSTY"
    N = "NO ODOR"
    P = "PUNGENT"
    S = "SPICY"


class GillAttachment(Enum):
    A = "ATTACHED"
    D = "DESCENDING"
    F = "FREE"
    N = "NOTCHED"


class GillSpacing(Enum):
    C = "CLOSE"
    W = "CROWDED"
    D = "DISTANT"


class GillSize(Enum):
    B = "BROAD"
    N = "NARROW"


class GillColor(Enum):
    K = "BLACK"
    N = "BROWN"
    B = "BUFF"
    H = "CHOCOLATE"
    G = "GRAY"
    R = "GREEN"
    O = "ORANGE"
    P = "PINK"
    U = "PURPLE"
    E = "RED"
    W = "WHITE"
    Y = "YELLOW"


class StalkShape(Enum):
    E = "ENLARGING"
    T = "TAPERING"


class StalkRoot(Enum):
    B = "BULBOUS"
    C = "CLUB"
    U = "CUP"
    E = "EQUAL"
    Z = "RHIZOMORPHS"
    R = "ROOTED"
    M = "MISSING"


class StalkSurfaceAboveRing(Enum):
    F = "FIBROUS"
    Y = "SCALY"
    K = "SILKY"
    S = "SMOOTH"


class StalkSurfaceBelowRing(Enum):
    F = "FIBROUS"
    Y = "SCALY"
    K = "SILKY"
    S = "SMOOTH"


class StalkColorAboveRing(Enum):
    N = "BROWN"
    B = "BUFF"
    C = "CINNAMON"
    G = "GRAY"
    O = "ORANGE"
    P = "PINK"
    E = "RED"
    W = "WHITE"
    Y = "YELLOW"


class StalkColorBelowRing(Enum):
    N = "BROWN"
    B = "BUFF"
    C = "CINNAMON"
    G = "GRAY"
    O = "ORANGE"
    P = "PINK"
    E = "RED"
    W = "WHITE"
    Y = "YELLOW"


class VeilType(Enum):
    P = "PARTIAL"
    U = "UNIVERSAL"


class VeilColor(Enum):
    N = "BROWN"
    O = "ORANGE"
    W = "WHITE"
    Y = "YELLOW"


class RingNumber(Enum):
    N = "ZERO"
    O = "ONE"
    T = "TWO"


class RingType(Enum):
    C = "COBWEBBY"
    E = "EVANESCENT"
    F = "FLARING"
    L = "LARGE"
    N = "NO RING"
    P = "PENDANT"
    S = "SHEATHING"
    Z = "ZONE"


class SporePrintColor(Enum):
    K = "BLACK"
    N = "BROWN"
    B = "BUFF"
    H = "CHOCOLATE"
    R = "GREEN"
    O = "ORANGE"
    U = "PURPLE"
    W = "WHITE"
    Y = "YELLOW"


class Population(Enum):
    A = "ABUNDANT"
    C = "CLUSTERED"
    N = "NUMEROUS"
    S = "SCATTERED"
    V = "SEVERAL"
    Y = "SOLITARY"


class Habitat(Enum):
    G = "GRASSES"
    L = "LEAVES"
    M = "MEADOWS"
    P = "PATHS"
    U = "URBAN"
    W = "WASTE"
    D = "WOODS"
