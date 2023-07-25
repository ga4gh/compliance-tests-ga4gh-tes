# Notes
# 1. Basic & Full views have same required fields. Hence, validating Basic views against Full view Model.

SERVICE_CONSTANTS = {
    "DIR_NAME": "compliance-tests-ga4gh-tes",
    "REQUEST_HEADERS": {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    "ENDPOINT_TO_MODEL": {
        'service_info': 'TesServiceInfo',
        'list_tasks_MINIMAL': 'TesListTasksResponseMinimal',
        'list_tasks_BASIC': 'TesListTasksResponse',
        'list_tasks_FULL': 'TesListTasksResponse',
        'get_task_MINIMAL': 'TesTaskMinimal',
        'get_task_BASIC': 'TesTask',
        'get_task_FULL': 'TesTask',
        'create_task': 'TesCreateTaskResponse',
        'create_task_request_body': 'TesTask',
        'cancel_task': 'TesCancelTaskResponse'
    }
}