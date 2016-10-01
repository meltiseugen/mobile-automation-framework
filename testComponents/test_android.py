"""
Test file for the Android version of SpotOn application.
It contains the tests for: Sliding menu, Number picker, Log in, Log out, Test POIs and Menu walk-through.
"""

import unittest
import time
import os

from controller.actions import Actions
from model import appiumproxy
from model.connection import AppiumConnection
from model.device import Device


class TestAndroid(unittest.TestCase):
    """
    First test class for the Android version of the SpotOn application.
    """

    def setUp(self):
        pass

    def test_android(self):
        """
        Main test method that instantiates the required device, establishes the
        Appium connection and retrieves the
        corresponding possible actions required for running the main test cases.
        """
        appium = appiumproxy.Appium.get_remote_appium()
        appium.start(initial_wait_time=15)
        print "inner appium started"
        device = Device(ui_elements_file=os.getcwd()+"/resources/ui_elements.json",
                        device_type="Android"
                       )
        try:
            connection = AppiumConnection(url="http://localhost:4444/wd/hub",
                                          connection_file=os.getcwd()+"/resources/device_data.json",
                                          device_type="Android"
                                         )
        except Exception as e:
            print "appium client connection error... reverting and retrying"
            appium.kill_process()
            appium.start(initial_wait_time=15)
            connection = AppiumConnection(url="http://localhost:4444/wd/hub",
                                          connection_file=os.getcwd() + "/resources/device_data.json",
                                          device_type="Android"
                                          )
        actions = Actions(device, connection)
        # charlesproxy = MyCharlesProxy("/Applications/Charles.app/Contents/MacOS/Charles",
        #                               ["-headless"]
        #                               )
        # print "starting charles"
        # charlesproxy.start()
        time.sleep(10)
        print ""

        def test_sliding_menu():
            """
            Test case for asserting the behaviour of the sliding menu.
            """
            self.assertFalse(actions.check_for_element("login"))
            actions.click_on_menu_button()
            self.assertTrue(actions.check_for_element("login"))
            actions.tap_screen(930, 130)

        def test_number_picker():
            """
            Test case for asserting the behaviour of the time picker.
            """
            time.sleep(4)
            actions.swipe_on_wheel(-50)
            time.sleep(5)
            print "wheel value is " + actions.get_wheel_value()
            self.assertEqual(actions.get_wheel_value(), "10 min")
            actions.swipe_on_wheel(50)
            time.sleep(5)
            print "wheel value is " + actions.get_wheel_value()
            self.assertEqual(actions.get_wheel_value(), "5 min")
            time.sleep(5)

        def test_login():
            """
            Test case for asserting the log in process.
            """
            time.sleep(2)
            print "clicking menu button"
            actions.click_on_menu_button()
            time.sleep(5)
            if actions.android_get_logged_user() == "Log In":
                print "clicking login"
                actions.click_on_login()
                time.sleep(10)
                print "logging in"
                actions.android_osm_login("summer_internship", "internship2016")
                time.sleep(8)
                self.assertEqual(actions.android_get_logged_user(), "summer_internship")
                time.sleep(3)
            else:
                test_logout()
                actions.close_menu(device_os="android")
                test_login()

        def test_logout():
            """
            Test case for asserting the log out process .
            """
            if actions.check_for_element("login"):
                actions.android_osm_logout()
            else:
                actions.click_on_menu_button()
                actions.android_osm_logout()
            self.assertEqual(actions.android_get_logged_user(), "Log In")

        def test_menu_walkthrough():
            """
            Test case for asserting the behaviour of the walk-through accessible from the menu.
            """
            # actions.click_on_menu_button()
            time.sleep(3)
            actions.click_on_walkthrough(device_os="android")
            time.sleep(3)
            actions.android_parse_walkthrough()

        def test_find():
            """
            Test case for the results received for the given time frame.
            """
            actions.swipe_on_wheel(-50)
            time.sleep(3)
            actions.click_on_find()
            time.sleep(3)
            while not actions.check_for_element("View_title", True):
                continue

            actions.swipe_on_screen(550, 1150, 0, -200)
            actions.swipe_on_screen(550, 1150, 0, -200)
            time.sleep(10)

        # def test_pois():
        #     """
        #     Test case for verifying that the returned POIs are within the bounding box.
        #     """
        #     import re
        #
        #     def contains_number(string):
        #         """
        #         Inner method that checks if a string contains a number.
        #         :param string: The input string.
        #         :return: returns True if the string contains a number or False otherwise.
        #         """
        #         return bool(re.search(r'\d', string))
        #
        #     def filter_json_response_locations(json_data):
        #         """
        #         Inner method that filters the POIs with name, lat and log from the jackson response from the session.
        #         :param json_data: the jackson data.
        #         :return: returns a list of tuples with two elements(longitude, latitude).
        #         """
        #         coodrdinates = []
        #         for location in json_data["elements"]:
        #             if "tags" in location and "lon" in location and "lat" in location:
        #                 if "name" in location["tags"]:
        #                     if not contains_number(location["tags"]["name"]):
        #                         coodrdinates.append((location["lon"], location["lat"]))
        #         return coodrdinates
        #
        #     def parse_request(request_body):
        #         """
        #         Inner method that returns the 4 coordinates from the request body.
        #         :param request_body: The request body(text).
        #         :return: returns a tuple with 4 elements where the first two are the coordinates for the top-left point
        #         and the last two are the coordinates for the bottom-right point.
        #         """
        #         start = request_body.find("node(")
        #         start = start + 5
        #         coords = ""
        #         while not request_body[start] == ")":
        #             coords = coords + request_body[start]
        #             start = start + 1
        #         coords = coords.split(",")
        #         coords_tuple = (coords[0], coords[1], coords[2], coords[3])
        #         return coords_tuple
        #
        #     def verify_bbox_membership(bbox, location_coords):
        #         """
        #         Inner method that verifies if the location is inside the bounding box.
        #         :param bbox: The coordinates for the bounding box.
        #         :param location_coords: The coordinates for the location.
        #         :return: Returns True if the the location is inside the bounding box or False otherwise.
        #         """
        #         bbox_x1 = bbox[0]
        #         bbox_y1 = bbox[1]
        #         bbox_x2 = bbox[2]
        #         bbox_y2 = bbox[3]
        #
        #         point_x = location_coords[1]
        #         point_y = location_coords[0]
        #         # print str(bbox_x1) + "<=" + str(point_x) + " and " + str(point_x) + "<=" + str(bbox_x2) + " and " + str(bbox_y2) + "<=" + str(point_y) + " and " + str(point_y) + "<=" + str(bbox_y1)
        #         if float(bbox_x1) <= float(point_x) <= float(bbox_x2) and \
        #            float(bbox_y1) <= float(point_y) <= float(bbox_y2):
        #             return True
        #         else:
        #             return False
        #
        #     def get_request(file_name):
        #         """
        #         Inner method that extracts the 4 coordinates from the saved session file.
        #         :param file_name: The name of the session file.
        #         :return: Returns a tuple with the 4 coordinates of the bounding box.
        #         """
        #         with open(file_name) as session:
        #             r = session.read()
        #             return parse_request(r)
        #
        #     actions.swipe_on_wheel(-50)
        #     time.sleep(3)
        #
        #
        #     print "start recording"
        #     charlesproxy.record()
        #     time.sleep(10)
        #     actions.click_on_find()
        #     print "waiting"
        #     while not actions.check_for_element("View_title", True):
        #         continue
        #     time.sleep(10)
        #     print "saving session"
        #     charlesproxy.save_session(os.getcwd() + "/outputs", "request-and-response.txt", format_type="export-xml")
        #     print "saved"
        #     print "got the request"
        #     response = charlesproxy.get_response(format_type="export-xml",
        #                                          tag="body", attrs={"decoded": "true"},
        #                                          tag_index=0
        #                                          )
        #     print "got the response"
        #     response = response[30:]
        #     response = response[:-10]
        #     json_response = json.loads(response)
        #     print "filtering response"
        #     locations = filter_json_response_locations(json_response)
        #     print "filtering request"
        #     bbox_coords = get_request(os.getcwd()+"/outputs/request-and-response.txt")
        #     print bbox_coords
        #     checked_locations = []
        #     for location in locations:
        #         checked_locations.append(verify_bbox_membership(bbox_coords, location))
        #     print all(checked_locations)
        #     time.sleep(5)
        #     print "click on result"
        #     actions.click_on_result(device_os="android", index=3)
        #     print "click on edit"
        #     actions.click_on_edit()
        #     print "click on add"
        #     actions.click_on_add()


        def test_poi_update():
            actions.swipe_on_wheel(-50)
            time.sleep(3)
            actions.click_on_find()
            while not actions.check_for_element("View_title", True):
                continue
            actions.click_on_result(device_os="android", index=3)
            actions.click_on_edit()
            actions.click_on_add()
            time.sleep(3)

        def test_flow_one():
            test_login()
            test_menu_walkthrough()
            # test_pois()
            # time.sleep(2)
            # print "click on menu"
            # actions.click_on_menu_button()
            # time.sleep(2)
            # print "logging out"
            # test_logout()

        time.sleep(2)
        test_flow_one()
        time.sleep(10)
        # charlesproxy.close()
        connection.close_connection()
        appium.close()

    def tearDown(self):
        pass
