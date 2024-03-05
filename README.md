# Cynario Project

### Install dependencies
`pip install -r requirements.txt`
### Running the Application
`uvicorn main:app`

### Accessing the Application
After starting the server, you can access the application in your web browser at:


### API Endpoints
* http://localhost:8000/checkin?user=danny&task=work - will create a task named "work" for user "danny"
* http://localhost:8000/checkout?user=danny - will finish the task "danny" is working on
* http://localhost:8000/report - will report all finished tasks

