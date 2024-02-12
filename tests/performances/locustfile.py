from locust import HttpUser, task, between
from server import loadClubs, loadCompetitions

class ProjectPerfTest(HttpUser):
    wait_time = between(1, 5)
    competition = loadCompetitions()[0]
    club = loadClubs()[0]

    def on_start(self):
        self.client.get("/", name=".index")
        self.client.post('/showSummary', data={"email": self.club['email']}, name=".show_summary")

    @task
    def book_page(self):
        self.client.get(f"/book/{self.competition['name']}/{self.club['name']}", name=".book")

    @task
    def purchase_place(self):
        data = {
            "places" : "0",
            "club": self.club['name'],
            "competition": self.competition['name']
        }

        self.client.post('/purchasePlaces', data=data, name=".purchase_places")

    @task
    def logout(self):
        self.client.get('/logout', name=".logout")