from paga_objects.conftest import setup
from paga_objects.elements.text_box_and_radio_buttons import Textbox_and_buttons
import pytest


@pytest.mark.usefixtures("setup")
class TestTextBox:

    @pytest.mark.sanity
    def test_text(self):
        obj = Textbox_and_buttons(self.driver)
        obj.text_box()

    def test_checkbox_click(self):
        obj = Textbox_and_buttons(self.driver)
        obj.click_on_checkbox()

    # @pytest.mark.sanity
    def test_radio_buttons_click(self):
        obj = Textbox_and_buttons(self.driver)
        obj.click_on_radio_buttons()
