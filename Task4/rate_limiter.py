from locust import HttpUser, task, between

class WebUser(HttpUser):
    """Веб-клиенты (лимит 50 r/s)"""
    wait_time = between(0.01, 0.02) 

    @task
    def web_requests(self):
        self.client.get(
            "/api/",
            headers={"Client-Type": "web"}
        )


class MobileUser(HttpUser):
    """Мобильные клиенты (лимит 30 r/s)"""
    wait_time = between(0.01, 0.02) 

    @task
    def mobile_requests(self):
        self.client.get(
            "/api/",
            headers={"Client-Type": "mobile"}
        )