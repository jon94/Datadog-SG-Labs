# Datadog-101-Docker

## Pre-requisites 
- Account with learn.datadoghq.com
  - Sign Up here (https://learn.datadoghq.com/users/sign_up)
- Enroll for "The Agent on Docker" course (https://learn.datadoghq.com/courses/agent-on-docker)
- Note: The lab times out after 10 minutes of inactivity.

## Objectives
- After running this lab, you should be familiar with the following:
  - **Datadog Agent**
    - Agent Process Collection
    - Agent APM Set Up
    - Agent DogStatsD Set Up
  - **Application Performance Monitoring**
    - Installing the Datadog APM Library in Dockerfile
    - Automatic Instrumentation with Python using ddtrace-run

## How to use this?
### 1. Start the Lab
![image](https://github.com/jon94/Datadog-SG-Labs/assets/40360784/81283ffc-d20a-4dec-95db-10821b008675)

### 2. Obtain the credentials
![image](https://github.com/jon94/Datadog-SG-Labs/assets/40360784/d2f176d0-8f85-409b-9e77-70d09781ad35)

### 3. Log into app.datadoghq.com using creds obtained from step (1)
<img width="1501" alt="image" src="https://github.com/jon94/Datadog-SG-Labs/assets/40360784/7518ae2b-18c0-40dc-a535-0dbe3a7c19fd">
- If you are having issue logging in, please click on "Help" and navigate to "My training credentials don't work".

![image](https://github.com/jon94/Datadog-SG-Labs/assets/40360784/b11651c4-aec4-4cd4-9672-8d3e99cb8e2c)

### 4. Clone this repo and change directory
#### Checkpoint: Start from here if lab times out.
```
cd

git clone https://github.com/jon94/Datadog-SG-Labs.git

cd Datadog-SG-Labs/datadog-101-docker
```
![image](https://github.com/jon94/Datadog-SG-Labs/assets/40360784/fdbf45c0-e269-4440-b323-ea2b17e0c3e4)

### 5. Using API Key from step (2)
- Make sure you are in the correct directory >> root@agent-docker-lab-host:~/Datadog-SG-Labs/datadog-101-docker
```
# Replace "your_actual_api_key" with your actual API key in docker-compose.yaml
api_key="your_actual_api_key"
sed -i 's/YOUR API KEY/'"$api_key"'/g' docker-compose.yaml

# Replace 'YOUR API KEY' with your actual API key in the rest of the required files
find . -type f -exec sed -i 's/YOUR_API_KEY/'"$api_key"'/g' {} +
```

### 6. Start the containers
- Make sure you are in the correct directory >> root@agent-docker-lab-host:~/Datadog-SG-Labs/datadog-101-docker
```
docker compose up -d --force-recreate --no-deps --build
```
- Check that the containers are up and running
```
docker ps -a
```
![image](https://github.com/jon94/Datadog-SG-Labs/assets/40360784/54d1442f-e9a6-4521-8161-fcdbcd9b6a97)

### 7. Explore Infra using Live Containers on Datadog
- [Live Containers](https://app.datadoghq.com/containers?query=short_image%3A%28agent%20OR%20datadog-101-docker-web%29&overview-na-groups=false&selectedTopGraph=timeseries)
<img width="1346" alt="image" src="https://github.com/jon94/Datadog-SG-Labs/assets/40360784/f03a67e4-a479-489e-8a72-eefcd3db0617">
<img width="1040" alt="image" src="https://github.com/jon94/Datadog-SG-Labs/assets/40360784/48cd289a-74e6-45c3-9f27-f9c0ddf9d8d9">

### 8. Create Monitors on Datadog
- [Create](https://docs.datadoghq.com/account_management/api-app-keys/#add-application-keys) an application key in Datadog UI. We will need this for this step.

**Task 1: Create an Application Key in Datadog**
  
```
# Replace "your_actual_app_key" with your actual APP key in docker-compose.yaml

app_key="your_actual_app_key"
find . -type f -exec sed -i 's/YOUR_APP_KEY/'"$app_key"'/g' {} +
```

### 9. Generate load to the application and observe traces
- Make sure you are in the correct directory >> root@agent-docker-lab-host:~/Datadog-SG-Labs/datadog-101-docker

- There are 2 endpoints.
  - HelloWorld >> localhost:5000/hello
  - Simulate Error >> localhost:5000/simulate_error
```
chmod +x run_script.sh 

./run_script.sh
```
