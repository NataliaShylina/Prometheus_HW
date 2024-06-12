import requests


class GitHub:
    BASE_URL = "https://api.github.com"

    def get_user_defunkt(self):
        r = requests.get('https://api.github.com/users/defunkt')
        body = r.json()

        return body
    
    def get_not_exist_user(self):
        r = requests.get('https://api.github.com/users/butenkosergii')
        body = r.json()

        return body
    
    def get_user(self, username):
        r = requests.get(f"{self.BASE_URL}/users/{username}")
        body = r.json()

        return body
    
    def search_repo(self, name):
        r = requests.get(f"{self.BASE_URL}/search/repositories", params={"q": name})
        body = r.json()

        return body
    
    def get_emojis(self):
        r = requests.get(f"{self.BASE_URL}/emojis")
        body = r.json()

        return body
    
    def list_commits(self, owner, repo):
        r = requests.get(f"{self.BASE_URL}/repos/{owner}/{repo}/commits")
        body = r.json()
        
        return body
    
    def get_repo_languages(self, owner, repo):
        r = requests.get(f"{self.BASE_URL}/repos/{owner}/{repo}/languages")

        return r.json()

    def get_commit(self, owner, repo, sha):
        r = requests.get(f"{self.BASE_URL}/repos/{owner}/{repo}/commits/{sha}")

        return r.json()