import git
from termcolor import colored
from time import ctime

max_commit_summary_length = 50
max_commit_line_length = 50

def get_git_commit_history(project_path, branch=None):
    repo = git.Repo(project_path)
    commits = list(repo.iter_commits(branch or 'master'))
    for commit in commits:
        print(len(commit.summary))
        print('%s (%s): %s' % (commit.author.name, ctime(commit.committed_date), commit.summary))

def is_commit_summary_length_valid(commit_summary):
    if len(commit_summary) > max_commit_summary_length:
        return False
    return True

def is_commit_message_line_length_valid(commit_message):
    commit_message_lines = commit_message.split('\n')
    for line in commit_message_lines:
        if len(line) > max_commit_line_length:
            return False
        continue
    return True

def check_commit_history(project_path, branch_name=None):
    repo = git.Repo(project_path)
    commits = list(repo.iter_commits(branch_name or 'master'))
    for commit in commits:
        if not is_commit_summary_length_valid(commit.summary):
            print('%s %s' % (colored('ERROR:', 'red'), 'Commit summary length is too long.'))
            print('   Commit summary length should be <= %s' % max_commit_summary_length)
            print('   Commit summary length was:         %s' % len(commit.summary))
            print('   %s %s (%s)' % (commit.hexsha, commit.author.name, commit.committed_date))

        if not is_commit_message_line_length_valid(commit.summary):
            print('%s %s' % (colored('ERROR:', 'red'), 'Commit message line length is too long.'))
            print('   Commit message line length should be <= %s' % max_commit_line_length)
            print('   %s %s (%s)' % (commit.hexsha, commit.author.name, commit.committed_date))
