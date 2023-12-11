import requests

row = {
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

response = requests.post(
    url='https://tech-mental-health-985271153624.herokuapp.com/predict',
    json=row
)

print(response.status_code)
print(response.json())
