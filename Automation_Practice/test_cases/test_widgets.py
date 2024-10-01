import pytest
from paga_objects.conftest import setup
from paga_objects.widgets.widgets_features import Widgets


@pytest.mark.usefixtures("setup")
class TestWidgets:

    # @pytest.mark.sanity
    def test_accordian(self):
        obj = Widgets(self.driver)
        obj.check_accordian()

    @pytest.mark.sanity
    def test_auto_complete(self):
        obj = Widgets(self.driver)
        obj.check_auto_complete()

