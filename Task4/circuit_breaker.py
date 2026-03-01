from locust import HttpUser, task, between

class LogisticsUser(HttpUser):
    wait_time = between(0.1, 0.2)

    @task
    def error_requests(self):
        self.client.get("/logistics/error")

    @task
    def slow_requests(self):
        self.client.get("/logistics/slow")

    @task
    def slow_requests(self):
        self.client.get("/logistics/fast")