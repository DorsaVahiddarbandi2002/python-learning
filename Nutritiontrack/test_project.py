
import pytest
import project

from project import (
    add_food,
    calculate_nutrition,
    calculate_totals,
    calculate_macro_percentages,
    load_diary,
    save_diary,
    remove_food,
)



def test_calculate_nutrition():
    result = calculate_nutrition("egg", 200)

    assert result["calories"] == pytest.approx(310)
    assert result["protein"] == pytest.approx(26)


def test_calculate_nutrition_invalid_food():
    with pytest.raises(ValueError):
        calculate_nutrition("pizza", 100)


def test_add_food():
    diary = []

    add_food(diary, "banana", 100)

    assert len(diary) == 1
    assert diary[0]["food"] == "banana"
    assert diary[0]["calories"] == pytest.approx(89)


def test_calculate_totals():
    diary = []

    add_food(diary, "egg", 100)
    add_food(diary, "banana", 100)

    totals = calculate_totals(diary)

    assert totals["calories"] == pytest.approx(244)
    assert totals["protein"] == pytest.approx(14.1)


def test_invalid_serving_size():
    with pytest.raises(ValueError):
        calculate_nutrition("egg", 0)


def test_save_and_load_diary(tmp_path, monkeypatch):
    test_file = tmp_path / "nutrition_data.json"

    monkeypatch.setattr(project, "DATA_FILE", test_file)

    diary = []
    add_food(diary, "egg", 100)
    add_food(diary, "banana", 150)

    save_diary(diary)
    loaded_diary = load_diary()

    assert loaded_diary == diary


def test_remove_food():
    diary = []

    add_food(diary, "egg", 100)
    add_food(diary, "banana", 100)

    removed = remove_food(diary, 0)

    assert removed["food"] == "egg"
    assert len(diary) == 1
    assert diary[0]["food"] == "banana"


def test_remove_food_invalid_index():
    diary = []

    with pytest.raises(ValueError):
        remove_food(diary, 0)


def test_invalid_serving_size_nan():
    with pytest.raises(ValueError):
        calculate_nutrition("egg", float("nan"))


def test_invalid_serving_size_infinity():
    with pytest.raises(ValueError):
        calculate_nutrition("egg", float("inf"))


def test_invalid_food_type():
    with pytest.raises(ValueError):
        calculate_nutrition(None, 100)


def test_negative_serving_size():
    with pytest.raises(ValueError):
        calculate_nutrition("egg", -100)


def test_calculate_macro_percentages():
    totals = {
        "calories": 400,
        "protein": 20,
        "carbs": 50,
        "fat": 10,
    }

    percentages = calculate_macro_percentages(totals)

    assert percentages["protein"] == pytest.approx(80 / 370 * 100)
    assert percentages["carbs"] == pytest.approx(200 / 370 * 100)
    assert percentages["fat"] == pytest.approx(90 / 370 * 100)


def test_calculate_macro_percentages_zero():
    totals = {
        "calories": 0,
        "protein": 0,
        "carbs": 0,
        "fat": 0,
    }

    percentages = calculate_macro_percentages(totals)

    assert percentages == {
        "protein": 0.0,
        "carbs": 0.0,
        "fat": 0.0,
    }