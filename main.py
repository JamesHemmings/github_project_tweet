import time

from twitter_poster import TwitterPoster
from github_scraper import new_repos

if __name__ == '__main__':
    tweeter= TwitterPoster()

    for repo in new_repos():
        tweeter.tweet(message=repo)
        time.sleep(1)
    tweeter.driver.close()
