import pytest

from homemade_common.hid.hid import Categories
from homemade_common.hid.hid import Hid


@pytest.mark.parametrize("uid_type", list(Categories))
def test_hid_generate(uid_type):
    assert Hid(uid_type=uid_type).generate().startswith(uid_type.value)
