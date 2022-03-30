import pandas as pd
from decision_tree.decision_tree import Tree
from sklearn.model_selection import train_test_split


if __name__ == "__main__":
    # initialise data
    df = pd.read_csv("input/mushrooms.csv")
    train_data, test_data = train_test_split(df, test_size=0.2)

    # Prepare data for training
    attrs = [
        "target",
        "cap_shape",
        "cap_surface",
        "cap_color",
        "bruises",
        "odor",
        "gill_attachment",
        "gill_spacing",
        "gill_size",
        "gill_color",
        "stalk_shape",
        "stalk_root",
        "stalk_surface_above_ring",
        "stalk_surface_below_ring",
        "stalk_color_above_ring",
        "stalk_color_below_ring",
        "veil_type",
        "veil_color",
        "ring_number",
        "ring_type",
        "spore_print_color",
        "population",
        "habitat",
    ]
    data = train_data[attrs]
    target = "target"

    # Train Data
    t = Tree()
    t.fit(data, target, max_depth=4)
    t.root.pretty_print()

    # Predict

    correct_results = 0
    ## Single Prediction
    # prediction = t.predict(test_data.iloc[0])
    # print(f"predicition: {prediction} | actual: {test_data.iloc[0]['target']}")

    ## Predict Loop
    for i in range(0, len(test_data)):
        prediction = t.predict(test_data.iloc[i])
        if prediction == test_data.iloc[i]["target"]:
            correct_results += 1
        # print(f"predicition: {prediction} | actual: {test_data.iloc[i]['target']}")

    print(f"accuracy: {correct_results/len(test_data)}")
