from github import Github
import os
from datetime import datetime
import sqlite3

now = datetime.now()

TOKEN = os.getenv("GITHUB_TOKEN")

github = Github(TOKEN)

user = github.get_user()
# connect to database
con = sqlite3.connect("repos.db")
con.row_factory = lambda cursor, row: row[0]  # returns list of single values from database
cur = con.cursor()


# create table

# cur.execute('''CREATE TABLE repos
#                                         (id text NOT NULL UNIQUE,name text)''')
# con.commit()


def new_repos():
    repo_tweets = []
    posted_repos_ids = cur.execute('SELECT id FROM repos').fetchall()
    for repo in user.get_repos():
        if str(repo.id) not in posted_repos_ids:
            print(repo.name + " posted")
            repo_tweets.append(
                f"check out my new repo on github '{repo.name}'!\nDescription:{repo.description}\n {repo.html_url}")
            cur.execute(f"INSERT INTO repos VALUES ('{repo.id}','{repo.name}')")
            con.commit()
    if repo_tweets:
        print(f"{len(repo_tweets)} repo('s) posted")
    else:
        print("No new repos to post")
    return repo_tweets



