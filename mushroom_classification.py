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
    train_data, test_data = train_test_split(df, test_size=0.2, random_state=2212)

    # Prepare data for training
    attrs = df.keys()
    data = train_data[attrs]
    target = "class"

    # Train Data
    train_results = {
        "TP": 0,
        "TN": 0,
        "FP": 0,
        "FN": 0,
    }
    t = Tree()
    t.train(data, target, max_depth=4)
    t.root.pretty_print()

    # Calculate Training Accuracy
    for i in range(0, len(data)):
        prediction = t.predict(data.iloc[i])
        if prediction == data.iloc[i][target]:
            if prediction == "e":
                train_results["TP"] += 1
            else:
                train_results["TN"] += 1
        else:
            if prediction == "e":
                train_results["FP"] += 1
            else:
                train_results["FN"] += 1

        # logger.debug(
        #     f"predicition: {prediction} | actual: {test_data.iloc[i]['target']}"
        # )
    logger.info(
        f"Training accuracy={((train_results['TP'] + train_results['TN']) / len(data))*100:.3f}%"
    )
    logger.info(
        f"TP={train_results['TP']}, TN={train_results['TN']}, FP={train_results['FP']}, FN={train_results['FN']}"
    )

    # Predict
    test_results = {
        "TP": 0,
        "TN": 0,
        "FP": 0,
        "FN": 0,
    }
    ## Single Prediction
    # prediction = t.predict(test_data.iloc[0])
    # print(f"predicition: {prediction} | actual: {test_data.iloc[0]['target']}")

    ## Predict Loop
    for i in range(0, len(test_data)):
        prediction = t.predict(test_data.iloc[i])
        if prediction == test_data.iloc[i][target]:
            if prediction == "e":
                test_results["TP"] += 1
            else:
                test_results["TN"] += 1
        else:
            # logger.debug(
            #     f"predicition: {prediction} | actual: {test_data.iloc[i]['target']}"
            # )
            if prediction == "e":
                test_results["FP"] += 1
            else:
                test_results["FN"] += 1

    logger.info(
        f"Testing accuracy={((test_results['TP'] + test_results['TN']) / len(test_data))*100:.3f}%"
    )
    logger.info(
        f"TP={test_results['TP']}, TN={test_results['TN']}, FP={test_results['FP']}, FN={test_results['FN']}"
    )


if __name__ == "__main__":
    main()
