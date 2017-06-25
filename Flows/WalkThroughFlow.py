"""

"""
from settings import Settings
from src.TestFlows.MainFlowConfig.Flow import Flow
from src.model.UIElements.UIButton import UIButton
from src.model.decorators.test_case import test_case
from src.model.decorators.test_suite import test_suite
from src.model.platform import Platform


@test_suite("WalkThrough")
class WalkThroughFlow(Flow):
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
    def test1(self, **kwargs):
        menu_button = UIButton(self.controller, "B_menu")
        walk_through_button = UIButton(self.controller, "B_walkthrough_loggedout")
        walk_through_next_button = UIButton(self.controller, "B_walkthrough_next")
        walk_through_done_button = UIButton(self.controller, "B_walkthrough_start")

        menu_button.click()
        walk_through_button.click()
        while not walk_through_done_button.is_visible():
            walk_through_next_button.click()
        walk_through_done_button.click()

        self.finalize()  # tearDown method
