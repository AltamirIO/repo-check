import argparse
import tempfile

from git import Repo

import helpers

def clone_git(repo_url, branch_name='master'):
    """Returns the path of the locally-cloned repo."""
    project_path = tempfile.mkdtemp()
    Repo.clone_from(repo_url, project_path, branch=branch_name)
    return project_path

def main():
    parser = argparse.ArgumentParser(description='Check git standards.')
    parser.add_argument('--repo', dest='repo', type=str, help='Repository URL for compliance analysis')
    parser.add_argument('--branch', dest='branch', type=str, help='Name of the branch to be scanned')

    args = parser.parse_args()

    project_path = clone_git(args.repo, args.branch)

    helpers.check_commit_history.check_commit_history(project_path, args.branch)

if __name__ == '__main__':
    main()
