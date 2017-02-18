"""

"""
from src.TestFlows.MainFlowConfig.Flow import Flow
from src.model.UIElements.UIButton import UIButton


class WalkThroughFlow(Flow):
    """

    """
    def __init__(self, platform):
        super().__init__(platform)

    def run(self):

        menu_button = UIButton(self.controller, "B_menu")
        walk_through_button = UIButton(self.controller, "B_walkthrough_loggedout")
        walk_through_next_button = UIButton(self.controller, "B_walkthrough_next")
        walk_through_done_button = UIButton(self.controller, "B_walkthrough_start")

        menu_button.click()
        walk_through_button.click()
        while not walk_through_done_button.is_visible():
            walk_through_next_button.click()
        walk_through_done_button.click()

        self.finalize()
