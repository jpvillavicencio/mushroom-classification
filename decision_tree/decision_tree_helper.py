import numpy as np
import logging

logger = logging.getLogger("mushy_logger")


def compute_entropy(y):
    """Compute Entroy: Calculate the entropy of an attribute

    Args:
        y (pandas.core.series.Series): attribute

    Returns:
        numpy.float64: calculated entropy
    """
    if len(y) < 2:  #  a trivial case
        return 0
    freq = np.array(y.value_counts(normalize=True))
    return -(freq * np.log2(freq + 1e-6)).sum()


def compute_info_gain(samples, attr, target):
    """_summary_

    Args:
        samples (_type_): _description_
        attr (_type_): _description_
        target (_type_): _description_

    Returns:
        _type_: _description_
    """
    values = samples[attr].value_counts(normalize=True)
    split_ent = 0
    for value, percentage in values.iteritems():
        # get split of each attribute
        logger.debug(f"{attr}:{value}:{percentage:.3f}")
        sub_ent = compute_entropy(target[samples[attr] == value])
        split_ent += percentage * sub_ent
        logger.debug(
            f"sub_ent: {compute_entropy(target[samples[attr] == value]):.3f} | split_ent: {split_ent:.3f} "
        )
    ent = compute_entropy(target)
    return ent - split_ent


def most_common_value(index):
    return index.value_counts().idxmax()
