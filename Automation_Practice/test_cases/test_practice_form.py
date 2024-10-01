import pytest
from paga_objects.forms.practice_form import PracticeForm
from paga_objects.conftest import setup


@pytest.mark.usefixtures("setup")
class TestPracticeForm:

    @pytest.mark.sanity
    def test_practice_form(self):
        obj=PracticeForm(self.driver)
        obj.practice_form()

