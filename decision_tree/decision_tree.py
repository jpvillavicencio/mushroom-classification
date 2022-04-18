import logging
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

logger = logging.getLogger("mushy_logger")


class TreeNode:
    """_summary_"""

    def __init__(self, samples, target, curr_depth=0, max_depth=5):
        """_summary_

        Args:
            samples (dataframe): dataset
            target (string): string of target from dataset
            curr_depth (int, optional): current depth of tree. Defaults to 0.
            max_depth (int, optional): maximum depth of tree. Defaults to 5.
        """
        self.decision = None
        self.samples = samples
        self.target = target
        self.split_attr = None
        self.children = {}
        self.curr_depth = curr_depth
        self.max_depth = max_depth

        self.train()

    def train(self):
        if len(self.samples) == 0 or self.curr_depth == self.max_depth:
            # if there are no samples, use arbitary value of poisonous atm.
            self.decision = "p"
            logger.debug(f"no decision: {self.decision}")
        elif len(self.samples[self.target].unique()) == 1:
            # check if data is pure
            self.decision = self.samples[self.target].unique()[0]
            logger.debug(f"pure decision: {self.decision}")
        else:
            # Generate Subtree
            info_gain_max = 0
            for attr in self.samples.keys():  # Examine each attribute
                # print(f"attr: {attr}")
                if attr == self.target:
                    continue
                attr_ig = compute_info_gain(self.samples, attr, self.target)
                if attr_ig > info_gain_max:
                    self.split_attr = attr
                    logger.debug(
                        f"split_attr: {self.split_attr} | previous ig: {info_gain_max} | split_attr ig: {attr_ig}"
                    )
                    info_gain_max = attr_ig
            self.children = {}
            for v in self.samples[self.split_attr].unique():
                index = self.samples[self.split_attr] == v
                self.children[v] = TreeNode(
                    self.samples[index],
                    self.target,
                    curr_depth=self.curr_depth + 1,
                    max_depth=self.max_depth,
                )

    def pretty_print(self, prefix=""):
        """Prints the results of the

        Args:
            prefix (str, optional): _description_. Defaults to ''.
        """
        # print(f"children count: {len(self.children)}")
        # print(f"self.split_attr: {self.split_attr}")
        if self.split_attr is None:
            logger.info(
                f"{prefix} | decision -> {mushroom_mapping[self.target][self.decision].value}"
            )
        else:
            for k, v in self.children.items():
                if prefix:
                    v.pretty_print(
                        f"{prefix} -> {self.split_attr}={mushroom_mapping[self.split_attr][k].value}"
                    )
                else:
                    v.pretty_print(
                        f"{self.split_attr}={mushroom_mapping[self.split_attr][k].value}"
                    )


class Tree:
    def __init__(self):
        """_summary_"""
        self.root = None
        self.current_node = None

    def train(self, samples, target, max_depth=5):
        """_summary_

        Args:
            samples (_type_): _description_
            target (_type_): _description_
        """
        self.root = TreeNode(samples, target, max_depth=max_depth)

    def predict(self, sample):
        """_summary_

        Args:
            sample (dataframe): test sample

        Returns:
            str: decision
        """
        decision = None
        self.current_node = self.root
        while decision is None:
            if self.current_node.decision is not None:
                logger.debug(f"decision: {self.current_node.decision}")
                return self.current_node.decision
            else:
                attr_val = sample[self.current_node.split_attr]
                logger.debug(
                    f"testing {self.current_node.split_attr} -> {mushroom_mapping[self.current_node.split_attr][attr_val].value}"
                )
                self.current_node = self.current_node.children[attr_val]
        return decision


mushroom_mapping = {
    "class": Classification,
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
