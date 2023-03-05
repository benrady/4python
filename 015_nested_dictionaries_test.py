

def test_keys_and_values():
    """Dictionary keys and values can be any other object, including other lists and dictionaries"""
    value = None  # Replace this
    d = {"even": [2, 4, 6], "odd": [1, 3, 5], "ratios": [{"numerator": 1.0, "denominator": 2.0}]}
    ratio = d["ratios"][value]
    assert d["odd"][value] / d["even"][value] == ratio["numerator"] / ratio["denominator"]
