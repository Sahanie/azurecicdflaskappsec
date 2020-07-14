from locust import HttpUser, task, between
import json

class WebTasks(HttpUser):
    wait_time = between(5, 9)

    @task
    def index(self):
        self.client.post(
            "/predict",
            data=json.dumps({"CHAS":{"0":0}, "RM":{"0":6.575},"TAX":{"0":296.0},"PTRATIO":{"0":15.3},"B":{"0":396.9},"LSTAT":{"0":4.98}}),
            headers={'content-type': 'application/json'}
        )
