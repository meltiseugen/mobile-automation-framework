"""

"""
from settings import Settings
from src.TestFlows.MainFlowConfig.Flow import Flow
from src.model.UIElements.UIButton import UIButton
from src.model.UIElements.UITextBox import UITextBox
from src.model.platform import Platform


@threaded()
@test_suite("Login")
class LogInFlow(Flow):
    """
    Test suite related to the validation of the walk-through feature
    """

    def __init__(self):
        """
        setUp method.
        :param platform: the type of platform on which to run the test (Android or iOS)
        """
        platform = Platform(Settings.Config.ANDROID_PLATFORM_TAG)
        super().__init__(platform)

    @test_case("SP-0001")
    def test1(self, kwargs):
        """

        :param kwargs:
        :return:
        """

        menu_button = UIButton(self.controller, "B_menu")
        log_in_button = UIButton(self.controller, "B_log_in")
        log_out_button = UIButton(self.controller, "B_log_out")
        username_text_box = UITextBox(self.controller, "TB_username")
        password_text_box = UITextBox(self.controller, "TB_password")
        submit_credentials = UIButton(self.controller, "B_submit_credentials")
        logged_in_user = UIButton(self.controller, "B_user")

        menu_button.click()
        assert logged_in_user.is_visible() is False
        log_in_button.click()
        username_text_box.set_text("username")
        password_text_box.set_text("password")
        submit_credentials.click()
        assert logged_in_user.is_visible() is True
        assert logged_in_user.text() == "username"
        log_out_button.click()

        self.finalize()  # tearDown method
