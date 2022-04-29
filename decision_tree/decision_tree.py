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
    compute_info_gain,
    most_common_value,
)

logger = logging.getLogger("mushy_logger")


class TreeNode:
    """_summary_"""

    def __init__(
        self,
        max_depth=5,
        curr_depth=0,
        dataset="generic",
    ):
        """_summary_

        Args:
            samples (dataframe): dataset
            target (dataframe): dataset of target
            curr_depth (int, optional): current depth of tree. Defaults to 0.
            max_depth (int, optional): maximum depth of tree. Defaults to 5.
        """
        self.children = {}
        self.decision = None
        self.split_attr = None
        self.curr_depth = curr_depth
        self.max_depth = max_depth
        self.dataset = dataset
        self.results = {
            "TP": 0,
            "TN": 0,
            "FP": 0,
            "FN": 0,
        }

    def train(self, samples, target, target_name):
        if len(samples) == 0 or self.curr_depth == self.max_depth:
            # if there are no samples or reached max depth, use arbitary value of poisonous atm.
            self.decision = most_common_value(target)
            logger.debug(f"no decision: {self.decision}")
            return
        else:
            unique_values = target.unique()
            if len(unique_values) == 1:
                # check if data is pure
                self.decision = unique_values[0]
                logger.debug(f"pure decision: {self.decision}")
                return
            else:
                # Generate Subtree
                info_gain_max = 0
                for attr in samples.keys():  # Examine each attribute
                    if attr == target_name:
                        continue
                    attr_ig = compute_info_gain(samples, attr, target)
                    if attr_ig > info_gain_max:
                        self.split_attr = attr
                        logger.debug(
                            f"attr: {attr} | split_attr: {self.split_attr} | previous ig: {info_gain_max:.3f} | split_attr ig: {attr_ig:.3f}"
                        )
                        info_gain_max = attr_ig
                logger.debug(f"Split by {self.split_attr}, IG: {info_gain_max:.3f}")
                self.children = {}
                try:
                    for value in samples[self.split_attr].unique():
                        index = samples[self.split_attr] == value
                        self.children[value] = TreeNode(
                            curr_depth=self.curr_depth + 1,
                            max_depth=self.max_depth,
                            dataset=self.dataset,
                        )
                        self.children[value].train(
                            samples[index],
                            target[index],
                            target_name=target_name,
                        )
                except Exception as e:
                    logger.error(f"Training Error occured due to {repr(e)}")

    def predict(self, sample, curr_depth=0):
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
            if curr_depth == self.max_depth:
                # return arbitary value
                return 1
            else:
                attr_val = sample[self.split_attr]
                logger.debug(f"testing {self.split_attr} -> {attr_val}")
                return self.children[attr_val].predict(
                    sample, curr_depth=curr_depth + 1
                )

    def calculate_accuracy(self, df, target):
        self.results = {
            "TP": 0,
            "TN": 0,
            "FP": 0,
            "FN": 0,
        }
        for i in range(0, len(df)):
            try:
                prediction = self.predict(df.iloc[i])
            except Exception as e:
                logger.error(f"Prediction failed at row {i} due to {repr(e)}")
                # abitrary value
                prediction = 0
            if prediction == df.iloc[i][target]:
                if prediction == 0:
                    self.results["TP"] += 1
                else:
                    self.results["TN"] += 1
            else:
                if prediction == 1:
                    self.results["FP"] += 1
                else:
                    self.results["FN"] += 1

        return self.results

    def pretty_print(self, prefix=""):
        """Prints the results of the tree

        Args:
            prefix (str, optional): used for prepending existing string. Defaults to ''.
        """
        if self.split_attr is None:
            if self.dataset == "mushroom":
                logger.info(
                    f"{prefix} | decision -> {mushroom_mapping['class']['e' if self.decision == 0 else 'p'].value}"
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
