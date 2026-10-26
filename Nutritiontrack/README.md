# Nutrition Tracker

#### Video Demo: https://youtu.be/IzFPwpc5DoI

#### Description:

Nutrition Tracker is a command-line application written in Python that helps users record their food intake and monitor their daily nutritional values. I chose this project because nutrition tracking involves calculations, data management, and input validation, making it a practical way to apply the programming concepts I learned in CS50P.

The application allows users to add foods, specify serving sizes in grams, view their food diary, remove entries, and calculate daily totals for calories, protein, carbohydrates, and fat. It also calculates the percentage of calories contributed by each macronutrient.

The nutritional information is stored in a built-in database containing four foods: eggs, rice, chicken, and bananas. Values are approximate and calculated per 100 grams. The application scales these values according to the serving size entered by the user.

One important design decision was to separate the main operations into functions. This makes the code easier to maintain and allows individual functions to be tested independently. I used JSON to save the food diary so that entries persist between program sessions. I also added input validation to handle unknown foods and invalid serving sizes, including zero, negative numbers, NaN, and infinity.

Finally, I used pytest to test the application's calculations, data storage, food removal, and error handling. These tests helped me identify mistakes and improve the reliability of the program.


## Features

* Add food items to a daily food diary.
* Calculate calories, protein, carbohydrates, and fat based on serving size in grams.
* Display all recorded food items.
* Calculate daily totals for calories and macronutrients.
* Calculate the percentage of calories contributed by protein, carbohydrates, and fat.
* Remove food items from the diary.
* Save food records to a JSON file so they remain available after restarting the application.
* Validate food names and serving sizes.
* Test the main functions using pytest.

## Supported Foods

The current food database includes:

* Egg
* Rice
* Chicken
* Banana

The nutritional values are approximate and are calculated per 100 grams of each food.

## Technologies

* Python
* JSON for data storage
* pytest for automated testing

## How to Run

1. Clone or download the project.

2. Open a terminal in the project directory.

3. Run the application:

   ```bash
   python3 project.py
   ```

4. Follow the menu displayed in the terminal.

## Running the Tests

To run the automated tests, execute:

```bash
pytest -v
```

The tests cover nutritional calculations, food registration, daily totals, JSON storage, food removal, input validation, and macronutrient percentages.

## Project Structure

* `project.py`: Contains the application logic and command-line interface.
* `test_project.py`: Contains automated tests.
* `requirements.txt`: Lists the project's dependencies.
* `nutrition_data.json`: Stores the food diary when the application saves data.

## Design Decisions

I separated the nutritional calculations, food management, data storage, and command-line interface into functions. This makes the code easier to understand, test, and maintain.

The application uses JSON to store the food diary locally. This allows users to close the program and retrieve their saved records the next time they run it.

I also used pytest to test important functions and verify that invalid inputs are handled correctly.

## Future Improvements

Possible future improvements include adding more foods, supporting multiple dates, allowing users to set daily nutritional goals, and generating weekly nutrition reports.
