"""
A file used to define actions for interacting with the application
or to perform a certain set of operations.
"""

import time


class Actions(object):
    """
    A class that defines a set of operations used to interact or to
    perform a sequential interaction with the application.
    """

    def __init__(self, device, connection):
        """
        Constructor for the class.
        :param device: a variable of type model.device.Device that
                       contains the device information with the UI
                       elements of the application.
        :param connection: a variable of type model.connection.AppiumConnection
                           that holds the connection to the Appium server and
                           allows the interaction with the device.
        """
        self.__device = device
        self.__connection = connection

    def click_on_menu_button(self):
        """
        Method that clicks on the menu button from the application.
        """
        menu_path = self.__device.get_xpath_of_element("B_menu")
        self.__connection.click_element(menu_path)

    def close_menu(self, device_os):
        if device_os == "android":
            self.swipe_on_screen(500, 500, -200, 0)
        elif device_os == "ios":
            b_menu_menu = self.__device.get_xpath_of_element("B_menu_menu")
            self.__connection.click_element(b_menu_menu)
    def swipe_on_wheel(self, wheel1_swipe_to_y):
        """
        Method that performs a VERTICAL swipe action RELATIVE to the Number Picker position.
        :param wheel1_swipe_to_y: Y position where to move the swipe RELATIVE to the Number
                                  Picker position:
                                    - POSITIVE value means that the swipe moves DOWNWARDS.
                                    - NEGATIVE value means that the swipe moves UPWARDS.
        """
        edit_number_xpath = self.__device.get_xpath_of_element("E_number")
        edit_number_elem = self.__connection.get_element(edit_number_xpath)

        swipe_action = self.__connection.get_touch_action()
        swipe_action.press(edit_number_elem)\
                    .move_to(x=0, y=wheel1_swipe_to_y)\
                    .release()\
                    .perform()

    def check_for_element(self, name, override_default_path=False):
        """
        Method that checks if an element, given by name, is displayed on the application screen.
        :param name: the name of the element it needs to check for.
        :param override_default_path: a param that changes the behaviour of the function:
                                      - if TRUE, the device class will merge the default path
                                        with the relative path of the element.
                                      - if FALSE, the device class will return the path relative
                                        to the element name.
        :return: returns True if the element is displayed or False if it fails to find the element
                 or the element is not displayed.
        """
        element_xpath = self.__device.get_xpath_of_element(name, override_default_path)
        try:
            return self.__connection.get_element(element_xpath).is_displayed()
        except Exception:
            return False

    def get_wheel_value(self):
        """
        Method that returns the current value displayed on the Number Picker.
        :return: returns the current string value displayed on the Number Picker.
        """
        wheel1_xpath = self.__device.get_xpath_of_element("E_number")
        wheel1_elem = self.__connection.get_element(wheel1_xpath)
        return wheel1_elem.text

    def tap_screen(self, coord_x, coord_y):
        """
        Method that performs a tap on the screen at the desired given coordinates.
        :param coord_x: the x coordinate.
        :param coord_y: the y coordinate.
        """
        self.__connection.tap([(coord_x, coord_y)])

    def reset_wheel(self):
        """
        Method that resets the Number Picker to the starting, default, value.
        """
        wheel1_value = self.get_wheel_value()
        print "resetting wheel"
        while not wheel1_value == "5":
            self.swipe_on_wheel(100)
            wheel1_value = self.get_wheel_value()

    def click_on_login(self):
        """
        Method that clicks on the log in button from the menu.
        """
        login_xpath = self.__device.get_xpath_of_element("login")
        self.__connection.click_element(login_xpath)

    @staticmethod
    def send_keys_to_element(element, keys):
        """
        Method that sends a string value to the given element; usually so that the element
        will display that value.
        :param element: the element which is required to display that value.
        :param keys: the string value that needs to be sent to the element.
        """
        element.send_keys(keys)

    def swipe_on_screen(self, coord_x1, coord_y1, coord_x2, coord_y2):
        """
        Method that is used to perform a custom swipe on the screen. It performs a swipe action
        from the point (coord_x1, coord_y1) to the point (coord_x2, coord_y2). NOTE that the
        point (coord_x2, coord_y2) is RELATIVE to the first point (coord_x1, coord_y1).
        :param coord_x1: x value of the first point.
        :param coord_y1: y value of the first point.
        :param coord_x2: x value of the second point relative to the x value from the first point.
        :param coord_y2: y value of the second point relative to the y value from the first point.
        """
        swipe_action = self.__connection.get_touch_action()
        swipe_action.press(x=coord_x1, y=coord_y1)\
                    .move_to(x=coord_x2, y=coord_y2)\
                    .release()\
                    .perform()

    def android_osm_login(self, username, password):
        """
        Method that performs a sequence of interactions that achieve the log in process on the
        OSM WebView for the Android application.
        :param username: the username given as string for the OSM account.
        :param password: the password given as string for the OSM account.
        """
        user_edit_box_xpath = self.__device.get_xpath_of_element("E_OSM_username", True)
        user_edit_box_elem = self.__connection.get_element(user_edit_box_xpath)
        self.send_keys_to_element(user_edit_box_elem, username)

        pass_edit_box_xpath = self.__device.get_xpath_of_element("E_OSM_password", True)
        pass_edit_box_elem = self.__connection.get_element(pass_edit_box_xpath)
        self.send_keys_to_element(pass_edit_box_elem, password)

        self.__connection.hide_keyboard()

        login_xpath = self.__device.get_xpath_of_element("B_OSM_login", True)
        self.__connection.click_element(login_xpath)

        time.sleep(8)
        self.swipe_on_screen(550, 1150, 0, -200)
        self.swipe_on_screen(550, 1150, 0, -200)
        time.sleep(8)

        grant_access_xpath = self.__device.get_xpath_of_element("B_OSM_grant_access", True)
        self.__connection.click_element(grant_access_xpath)

    def android_get_logged_user(self):
        """
        Method that returns the value of the element where the name of the logged user
        is usually displayed.
        :return: returns the name of the current logged user or 'User' if there is no current user.
        """
        user_xpath = self.__device.get_xpath_of_element("user")
        user_elem = self.__connection.get_element(user_xpath)
        return user_elem.text

    def android_osm_logout(self):
        """
        Method that performs a sequence of interactions that achieve the log out process from
        the menu for the Android application.
        The method is only executed if there is a user logged in.
        """
        if not self.android_get_logged_user() == "User":
            logout_xpath = self.__device.get_xpath_of_element("logout")
            self.__connection.click_element(logout_xpath)
            time.sleep(3)
            logout_confirm_xpath = self.__device.get_xpath_of_element("B_logout", True)
            self.__connection.click_element(logout_confirm_xpath)

    def ios_osm_login(self, username, password):
        """
        Method that performs a sequence of interactions that achieve the log in process on
        the OSM WebView for the iOS application.
        :param username: the username given as string for the OSM account.
        :param password: the password given as string for the OSM account.
        """
        user_edit_box_xpath = self.__device.get_xpath_of_element("E_OSM_username", True)
        user_edit_box_elem = self.__connection.get_element(user_edit_box_xpath)
        self.__connection.click_element(user_edit_box_xpath)
        self.send_keys_to_element(user_edit_box_elem, username)

        pass_edit_box_xpath = self.__device.get_xpath_of_element("E_OSM_password", True)
        pass_edit_box_elem = self.__connection.get_element(pass_edit_box_xpath)
        self.__connection.click_element(pass_edit_box_xpath)
        self.send_keys_to_element(pass_edit_box_elem, password)

        self.__connection.hide_keyboard()

        login_xpath = self.__device.get_xpath_of_element("B_OSM_login", True)
        self.__connection.click_element(login_xpath)

        time.sleep(3)
        grant_access_xpath = self.__device.get_xpath_of_element("B_OSM_grant_access", True)
        while not self.check_for_element("B_OSM_grant_access"):
            self.swipe_on_screen(250, 250, 0, -150)

        self.__connection.click_element(grant_access_xpath)

    def ios_osm_logout(self):
        """
        Method that performs a sequence of interactions that achieve the log out process from
        the menu for the iOS application.
        """
        logout_xpath = self.__device.get_xpath_of_element("logout")
        self.__connection.click_element(logout_xpath)
        b_logout_xpath = self.__device.get_xpath_of_element("B_logout")
        self.__connection.click_element(b_logout_xpath)

    def ios_get_logged_user(self):
        """
        Method that returns the value of the element where the name of the logged user
        is usually displayed.
        :return: returns the name of the current logged user or 'User' if there is no current user.
        """
        user_xpath = self.__device.get_xpath_of_element("login_text")
        user_elem = self.__connection.get_element(user_xpath)
        return user_elem.text

    def click_on_walkthrough(self, device_os):
        """
        Method that clicks on the walk-through button from the menu.
        """
        if device_os == "android":
            if self.android_get_logged_user() == "Log In":
                walthrough_xpath = self.__device.get_xpath_of_element("B_walkthrough_loggedout")
                self.__connection.click_element(walthrough_xpath)
            else:
                walthrough_xpath = self.__device.get_xpath_of_element("B_walkthrough_loggedin")
                self.__connection.click_element(walthrough_xpath)
        elif device_os == "ios":
            if self.ios_get_logged_user() == "Log in":
                walthrough_xpath = self.__device.get_xpath_of_element("B_walkthrough_loggedout")
                self.__connection.click_element(walthrough_xpath)
            else:
                walthrough_xpath = self.__device.get_xpath_of_element("B_walkthrough_loggedin")
                self.__connection.click_element(walthrough_xpath)

    def android_parse_walkthrough(self):
        """
        Method that performs a sequence of interactions that parse through the
        walk-through interface for the Android application.
        """
        next_xpath = self.__device.get_xpath_of_element("B_walkthrough_next", True)
        while self.check_for_element("B_walkthrough_next", True):
            self.__connection.click_element(next_xpath)
            time.sleep(2)

        print "finished while"
        start_xpath = self.__device.get_xpath_of_element("B_walkthrough_start", True)
        self.__connection.click_element(start_xpath)

    def ios_parse_walkthrough(self):
        """
        Method that performs a sequence of interactions that parse through the
        walk-through interface for the iOS application.
        """
        next_xpath = self.__device.get_xpath_of_element("B_walkthrough_next", True)
        while self.check_for_element("B_walkthrough_next", True):
            self.__connection.click_element(next_xpath)
            if not self.__connection.get_element(next_xpath).text == "Next":
                break
        time.sleep(3)
        start_xpath = self.__device.get_xpath_of_element("B_walkthrough_start", True)
        self.__connection.click_element(start_xpath)

    def get_connectivity(self):
        """
        Method that returns the current network status of the device.
        MIGHT ONLY WORK FOR ANDROID.
        :return: returns the network state of the device:
                    - NO INTERNET CONNECTION = 0
                    - WIFI INTERNET CONNECTION = 2
                    - DATA INTERNET CONNECTION = 4
                    - ALL INTERNET CONNECTION = 6
        """
        return self.__connection.get_network_connection()

    def turn_location_on(self):
        """
        Method that toggles location services on.
        """
        self.__connection.turn_location_on()

    def click_on_find(self):
        """
         Method that performs the click action on the 'Find' button from the main screen.
        """
        b_find_xpath = self.__device.get_xpath_of_element("B_find")
        self.__connection.click_element(b_find_xpath)

    def ios_check_for_view(self, title):
        view_title_xpath = self.__device.get_xpath_of_element("View_title")
        view_title = self.__connection.get_element(view_title_xpath)
        return view_title.text == title

    def click_on_result(self, device_os, index=1):
        if device_os == "ios":
            result_xpath = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[" + str(index) + "]"
            self.__connection.click_element(result_xpath)
        elif device_os == "android":
            result_xpath = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[" + str(index) + "]"
            self.__connection.click_element(result_xpath)

    def click_on_add(self):
        add_xpath = self.__device.get_xpath_of_element("B_Add", True)
        self.__connection.click_element(add_xpath)

    def click_on_edit(self):
        edit_xpath = self.__device.get_xpath_of_element("B_Edit", True)
        self.__connection.click_element(edit_xpath)
