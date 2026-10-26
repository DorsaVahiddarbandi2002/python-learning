import json
from pathlib import Path
DATA_FILE = Path(__file__).with_name("nutrition_data.json")


def save_diary(diary):
    """Save the food diary to a JSON file."""

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(diary, file, indent=4)


def load_diary():
    """Load the food diary from a JSON file."""

    if not DATA_FILE.exists():
        return []

    with DATA_FILE.open(encoding="utf-8") as file:
        return json.load(file)

    
def calculate_totals(diary):
    """Calculate total calories and macronutrients in the diary."""

    totals = {
        "calories": 0.0,
        "protein": 0.0,
        "carbs": 0.0,
        "fat": 0.0,
    }

    for entry in diary:
        for nutrient in totals:
            totals[nutrient] += entry[nutrient]

    return totals


def calculate_macro_percentages(totals):
    """Calculate the percentage of calories from each macronutrient."""

    protein_calories = totals["protein"] * 4
    carbs_calories = totals["carbs"] * 4
    fat_calories = totals["fat"] * 9

    total_macro_calories = (
        protein_calories + carbs_calories + fat_calories
    )

    if total_macro_calories == 0:
        return {
            "protein": 0.0,
            "carbs": 0.0,
            "fat": 0.0,
        }

    return {
        "protein": protein_calories / total_macro_calories * 100,
        "carbs": carbs_calories / total_macro_calories * 100,
        "fat": fat_calories / total_macro_calories * 100,
    }


def add_food(diary, food, grams):
    """Add a food serving to the daily food diary."""

    nutrition = calculate_nutrition(food, grams)

    diary.append({
        "food": food,
        "grams": grams,
        **nutrition,
    })


def remove_food(diary, index):
    """Remove a food entry from the diary by its index."""

    if index < 0 or index >= len(diary):
        raise ValueError("Invalid food number.")

    return diary.pop(index)


import math


def calculate_nutrition(food, grams):
    """Calculate nutrition values for a given food and serving size."""

    if not isinstance(food, str) or food not in FOOD_DATABASE:
        raise ValueError("Food not found.")

    if (
        isinstance(grams, bool)
        or not isinstance(grams, (int, float))
        or not math.isfinite(grams)
        or grams <= 0
    ):
        raise ValueError("Grams must be a positive finite number.")

    nutrition = FOOD_DATABASE[food]
    factor = grams / 100

    return {
        "calories": nutrition["calories"] * factor,
        "protein": nutrition["protein"] * factor,
        "carbs": nutrition["carbs"] * factor,
        "fat": nutrition["fat"] * factor,
    }


FOOD_DATABASE = {
    "egg": {
        "calories": 155,
        "protein": 13,
        "carbs": 1.1,
        "fat": 11,
    },
    "rice": {
        "calories": 130,
        "protein": 2.7,
        "carbs": 28,
        "fat": 0.3,
    },
    "chicken": {
        "calories": 165,
        "protein": 31,
        "carbs": 0,
        "fat": 3.6,
    },
    "banana": {
        "calories": 89,
        "protein": 1.1,
        "carbs": 22.8,
        "fat": 0.3,
    },
}


def main():
    diary = load_diary()

    while True:
        print("\n========== NUTRITION TRACKER ==========")
        print("1. Add Food")
        print("2. View Food Diary")
        print("3. View Daily Summary")
        print("4. Remove food")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            food = input(
                "Food (egg, rice, chicken, banana): "
            ).strip().lower()

            try:
                grams = float(input("Serving size in grams: "))

                add_food(diary, food, grams)
                save_diary(diary)
                print("Food added successfully!")

            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "2":
            if not diary:
                print("Your food diary is empty.")
            else:
                for entry in diary:
                    print(
                        f"{entry['food'].title()} - "
                        f"{entry['grams']:.1f} g - "
                        f"{entry['calories']:.1f} kcal"
                    )

        elif choice == "3":
            totals = calculate_totals(diary)
            percentages = calculate_macro_percentages(totals)

            print("\n========== DAILY SUMMARY ==========")
            print(f"Calories: {totals['calories']:.1f} kcal")
            print(
                f"Protein:  {totals['protein']:.1f} g "
                f"({percentages['protein']:.1f}% of macro calories)"
            )
            print(
                f"Carbs:    {totals['carbs']:.1f} g "
                f"({percentages['carbs']:.1f}% of macro calories)"
            )
            print(
                f"Fat:      {totals['fat']:.1f} g "
                f"({percentages['fat']:.1f}% of macro calories)"
            )

        elif choice == "4":
            if not diary:
                print("Your food diary is empty.")
            else:
                for index, entry in enumerate(diary, start=1):
                    print(
                        f"{index}. {entry['food'].title()} - "
                        f"{entry['grams']:.1f} g - "
                        f"{entry['calories']:.1f} kcal"
                    )

                try:
                    number = int(input("Enter food number to remove: "))
                    removed = remove_food(diary, number - 1)
                    save_diary(diary)
                    print(f"{removed['food'].title()} removed successfully!")

                except ValueError as error:
                    print(f"Error: {error}")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()

