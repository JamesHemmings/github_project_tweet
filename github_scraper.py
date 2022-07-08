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
            if repo.created_at.date() == now.date() and repo.name not in already_posted:
                print(repo.name + " posted")
                repo_tweets.append(
                    f"check out my new repo on github '{repo.name}'!\nDescription:{repo.description}\n {repo.html_url}")
                f.write(repo.name + "\n")
    if repo_tweets:
        print(f"{len(repo_tweets)} repo('s) posted")
    else:
        print("No new repos to post")
    return repo_tweets
