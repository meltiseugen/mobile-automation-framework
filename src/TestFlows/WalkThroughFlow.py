"""

"""
from src.TestFlows.MainFlowConfig.Flow import Flow
from src.model.UIElements.UIButton import UIButton


class WalkThroughFlow(Flow):
    """

    """

    def run(self):

        menu_button = UIButton(self.controller, "menu_tag")
        walk_through_button = UIButton(self.controller, "walk_though_tag")
        walk_through_next_button = UIButton(self.controller, "walk_though_next_tag")
        walk_through_done_button = UIButton(self.controller, "walk_though_done_tag")

        menu_button.click()
        walk_through_button.click()
        while not walk_through_done_button.is_visible():
            walk_through_next_button.click()
        walk_through_done_button.click()

        self.finalize()
