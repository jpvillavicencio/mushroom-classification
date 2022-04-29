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
from decision_tree.decision_tree_helper import (
    compute_entropy,
    compute_info_gain,
    most_common_value,
)

logger = logging.getLogger("mushy_logger")


class TreeNode:
    """_summary_"""

    def __init__(
        self,
        samples,
        target,
        curr_depth=0,
        max_depth=5,
        dataset="generic",
    ):
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
        self.dataset = dataset

        self.train()

    def train(self):
        if len(self.samples) == 0:
            # if there are no samples, use arbitary value of poisonous atm.
            self.decision = most_common_value(self.samples[self.target])
            logger.debug(f"no decision: {self.decision}")
        elif self.curr_depth == self.max_depth:
            self.decision = most_common_value(self.samples[self.target])
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
                        f"attr: {attr} | split_attr: {self.split_attr} | previous ig: {info_gain_max:.3f} | split_attr ig: {attr_ig:.3f}"
                    )
                    info_gain_max = attr_ig
            for v in self.samples[self.split_attr].unique():
                index = self.samples[self.split_attr] == v
                self.children[v] = TreeNode(
                    self.samples[index],
                    self.target,
                    curr_depth=self.curr_depth + 1,
                    max_depth=self.max_depth,
                    dataset=self.dataset,
                )

    def predict(self, sample):
        """predicts classification based on previous training data

        Args:
            sample (dataframe): test sample

        Returns:
            str: decision
        """
        if self.decision is not None:
            logger.debug(f"decision: {self.decision}")
            return self.decision
        else:
            attr_val = sample[self.split_attr]
            logger.debug(f"testing {self.split_attr} -> {attr_val}")
            return self.children[attr_val].predict(sample)

    def pretty_print(self, prefix=""):
        """Prints the results of the tree

        Args:
            prefix (str, optional): used for prepending existing string. Defaults to ''.
        """
        if self.split_attr is None:
            if self.dataset == "mushroom":
                logger.info(
                    f"{prefix} | decision -> {mushroom_mapping[self.target][self.decision].value}"
                )
            else:
                logger.info(f"{prefix} | decision -> {self.decision}")
        else:
            for k, v in self.children.items():
                if self.dataset == "mushroom":
                    if prefix:
                        v.pretty_print(
                            f"{prefix} -> {self.split_attr}={mushroom_mapping[self.split_attr][k].value}"
                        )
                    else:
                        v.pretty_print(
                            f"{self.split_attr}={mushroom_mapping[self.split_attr][k].value}"
                        )
                else:
                    if prefix:
                        v.pretty_print(f"{prefix} -> {self.split_attr}={k}")
                    else:
                        v.pretty_print(f"{self.split_attr}={k}")


class Tree:
    def __init__(self, dataset="generic"):
        """Tree Constructor"""
        self.root = None
        self.dataset = dataset

    def train(self, samples, target, max_depth=5):
        """trains decision tree based on samples

        Args:
            samples (df): training data
            target (string): target classificaiton
            max_depth (int, optional): maximum depth of decision tree. Defaults to 5.
        """
        self.root = TreeNode(samples, target, max_depth=max_depth, dataset=self.dataset)

    def calculate_accuracy(self, data, target):
        """Calculates the accuracy of the data

        Args:
            t (Tree): decision tree
            data (df): data sample
            target (string): classification

        Returns:
            results: training accuracy
        """

        results = {
            "TP": 0,
            "TN": 0,
            "FP": 0,
            "FN": 0,
        }

        for i in range(0, len(data)):
            prediction = self.root.predict(data.iloc[i])
            # logger.info(f"{data.iloc[i][target]}")
            if prediction == data.iloc[i][target]:
                if prediction == 0:
                    results["TP"] += 1
                else:
                    results["TN"] += 1
            else:
                if prediction == 1:
                    results["FP"] += 1
                else:
                    results["FN"] += 1

        return results


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
