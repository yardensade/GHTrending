# GHTrending.py

import argparse
import os
import shutil
from itertools import islice

from gtrending import fetch_repos

from base_logger import logger
from repo_utils import check_positive
from RepoFactory import RepoFactory

API_RESULTS_LIMIT = 10

def fetch_trending_repos(repos_amount):
    aggregated_result = ''
    repos_to_fetch = repos_amount
    if repos_amount > API_RESULTS_LIMIT:
        repos_to_fetch = API_RESULTS_LIMIT
    logger.info(f'Fetching {repos_to_fetch} GH trending repos')
    repos = fetch_repos(language="python")
    for repo in islice(repos, repos_to_fetch):
        try:
            trending_repo = RepoFactory(repo)
            trending_repo.calculate_repo_security_score()
            aggregated_result=aggregated_result + trending_repo.pretty_print_repo()
        except Exception as e:
            logger.error(e)
        finally:
            if os.path.isdir(repo.get('name')):
                shutil.rmtree(repo.get('name'))
    return aggregated_result


def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='List the content of a folder')

    # Add the arguments
    parser.add_argument('-n',
                        required=True,
                        type=check_positive,
                        help='Number of repos to fetch from GH trending')

    # Parse args
    args = parser.parse_args()
    input_repos_num = args.n
    print(fetch_trending_repos(input_repos_num))

if __name__ == '__main__':
    main()
