import os
import subprocess


def check_positive(value):
    """
    Returns a value if it is a positive int or errors
    Args:
        value (str): user's input
    Returns:
        int
    """
    ivalue = int(value)
    if ivalue <= 0:
        raise ValueError("%s is an invalid positive int value" % value)
    return ivalue

def is_dir_populated(path):
    """
    Returns True if given path is a directory and not empty
    Args:
        path (str): dir path
    Returns:
        bool
    """
    if os.path.exists(path) and not os.path.isfile(path):
        # Checking if the directory is not empty
        if os.listdir(path):
            return True
    return False

def clone_repo(repo_url, repo_name):
    """
    Clones repository URL, errors if clone failed or repo folder is populated
    Args:
        repo_url (str): repository URL
        repo_name (str): repository name
    Returns:
        None
    """
    repo_clone_url = f'{repo_url}.git'
    process = subprocess.Popen(['git', 'clone', repo_clone_url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, _ = process.communicate()
    if process.returncode or not is_dir_populated(repo_name):
        raise Exception(f'Could not clone repo {repo_name}')
