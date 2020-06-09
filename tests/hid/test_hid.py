import pytest

from common.hid.hid import Hid


@pytest.mark.parametrize("prefix", ("RQ", "RC"))
def test_hid_generate(prefix):
    hid_gen = Hid(prefix)
    assert hid_gen().startswith(prefix)
