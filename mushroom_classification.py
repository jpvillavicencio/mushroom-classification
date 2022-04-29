import pandas as pd
from decision_tree.decision_tree import TreeNode
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


def run_model_with_target(df, target, max_depth=3, dataset="generic"):
    # initialise data
    evaluate_data(df)
    clean_data(df)

    # split data
    train_data, test_data = train_test_split(df, test_size=0.4, random_state=2212)
    train_data.info()
    test_data.info()
    # Prepare data for training
    target_set = train_data[target]

    t = TreeNode(
        max_depth=max_depth,
        dataset=dataset,
    )
    t.train(samples=train_data, target=target_set, target_name=target)
    t.pretty_print()

    # Train Data
    train_results = t.calculate_accuracy(
        df=train_data,
        target=target,
    )

    logger.info(
        f"Training accuracy={((train_results['TP'] + train_results['TN']) / len(train_data))*100:.3f}%"
    )
    logger.info(
        f"TP={train_results['TP']}, TN={train_results['TN']}, FP={train_results['FP']}, FN={train_results['FN']}"
    )
    logger.info(
        f"TP={train_results['TP']/ len(train_data)*100:.2f}%, TN={train_results['TN']/ len(train_data)*100:.2f}%, FP={train_results['FP']/ len(train_data)*100:.2f}%, FN={train_results['FN']/ len(train_data)*100:.2f}%"
    )

    # Predict Test Data
    test_results = t.calculate_accuracy(
        df=test_data,
        target=target,
    )
    logger.info(
        f"Testing accuracy={((test_results['TP'] + test_results['TN']) / len(test_data))*100:.3f}%"
    )
    logger.info(
        f"TP={test_results['TP']}, TN={test_results['TN']}, FP={test_results['FP']}, FN={test_results['FN']}"
    )
    logger.info(
        f"TP={test_results['TP']/ len(test_data)*100:.2f}%, TN={test_results['TN']/ len(test_data)*100:.2f}%, FP={test_results['FP']/ len(test_data)*100:.2f}%, FN={test_results['FN']/ len(test_data)*100:.2f}%"
    )


def main():
    # Mushroom Dataset
    mushroom_df = pd.read_csv(f"{os.path.join(folder_path, 'input', 'mushrooms.csv')}")
    mushroom_target = "class"
    # Map Target results to 0 or 1
    mushroom_df[mushroom_target] = mushroom_df[mushroom_target].map({"e": 0, "p": 1})
    run_model_with_target(
        df=mushroom_df,
        target=mushroom_target,
        dataset="mushroom",
    )

    # # Iris Dataset
    # df = pd.read_csv(f"{os.path.join(folder_path, 'input', 'iris.data')}")
    # target = "class"
    # df = df[df[target] != "Iris-virginica"]
    # df[target] = df[target].map({"Iris-setosa": 0, "Iris-versicolor": 1})
    # run_model_with_target(df=df, target=target)

    # # Connect 4
    # df = pd.read_csv(f"{os.path.join(folder_path, 'input', 'connect-4.data')}")
    # target = "Class"
    # df = df[df[target] != "draw"]
    # df[target] = df[target].map({"win": 0, "loss": 1})
    # run_model_with_target(df=df, target=target, max_depth=5)


if __name__ == "__main__":
    main()
