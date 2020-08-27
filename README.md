
Welcome to AllinCall. This will be your first project and you need to complete all the tasks mentioned below.

## Getting Started
1. Get a clone of this project on your local.
    ```sh
    $ git clone git@github.com:amangoeliitb/SDE-training.git
    ```
2. Make sure to create the virtual environment before start working on this project.
    ```sh
    $ virtualenv -p python3 venv
    ```
3. Install all the requirements and run the application.
    ```sh
    $ pip install -r requirements.txt
    ```
## Tasks

Your task is to create a demo app just like Zomato.

#### Problem Statement: 
When a registered user logged in they will be redirected to the restaurant page where the user can select any restaurant from the list (dropdown). After selecting the restaurant user will get the list of all the dishes with the name and price and the user can select one or multiple dishes at once. After selecting the dishes a 'Place Order' button will be shown with the total price and after ordering,  the page will show 'Your order has been placed.' and the user will be redirected to the home page.

#### Task 1
Create SignIn and SignUp functionality where a user can register and login.
1. HTML Page for SignIn and SignUp
2. SignUp Page - To register, ask these details -> Username, Name, Email, Password.
3. SignIn Page - User can sign-in using username and password.
  
Note: Make sure to add validator in email, username and name.

#### Task 2

Create models
1. Users - You can use Django User model
    1. Name
    2. Username
    3. Password
2. Restaurants
    1. Restaurant Name
    2. Restaurant Address
3. Dishes
    1. Dish Name
    2. Dish Price
    3. Restraunts in which this dish is available.
4. Order Placed
    1. User who placed the order
    2. Restaurant from which the order is placed
    3. Dish which is orders
    4. Total Price

#### Task 3

1. Create a GET API to get list of all the dishes which is being served in the selected restaurant.
2. Create a POST API which will be called when user placed the order and save all the details.

Note: Use Ajax in JavaScript to call the API and create REST API in Python. 

#### Task 4

You have to write test cases for each and every file will have its own test file
Some set of operation will have its own file

```sh
$ ./manage.py test test-folder/
File name format =>    test_{file/functionality to be tested}
$ ./manage.py test --pattern="tests_*.py"
```

Test file format (Example)
```sh
from django.test import TestCase

class UtilsSmallFunctionsWithModels(TestCase):
	# Each set of operation will have its own class
	# Name of the functionality for which you writing unit test

    def setUp(self):
		#This function will be used to initialize database or some initial condition for testing above functionalities

    def test_correct_query(self):
        # input to that function
        input_queries = ['tell me my balancd', 'i want to know salary','show me ofters', 'what is your moblie number']
         # expected output of that function
        expected_responses = ['tell me my BALANCE', 'i want to know salary','show me OFFERS', 'what is your moblie number']

        corrected_queries = []
        for query in input_queries:
            corrected = correct_query(query)
            corrected_queries.append(corrected)
        # check whether expected and obtained responses are same or not
        self.assertEqual(expected_responses, corrected_queries)
```
Comments format for test functions
On the top of every test function, comments are to be written in the following format:
```sh
"""
    function tested: <function name>
    input queries:
        <the nature of the input queries>
    expected output:
        <the nature of the output>
    checks for:
        <what does this test function do>
"""
```



#### Creating PR

After completing all the tasks you have to create a pull request in the same github repository. 

1. Create a new branch
    ```sh
        $ git checkout -b v1.0-YOUR-NAME 
    ```
2. Add and commit your code locally
    ```sh
        $ git add .
        $ git commit -m "TASK DETAILS"
    ```
3. Push your code
    ```sh
        git push origin YOUR BRANCH NAME
    ```
