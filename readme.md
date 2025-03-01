# Project Title
Selenium Automation Framework for OrangeHRM using Python and Pytest

## Description
This is a robust automation testing framework built using **Selenium**, **Python**, and **pytest**.
It is designed to automate some basic testcases for OrangeHRM web application including searching , filtering and creating new users. 
The framework follows the **Page Object Model (POM)** design pattern for better maintainability and scalability. 
It can run with browser in foreground as well as headlessly based on the "--headless" arguments provided in pytest.ini file.
It supports Chrome or Edge Browser.

## Features
- **Page Object Model (POM)**: Encapsulates web elements and actions in separate page files and classes.
- **Data-Driven Testing**: Supports CSV files for test data.
- **Logging**: Integrated logging for better debugging and tracking.
- **Reporting**: Generates HTML reports with screenshots for failed tests.
- **Cross-Browser Testing**: Supports Chrome and Edge browsers.
- **Environment Configuration**: Uses `.ini` files for pytest configurations.

## Install dependencies
- **requirements.txt**: Install requirements by running the following command in terminal "pip install -r requirements.txt".
This will setup the packages required to run this project.

## Handling Flaky Tests
To handle flaky tests, the framework uses the `pytest-rerunfailures` plugin. Failed tests are automatically rerun **twice** before being marked as failed. This helps to mitigate intermittent issues caused by network latency, timing issues, or other environmental factors.

## Running Tests
- To run the tests, go to testCases and just type **pytest** in terminal

## Parallel Execution
- To run tests parallely , specify it in pytest.ini using argument **"-n" number_of_parallel_executions**.
#pytest # selenium #python #automation #QA