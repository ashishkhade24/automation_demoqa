from paga_objects.conftest import setup
from paga_objects.elements.web_tables_buttons_and_links import Web_tables_and_links
import pytest

@pytest.mark.usefixtures("setup")
class Test_Buttons_And_Links:

    def test_web_tables(self):
        obj = Web_tables_and_links(self.driver)
        obj.create_web_table()

    def test_edit_web_table(self):
        obj = Web_tables_and_links(self.driver)
        obj.edit_web_tables()

    # @pytest.mark.sanity
    def test_delete_user(self):
        obj = Web_tables_and_links(self.driver)
        obj.delete_user()

    def test_click_on_buttons(self):
        obj = Web_tables_and_links(self.driver)
        obj.click_on_buttons()

    # @pytest.mark.sanity
    def test_click_on_links(self):
        obj = Web_tables_and_links(self.driver)
        obj.click_on_links()

    # @pytest.mark.sanity
    def test_click_on_broken_links(self):
        obj = Web_tables_and_links(self.driver)
        obj.click_on_broken_links()

    @pytest.mark.sanity
    def test_check_upload(self):
        obj = Web_tables_and_links(self.driver)
        obj.check_download_upload()

