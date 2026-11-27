import httpx
from django.conf import settings


class GitHubError(Exception):
    """GitHub server error"""


class GitHubService:
    def __init__(self):
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"Bearer {settings.GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json"
        }
        

    async def get_user_info(self, username: str) -> dict | None:
        try:
            async with httpx.AsyncClient(timeout=5) as client:
                r = await client.get(
                    f"{self.base_url}/users/{username}", 
                    headers=self.headers
                )
        except httpx.HTTPError as e:
            raise GitHubError("Network error") from e
    
        if r.status_code == 200:
            return r.json()
        if r.status_code == 404:
            return None
        
        raise GitHubError(f"GitHub status {r.status_code}")
        

    async def check_user_exists(self, username: str) -> bool:
        return await self.get_user_info(username) is not None
