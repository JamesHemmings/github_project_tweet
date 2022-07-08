from github import Github
import os
from datetime import datetime

now = datetime.now()

TOKEN = os.getenv("GITHUB_TOKEN")

github = Github(TOKEN)

user = github.get_user()


def new_repos():
    repo_tweets = []
    with open("previously_posted_repos", "r+") as f:
        already_posted = f.read()
        for repo in user.get_repos():
            if repo.name in already_posted:
                print(repo.name + " already posted")
            if repo.created_at.date() == now.date() and repo.name not in already_posted:
                print(repo.name + " posted")
                print(repo.description)
                repo_tweets.append(
                    f"check out my new repo on github '{repo.name}'!\nDescription:{repo.description}\n {repo.html_url}")
                f.write(repo.name + "\n")
    return repo_tweets
