import pandas as pd
from decision_tree.decision_tree import Tree

if __name__ == "__main__":
    # initialise data
    df = pd.read_csv("input/mushrooms.csv")

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
    data = df[attrs]
    target = "target"

    # Train Data
    t = Tree()
    t.fit(data, target, max_depth=4)

    # Predict
    prediction = t.root.predict(
        {
            "cap_shape": "K",
            "cap_surface": "Y",
            "cap_color": "N",
            "bruises": "F",
            "odor": "Y",
            "gill_attachment": "F",
            "gill_spacing": "C",
            "gill_size": "N",
            "gill_color": "B",
            "stalk_shape": "T",
            "stalk_root": "M",
            "stalk_surface_above_ring": "S",
            "stalk_surface_below_ring": "K",
            "stalk_color_above_ring": "W",
            "stalk_color_below_ring": "W",
            "veil_type": "P",
            "veil_color": "W",
            "ring_number": "O",
            "ring_type": "E",
            "spore_print_color": "W",
            "population": "V",
            "habitat": "L",
        },
    )

    t.root.pretty_print()
