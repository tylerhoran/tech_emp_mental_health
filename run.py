from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle

with open('model/final_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('model/preprocessor.pkl', 'rb') as file:
    preprocessor = pickle.load(file)


class EmployeeData(BaseModel):
    age: float
    gender: str
    country: str
    state: str
    is_self_employed: bool
    is_family_history_of_mental_illness: bool
    interference_with_work: str
    number_of_employees_in_organization: str
    is_employer_tech_company: bool
    mental_health_benefits: str
    mental_healthcare_options: str
    mental_health_employee_wellness_program: str
    mental_health_employee_resources: str
    employee_anonymity_protected: str
    mental_health_leave: str
    willingness_to_discuss_with_coworkers: str
    willingness_to_discuss_with_supervisors: str


app = FastAPI()


@app.get("/")
def home():
    return {"Hello": "Welcome to the mental health prediction API!"}


@app.post("/predict")
async def make_prediction(employee_data: EmployeeData):
    input_data_df = pd.DataFrame([dict(employee_data)])
    input_data_df.columns = map(str.lower, input_data_df.columns)
    input_data_transformed = preprocessor.transform(input_data_df)
    prediction = model.predict(input_data_transformed)
    return {"prediction": str(prediction[0])}
