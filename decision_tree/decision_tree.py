from model.mushroom import (
    Classification,
    CapShape,
    CapSurface,
    CapColor,
    Bruises,
    Odor,
    GillAttachment,
    GillSpacing,
    GillSize,
    GillColor,
    StalkShape,
    StalkRoot,
    StalkSurfaceAboveRing,
    StalkSurfaceBelowRing,
    StalkColorAboveRing,
    StalkColorBelowRing,
    VeilType,
    VeilColor,
    RingNumber,
    RingType,
    SporePrintColor,
    Population,
    Habitat,
)
from decision_tree.decision_tree_helper import compute_entropy, compute_info_gain


class TreeNode:
    """_summary_"""

    def __init__(self, samples, target, max_depth=5):
        """_summary_

        Args:
            samples (_type_): _description_
            target (_type_): _description_
        """
        self.decision = None
        self.samples = samples
        self.target = target
        self.split_attr = None
        self.children = {}
        self.max_depth = max_depth
        self.mushroom = {
            "target": Classification,
            "cap_shape": CapShape,
            "cap_surface": CapSurface,
            "cap_color": CapColor,
            "bruises": Bruises,
            "odor": Odor,
            "gill_attachment": GillAttachment,
            "gill_spacing": GillSpacing,
            "gill_size": GillSize,
            "gill_color": GillColor,
            "stalk_shape": StalkShape,
            "stalk_root": StalkRoot,
            "stalk_surface_above_ring": StalkSurfaceAboveRing,
            "stalk_surface_below_ring": StalkSurfaceBelowRing,
            "stalk_color_above_ring": StalkColorAboveRing,
            "stalk_color_below_ring": StalkColorBelowRing,
            "veil_type": VeilType,
            "veil_color": VeilColor,
            "ring_number": RingNumber,
            "ring_type": RingType,
            "spore_print_color": SporePrintColor,
            "population": Population,
            "habitat": Habitat,
        }

    def make(self, depth=0):
        """_summary_"""
        if len(self.samples) == 0 or depth == self.max_depth:
            # if there are no samples, use parent node. arbitary value of poisonous atm.
            self.decision = "P"
            # print(f"decision: {self.decision}")
        elif len(self.samples[self.target].unique()) == 1:
            # check if data is pure
            self.decision = self.samples[self.target].unique()[0]
            # print(f"pure decision: {self.decision}")
        else:
            # Generate Subtree
            info_gain_max = 0
            for attr in self.samples.keys():  # Examine each attribute
                # print(f"attr: {attr}")
                if attr == self.target:
                    continue
                attr_ig = compute_info_gain(self.samples, attr, self.target)
                if attr_ig > info_gain_max:
                    info_gain_max = attr_ig
                    self.split_attr = attr
                    # print(
                    #     f"split_attr: {self.split_attr} | previous ig: {info_gain_max} | new ig: {attr_ig}"
                    # )
            self.children = {}
            for v in self.samples[self.split_attr].unique():
                index = self.samples[self.split_attr] == v
                self.children[v] = TreeNode(
                    self.samples[index], self.target, max_depth=self.max_depth
                )
                self.children[v].make(depth=depth + 1)

    def pretty_print(self, prefix=""):
        """Prints the results of the

        Args:
            prefix (str, optional): _description_. Defaults to ''.
        """
        # print(f"children count: {len(self.children)}")
        # print(f"self.split_attr: {self.split_attr}")
        if self.split_attr is None:
            print(
                f"{prefix} | decision -> {self.mushroom['target'][self.decision].value}"
            )
        else:
            for k, v in self.children.items():
                if prefix:
                    v.pretty_print(
                        f"{prefix} | when {self.split_attr} -> {self.mushroom[self.split_attr][k].value}"
                    )

                else:
                    v.pretty_print(
                        f"when {self.split_attr} -> {self.mushroom[self.split_attr][k].value}"
                    )

    def predict(self, sample):
        """_summary_

        Args:
            sample (object): test sample

        Returns:
            str: decision
        """
        if self.decision is not None:
            print(f"decision: {self.decision}")
            return self.decision
        else:
            attr_val = sample[self.split_attr]
            # print(f"testing {self.split_attr} -> {attr_val}")
            child = self.children[attr_val]
        return child.decision


class Tree:
    def __init__(self):
        """_summary_

        Args:
            samples (_type_): _description_
            target (_type_): _description_
        """
        self.root = None

    def fit(self, samples, target, max_depth=5):
        """_summary_

        Args:
            samples (_type_): _description_
            target (_type_): _description_
        """
        self.root = TreeNode(samples, target, max_depth=max_depth)
        self.root.make()
