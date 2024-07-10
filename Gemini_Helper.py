import vertexai
import os

from vertexai.generative_models import GenerativeModel, Part

#os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="USE_YOUR_SERVICE_ACCOUNT_JSON_FILE"
#project_id = "YOUR_PROJECT_ID"

vertexai.init(project=project_id, location="us-central1")
model = GenerativeModel(model_name="gemini-1.5-flash")

def generate_prompt():
    prompt_template = """
    You are a report reader. Your task is to read the test report and check the values are in the range or not.
    Range should be depend on gender and age. Suggest some tips on the same.

    You must respond in the following json format:
    [{
    "RESULT": "YOUR_RESULT_HERE"
    }]

    For example:
    "TEST": "Hemoglobin is 10 grams of 26 year old male in correct range or not?",
    "RESULT": "Hemoglobin is fine. The normal range for hemoglobin levels is 12 grams per deciliter to 17.4 grams
     per deciliter of blood for adults."
    """
    return prompt_template

def generate_report_summary(gender, age, txt):
    try:
        print('--Execution started--')
        Question = f"{txt} of {age} year old {gender}."
        prompt = generate_prompt()
        contents = [Question, prompt]
        print(Question)
        response = model.generate_content(contents)
        response = response.text
        response = response.replace("```json", "").replace("```", "")
        print('--Execution completed--')
        return response
    except Exception as e:
        print(e)

if __name__ == "__main__":
    print(generate_report_summary('Male','30','Hemoglobim 18 grams'))