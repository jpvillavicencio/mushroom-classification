import pandas as pd
from decision_tree.decision_tree import Tree
from sklearn.model_selection import train_test_split
import log
import os

folder_path = os.path.dirname(os.path.realpath(__file__))
logger = log.setup_custom_logger("mushy_logger")


def main():
    # initialise data
    df = pd.read_csv(f"{os.path.join(folder_path, 'input', 'mushrooms.csv')}")
    # remove na values from data
    df = df.dropna()
    # split data
    train_data, test_data = train_test_split(df, test_size=0.2, random_state=2212)

    # Prepare data for training
    attrs = df.keys()
    data = train_data[attrs]
    target = "class"

    t = Tree()
    t.train(data, target, max_depth=4)
    t.root.pretty_print()

    # Train Data
    train_results = t.calculate_accuracy(
        data=data,
        target=target,
    )

    logger.info(
        f"Training accuracy={((train_results['TP'] + train_results['TN']) / len(data))*100:.3f}%"
    )
    logger.info(
        f"TP={train_results['TP']}, TN={train_results['TN']}, FP={train_results['FP']}, FN={train_results['FN']}"
    )

    # Predict Test Data
    test_results = t.calculate_accuracy(
        data=test_data,
        target=target,
    )
    logger.info(
        f"Testing accuracy={((test_results['TP'] + test_results['TN']) / len(test_data))*100:.3f}%"
    )
    logger.info(
        f"TP={test_results['TP']}, TN={test_results['TN']}, FP={test_results['FP']}, FN={test_results['FN']}"
    )


if __name__ == "__main__":
    main()
