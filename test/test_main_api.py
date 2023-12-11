from fastapi.testclient import TestClient
from run import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "Hello": "Welcome to the mental health prediction API!"
    }


def test_predict_positive_case():
    """
    Test the predict endpoint with data that is expected
    to return a positive prediction.
    """
    test_data = {
        "age": 30,
        "gender": "Male",
        "country": "United States of America",
        "state": "California",
        "is_self_employed": False,
        "is_family_history_of_mental_illness": "No",
        "interference_with_work": "Sometimes",
        "number_of_employees_in_organization": "100-500",
        "is_employer_tech_company": True,
        "mental_health_benefits": "Yes",
        "mental_healthcare_options": "Yes",
        "mental_health_employee_wellness_program": "Yes",
        "mental_health_employee_resources": "Yes",
        "employee_anonymity_protected": "Yes",
        "mental_health_leave": "Somewhat easy",
        "willingness_to_discuss_with_coworkers": "Yes",
        "willingness_to_discuss_with_supervisors": "Yes"
    }

    response = client.post("/predict", json=test_data)
    print(response.content)
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert response.json()["prediction"] == 'True'


def test_predict_negative_case():
    """
    Test the predict endpoint with data that is expected
    to return a negative prediction.
    """
    test_data = {
        "age": 25,
        "gender": "Male",
        "country": "United States of America",
        "state": "Nebraska",
        "is_self_employed": False,
        "is_family_history_of_mental_illness": False,
        "interference_with_work": "Not applicable to me",
        "number_of_employees_in_organization": "26-100",
        "is_employer_tech_company": True,
        "mental_health_benefits": "Yes",
        "mental_healthcare_options": "I don't know",
        "mental_health_employee_wellness_program": "No",
        "mental_health_employee_resources": "Yes",
        "employee_anonymity_protected": "Yes",
        "mental_health_leave": "Somewhat easy",
        "willingness_to_discuss_with_coworkers": "No",
        "willingness_to_discuss_with_supervisors": "No"
    }

    response = client.post("/predict", json=test_data)
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert response.json()["prediction"] == 'False'


def test_predict_invalid_data():
    """
    Test the predict endpoint with invalid data
    to ensure it handles errors gracefully.
    """
    test_data = {
        "age": -5,
        "gender": "Unknown",
    }

    response = client.post("/predict", json=test_data)
    assert response.status_code == 422
