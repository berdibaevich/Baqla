import httpx
from django.conf import settings


class GitHubService:
    def __init__(self):
        self.token = settings.GITHUB_TOKEN
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }
        self.base_url = "https://api.github.com"


    async def get_user_info(self, username: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/users/{username}", 
                headers=self.headers
            )
            if response.status_code == 200:
                return response.json()
            return None
        

    async def check_user_exists(self, username: str) -> bool:
        user_data = await self.get_user_info(username)
        return user_data is not None
