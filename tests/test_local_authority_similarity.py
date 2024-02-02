import local_authority_similarity

import pytest
from pathlib import Path
import pandas as pd


def test_right_number_councils():
    packages = Path("data", "packages")

    # iterate through each folder
    for folder in packages.iterdir():
        df = pd.read_csv(folder / "distance_map.csv")
        a_col = "local-authority-code_A"
        assert (
            len(df[a_col].unique()) == 394
        ), f"Wrong number of councils in {folder.name}"
