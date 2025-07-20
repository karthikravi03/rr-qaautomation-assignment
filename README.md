# 🎬 Movie Filter Automation Testing

###### This project validates movie listings on a web application by applying filters such as start year, end year, and ratings using Python, Selenium, and Pytest.


## 1. Clone the Repository

git clone [https://github.com/your-org/movie-filter-automation.git](https://github.com/karthikravi03/rr-qaautomation-assignment.git)
cd movie-filter-automation

## 2. Create Virtual Environment

python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

## 3. Install Dependencies

pip install -r requirements.txt

## 4. Run Test 

pytest -v -s --html=Reports/report.html --self-contained-html

### 🧰 Tools Used

* Python 3.9+
* Selenium
* Pytest
* Allure / HTML Reports (Optional)
* Logging

# 🧩 CI/CD Integration with Jenkins

## Jenkins Configuration

Install Required Plugins
Git Plugin
ShiningPanda (for Python virtualenv)
HTML Publisher (for custom reports)

Jenkinsfile or Freestyle Steps:

### Clone repository
git clone [https://your-repo-url.git](https://github.com/karthikravi03/rr-qaautomation-assignment.git)

### Setup virtual environment
python3 -m venv venv
source venv/bin/activate

### Install dependencies
pip install -r requirements.txt

### Run Selenium tests
pytest -v -s --html=Reports/report.html --self-contained-html

### Publish HTML reports (optional)


### 🧪 CI/CD Integration with GitLab CI
#### .gitlab-ci.yml Sample

stages:
  - test

selenium_tests:
  stage: test
  image: python:3.9
  before_script:
    - python -m venv venv
    - source venv/bin/activate
    - pip install -r requirements.txt
  script:
    - pytest -v -s --html=Reports/report.html --self-contained-html
  artifacts:
    paths:
      - output/customreport/
    when: always


### 📊 Reports & Logs
Custom HTML Reports: Located under output/customreport/detailreport.html

Logs & Step Status: Captured using pytest.get_step_status() in conftest.
