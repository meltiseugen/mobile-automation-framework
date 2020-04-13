# A QA automation framework for mobile testing 

This is a QA automation framework designed for testing mobile applications
running on Android and iOS.

### 1. Description

The idea of the framework is to encapsulate the communication with the device,
the interactions and utilities, behind interfaces and APIs in order to give the
user an easy interaction and face pacing of the test cases development

The connection between the framework and the device is handled by Appium.

### 2. The idea behind the framework

The framework executes user defined `flows` that represent the steps of the test case.
This includes basic interactions like `click`, `type`, but also `validation`.

Here is an example of a flow:
```python
log_in_button = UIButton(self.controller, "B_log_in")
username_text_box = UITextBox(self.controller, "TB_username")
password_text_box = UITextBox(self.controller, "TB_password")
submit_credentials = UIButton(self.controller, "B_submit_credentials")

menu_button.click()
assert logged_in_user.is_visible() is False
log_in_button.click()
username_text_box.set_text("username")
password_text_box.set_text("password")
submit_credentials.click()
``` 

### 3. Interfaces and APIs

#### 3.1 UI Classes

The framework offers a set of classes that represent UI elements. Each of these
classes have their own methods and are linked to a specific real UI element 
through an element ID like `TB_username`. 

There UI classes are: `UIBaseElement`, `UIButton`, `UIObject`, `UITableView`, `UITableViewChildElement`, `UITextBox`.
```python
username_text_box = UITextBox(self.controller, "TB_username")
```

#### 3.2 The Appium interface

In order to connect to the device the framework communicates to an Appium server.
in order to hide this sometomes complicated connection, as well as handling the
starting and shutdown of the service, the framework has an Appium interface class.

Each new written flow must inherit from the Flow class. The flow class is responsible
for starting and managing the Appium connection through its controllers.

This way the used needs only to focus on writing the test code, and not about 
the configurations

#### 3.3 The Charles Web Proxy interface

Sometimes the test case requires you to validate the contents of requests.
For this the framework provide an interface called `Charles`.

It gives the option to save the logs in three different formats: `xml`, `har`,
and `csv`. These files can later be parsed and validated in the test case
implementation.

Example:
```python
charles = Charles()
charles.start()
charles.record()
charles.save_session('my_session')
charles.close()
```

#### 3.4 Decorators

In order to simplify the test case logic, and also to annotate it with some
extra information, the framework has two important decorators: `

##### 3.4.1 Test Suite decorator

This is used to decorate the Flow class by providing it with a name. Example:
```python
@test_suite("MyFlow")
class MyFlow(Flow):
    pass
```

The role of this decorator is to execute all the test cases from the class
when the class is instantiated.
It only executes the methods that start with `test_`.

##### 3.4.2 Test Case decorator

The test case decorator is responsible for linking the implementation of the
test case with the test data through the test case ID. The test data file is
located in the `resources` directory and is basically a JSON file that has the
IDs of all the test cases with the respective test data.

Example:
```python
@test_case("SP-0001")
def test_1(self, **kwargs):
    print(kwargs['test_data']['key'])
```
