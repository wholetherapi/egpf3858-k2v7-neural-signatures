from signatures import encoder


def test_import():
    assert encoder.Config().seed == 0
