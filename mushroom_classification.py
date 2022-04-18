import pandas as pd
from decision_tree.decision_tree import Tree
from sklearn.model_selection import train_test_split
import log
import os

folder_path = os.path.dirname(os.path.realpath(__file__))
logger = log.setup_custom_logger("mushy_logger")


def evaluate_data(df):
    df.info()

    for attr in df.keys():
        logger.debug(df[attr].value_counts(normalize=True))

    # check for null values
    logger.debug(df.isnull().sum())


def clean_data(df):
    # clean data if they only have 1 value
    for attr in df.keys():
        if df[attr].nunique() == 1:
            del df[attr]

    # remove null values from data
    df = df.dropna()


def main():
    # initialise data
    df = pd.read_csv(f"{os.path.join(folder_path, 'input', 'mushrooms.csv')}")
    evaluate_data(df)
    clean_data(df)

    # split data
    train_data, test_data = train_test_split(df, test_size=0.2, random_state=2212)
    train_data.info()
    test_data.info()

    # Prepare data for training
    attrs = df.keys()
    data = train_data[attrs]
    target = "class"

    t = Tree()
    t.train(data, target, max_depth=3)
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
