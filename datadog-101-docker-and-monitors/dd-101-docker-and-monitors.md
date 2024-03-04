# Datadog-101-Docker-And-Monitors

## Pre-requisites 
- Account with learn.datadoghq.com
  - Sign Up here (https://learn.datadoghq.com/users/sign_up)
- Enroll for "The Agent on Docker" course (https://learn.datadoghq.com/courses/agent-on-docker)
- Note: The lab times out after 10 minutes of inactivity.
- Each lab session lasts for 1 hour

## Objectives
- After running this lab, you should be familiar with the following:
  - **Datadog Agent**
    - Agent Process Collection
    - Agent APM Set Up
    - Agent DogStatsD Set Up
  - **Application Performance Monitoring**
    - Installing the Datadog APM Library in Dockerfile
    - Automatic Instrumentation with Python using ddtrace-run
  - **Monitors, Alerts, Notifications**
    - Threshold Monitor using APM Metrics
      - Understand how to edit monitors
    - Monitor Variables, Notifications  
    - Set up dependencies between Monitors and Datadog API
  - **Datadog Workflow Automation**
    - Familiar with Datadog Workflow Automation  

## How to use this?
### 1. Start the Lab
<details>
<summary>Click to toggle for more info</summary>
  
![image](https://github.com/jon94/Datadog-SG-Labs/assets/40360784/81283ffc-d20a-4dec-95db-10821b008675)

</details>

### 2. Obtain the credentials
<details>
<summary>Click to toggle for more info</summary>
  
![image](https://github.com/jon94/Datadog-SG-Labs/assets/40360784/d2f176d0-8f85-409b-9e77-70d09781ad35)

</details>

### 3. Log into app.datadoghq.com using creds obtained from step (1)
<details>
<summary>Click to toggle for more info</summary>
  
<img width="1501" alt="image" src="https://github.com/jon94/Datadog-SG-Labs/assets/40360784/7518ae2b-18c0-40dc-a535-0dbe3a7c19fd">
- If you are having issue logging in, please click on "Help" and navigate to "My training credentials don't work".

![image](https://github.com/jon94/Datadog-SG-Labs/assets/40360784/b11651c4-aec4-4cd4-9672-8d3e99cb8e2c)

</details>

### 4. Clone this repo and change directory
#### Checkpoint: Start from here if lab times out.
<details>
<summary>Click to toggle for more info</summary>

```
cd

git clone https://github.com/jon94/Datadog-SG-Labs.git

cd Datadog-SG-Labs/datadog-101-docker-and-monitors
```
![image](https://github.com/jon94/Datadog-SG-Labs/assets/40360784/fdbf45c0-e269-4440-b323-ea2b17e0c3e4)

</details>

### 5. Using API Key from step (2)
<details>
<summary>Click to toggle for more info</summary>
- Make sure you are in the correct directory >> root@agent-docker-lab-host:~/Datadog-SG-Labs/datadog-101-docker
  
```
# Replace "your_actual_api_key" with your actual API key in docker-compose.yaml
api_key="your_actual_api_key"
find . -type f -exec sed -i 's/YOUR_API_KEY/'"$api_key"'/g' {} +
```

</details>

### 6. Start the containers
<details>
<summary>Click to toggle for more info</summary>

- Make sure you are in the correct directory >> root@agent-docker-lab-host:~/Datadog-SG-Labs/datadog-101-docker
```
docker compose up -d --force-recreate --no-deps --build
```
- Check that the containers are up and running
```
docker ps -a
```
![image](https://github.com/jon94/Datadog-SG-Labs/assets/40360784/54d1442f-e9a6-4521-8161-fcdbcd9b6a97)

</details>

### 7. Explore Infra using Live Containers on Datadog
<details>
<summary>Click to toggle for more info</summary>
  
- [Live Containers](https://app.datadoghq.com/containers?query=short_image%3A%28agent%20OR%20datadog-101-docker-web%29&overview-na-groups=false&selectedTopGraph=timeseries)
<img width="1346" alt="image" src="https://github.com/jon94/Datadog-SG-Labs/assets/40360784/f03a67e4-a479-489e-8a72-eefcd3db0617">
<img width="1040" alt="image" src="https://github.com/jon94/Datadog-SG-Labs/assets/40360784/48cd289a-74e6-45c3-9f27-f9c0ddf9d8d9">

</details>

### 8. Generate load to the application and observe traces
<details>
<summary>Click to toggle for more info</summary>
  
- Make sure you are in the correct directory >> root@agent-docker-lab-host:~/Datadog-SG-Labs/datadog-101-docker

- There are 2 endpoints.
  - HelloWorld >> localhost:5000/hello
  - Simulate Error >> localhost:5000/simulate_error
```
chmod +x run_script.sh 

./run_script.sh
```
</details>

### 9. Create Monitors on Datadog
<details>
<summary>Click to toggle for more info</summary>

**Task 1: Create an Application Key in Datadog**
<details>
<summary>Click to toggle for more info</summary>

- [Create](https://docs.datadoghq.com/account_management/api-app-keys/#add-application-keys) an application key in Datadog UI. We will need this for this step.

- Proceed to next step after application key is created
  
```
# Replace "your_actual_app_key" with your actual APP key in docker-compose.yaml

app_key="your_actual_app_key"
find . -type f -exec sed -i 's/YOUR_APP_KEY/'"$app_key"'/g' {} +
```
```
chmod +x create_monitor.sh
./create_monitor.sh
```
![image](https://github.com/jon94/Datadog-SG-Labs/assets/40360784/4fa64f28-0c21-4578-9029-94abc45157f2)

</details>

**Task 2: Edit the created monitor to shorten the evaluation time**
<details>
<summary>Click to toggle for more info</summary>
  
![image](https://github.com/jon94/Datadog-SG-Labs/assets/40360784/ae03c3f0-265f-478b-b683-18f05c4769eb)

</details>

**Task 3: Based on the threshold monitor, create a similar one for simulate_error service**
<details>
<summary>Click to toggle for more info</summary>
  
- 2 methods
  - From Service Catalogue
    <img width="1329" alt="image" src="https://github.com/jon94/Datadog-SG-Labs/assets/40360784/511c7a9a-5145-443a-af4e-278a12d4db10">
  - From Monitors
    <img width="1352" alt="image" src="https://github.com/jon94/Datadog-SG-Labs/assets/40360784/7f718644-bfc8-4683-93fb-2819bc36860a">
    <img width="1351" alt="image" src="https://github.com/jon94/Datadog-SG-Labs/assets/40360784/680d4621-a854-4fbd-8f2d-70a251cd52ba">
    
</details>

**Task 4: Instead of creating a monitor based on metrics, create a monitor using APM Trace Analytics. This monitor should monitor service:flask-dd-lab in env:dd-sg-lab. Trigger an Alert when the count of error spans is > 20.**

[Hint](https://app.datadoghq.com/monitors/manage?order=desc) You should see 2 monitors created. Refer to one of them as an example.

<details>
<summary>Click to toggle for more info</summary>
  
<img width="1332" alt="image" src="https://github.com/jon94/Datadog-SG-Labs/assets/40360784/a910810c-df73-47b5-9ba8-5171bbfeb988">
    
</details>

</details>

### Bonus: Monitor Deep Dive

<details>
<summary>Click to toggle for `Tasks in Monitor Deep Dive`</summary>

**Task 1: How do you alert different members based on the status of the monitor?**

<details>
<summary>Click to toggle for `Task 1`</summary>

[Hint] (https://docs.datadoghq.com/monitors/notify/variables/?tab=is_alert#conditional-variables)
  
   ```
  {{#is_alert}}
  high error rate on {{service.name}} on {{env.name}} @<email>
  {{/is_alert}} 
  
  {{#is_alert_recovery}}
  recovered. @<email>
  {{/is_alert_recovery}}
  ```

</details>

**Task 2: Your team wants better control of alerts, since simulate_error is invoked by flask-dd-labs, how can you create dependencies between the monitors such that when flask-dd-labs has an alert, simulate_errors service monitor will not be called?**

<details>
<summary>Click to toggle for `Task 2`</summary>

[Hint] (https://docs.datadoghq.com/monitors/guide/create-monitor-dependencies/)
- Follow along the idea in the document above. The endpoints in the documents are outdated. But you can use docs on [API Reference] (https://docs.datadoghq.com/api/latest/#api-reference)
  
  ```
  {{#is_alert}} 
  high error rate on {{service.name}} on {{env.name}}. Proceeding to mute downstream service (simulate_error) @webhook-mute-simulateerror
  {{/is_alert}}

  {{#is_alert_recovery}} 
  alert recovered. Proceeding to unmute downstream service (simulate_error) @webhook-unmute-simulateerror
  {{/is_alert_recovery}}
  ```

**Configure Webhook Integration**

```
To mute monitor: https://api.datadoghq.com/api/v1/monitor/<monitorid>/mute?api_key=&application_key=
To unmute monitor: https://api.datadoghq.com/api/v1/monitor/<monitorid>/unmute?api_key=&application_key=
```

[Grant the correct application key scope] (https://docs.datadoghq.com/account_management/api-app-keys/#scope-application-keys)
<img width="996" alt="image" src="https://github.com/jon94/Datadog-SG-Labs/assets/40360784/219b7a1e-67c8-455c-8912-7ec90a9b35fc">

<img width="994" alt="image" src="https://github.com/jon94/Datadog-SG-Labs/assets/40360784/ca7c2cd7-fc3d-4e4e-bcbf-a31b9d19fd1f">

<img width="998" alt="image" src="https://github.com/jon94/Datadog-SG-Labs/assets/40360784/48c0a1ff-2e1a-4412-85a5-210b5a3e26b1">

</details>

**Task 3: You learnt how to mute individual monitors, what if the downstream service has many monitors? How can you mute all monitors belonging to service:simulate_error?**

<details>
<summary>Click to toggle for `Task 3`</summary>

[Hint 1] (https://docs.datadoghq.com/monitors/downtimes/) and [Hint 2] (https://docs.datadoghq.com/service_management/workflows/)

- In order to use the api, you have to give the correct scope on your application key (monitor_downtime).
- Webhook integrations are for basic API calls, but what if you need to draw values from different endpoints? For more complicated scenarios like this, Datadog Workflow Automation is an excellent solution. 

<img width="984" alt="image" src="https://github.com/jon94/Datadog-SG-Labs/assets/40360784/d6f827c0-84c3-4399-ab05-bf2e1510ede8">

```
{{#is_alert}} 
high error rate on {{service.name}} on {{env.name}}. Proceeding to mute all alerts related to service:simulate_error @workflow-mute-all-simulate_error 
{{/is_alert}}

{{#is_alert_recovery}} 
alert recovered. Proceeding to unmute all alerts related to service:simulate_error @workflow-unmute-all-simulate_error 
{{/is_alert_recovery}}
```

## Mute all monitor based on monitor tags

<img width="1351" alt="image" src="https://github.com/jon94/Datadog-SG-Labs/assets/40360784/65951496-2e04-4374-bb7f-ac07a57e40ab">

## Unmute all monitor based on monitor tags

<img width="1349" alt="image" src="https://github.com/jon94/Datadog-SG-Labs/assets/40360784/a4215988-1ed1-4671-ab85-7949ccda6875">

### Get Active Downtime

- This displays all active downtime at the time of API call

```
https://api.datadoghq.com/api/v2/downtime?api_key=&application_key=&current_only=true
```
### Extract downtime id if env and service matches

- targetTags are defined in the JS code. This will extract the downtime id required for the cancel downtime API later.

```
var jsonData = $.Steps.Get_Active_Downtime.body;

var targetTags = ["env:dd-sg-lab", "service:simulate_error"];
var extractedIds = [];

// Check if jsonData and jsonData.data are defined
if (jsonData && jsonData.data && Array.isArray(jsonData.data)) {
  // Iterate through the data array
  for (var i = 0; i < jsonData.data.length; i++) {
    var entry = jsonData.data[i];

    // Check if entry, attributes, and monitor_tags exist
    if (
      entry &&
      entry.attributes &&
      entry.attributes.monitor_identifier &&
      entry.attributes.monitor_identifier.monitor_tags
    ) {
      // Check if monitor_tags array includes all targetTags
      var hasAllTags = targetTags.every(function(tag) {
        return entry.attributes.monitor_identifier.monitor_tags.includes(tag);
      });

      // If all targetTags are present, push the id to the extractedIds array
      if (hasAllTags) {
        extractedIds.push(entry.id);
      }
    }
  }
}

// Return the extracted IDs
return {
  extractedIds: Array.isArray(extractedIds) ? extractedIds : [extractedIds]
}
```
### Cancel Downtime API

- Downtime ID is obtained from earlier step and the Cancel Downtime API is called.

```
DELETE https://api.datadoghq.com/api/v2/downtime/{{ Steps.extract_id_if_env_and_service_match.data.extractedIds.[0] }}?api_key=&application_key=
```

</details>
