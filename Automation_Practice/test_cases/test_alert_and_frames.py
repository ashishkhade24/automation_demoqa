import pytest
from paga_objects.conftest import setup
from paga_objects.alert_and_frames.alert_frame import AlarmFramesWindows


@pytest.mark.usefixtures("setup")
class TestAlertFrame:

    # @pytest.mark.sanity
    def test_browser_windows(self):
        obj=AlarmFramesWindows(self.driver)
        obj.check_browser_windows()

    def test_alert_handle(self):
        obj = AlarmFramesWindows(self.driver)
        obj.alerts_handle()

    # @pytest.mark.sanity
    def test_frames(self):
        obj = AlarmFramesWindows(self.driver)
        obj.check_frames()

    # @pytest.mark.sanity
    def test_nested_frames(self):
        obj = AlarmFramesWindows(self.driver)
        obj.check_nested_frames()

    @pytest.mark.sanity
    def test_modals(self):
        obj = AlarmFramesWindows(self.driver)
        obj.check_modal_dialogs()



