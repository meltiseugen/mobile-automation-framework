"""
Test module regarding walk-through feature
"""
from settings import Settings
from src.TestFlows.MainFlowConfig.Flow import Flow
from src.model.UIElements.UIButton import UIButton
from src.model.decorators.test_case import test_case
from src.model.decorators.test_suite import test_suite
from src.model.platform import Platform

from ui import UI


@test_suite("WalkThrough")
class WalkThroughFlow(Flow):
    """
    Test suite related to the validation of the walk-through feature
    """

    def __init__(self):
        """
        setUp method.
        """
        platform = Platform(Settings.Config.ANDROID_PLATFORM_TAG)
        super().__init__(platform)

    @test_case("SP-0001")
    def test1(self, **kwargs):
        """
        Test case validating the number of walk-through pages.
        """
        menu_button = UIButton(self.controller, UI.MENU_BUTTON_TAG)
        walk_through_button = UIButton(self.controller, UI.WALKTHROUGH_BUTTON_TAG)
        walk_through_next_button = UIButton(self.controller, UI.WALKTHROUGH_NEXT_TAG)
        walk_through_done_button = UIButton(self.controller, UI.WALKTHROUGH_DONE_TAG)

        menu_button.click()
        walk_through_button.click()
        pages_counter = 0
        while not walk_through_done_button.is_visible():
            walk_through_next_button.click()
            pages_counter += 1
        assert pages_counter == kwargs['test_data']['number of pages']
        walk_through_done_button.click()

        self.finalize()
