import subprocess
from abc import ABC, abstractmethod

from base_logger import logger
from repo_utils import clone_repo


class RepoInterface(ABC):
    """
    An interface used to represent a repo

    Attributes
    ----------
    repo_name : str
        The name of the repo
    repo_url : str
        The URL for the repo
    author : str
        The amazing person who owns this repo
    risk_score : int
        How risky is this repo, more is riskier

    Methods
    -------
    calculate_repo_security_score()
        Calculates repo security score
    """
    def __init__(self, repo):
        self.repo_name = repo.get('name')
        self.repo_url = repo.get('url')
        self.author = repo.get('author')
        self.risk_score = -1 # -1 acts as not found for this purpose

    @abstractmethod
    def calculate_repo_security_score_basic(self):
        pass

    @abstractmethod
    def calculate_repo_security_score(self):
        repo_url = self.repo_url
        repo_name = self.repo_name
        if not repo_url or not repo_name:
            raise Exception('Does not have sufficient data to retrieve results about repo')
        clone_repo(repo_url, repo_name)
        self.risk_score = self.calculate_repo_security_score_basic()

    @abstractmethod
    def pretty_print_repo(self):
        formatted_string = '''\n
Report for "{name}" repo: \n
URL: {url} \n
Author: {author} \n
Risk Score: {rs} \n
'''.format(name=self.repo_name, url=self.repo_url, author=self.author, rs=self.risk_score)
        return formatted_string

class PythonRepo(RepoInterface):

    def calculate_repo_security_score_basic(self):
        """
        Calculates security score of a given GH repository URL based on unused python packs
        Returns:
            int
        """
        repo_name = self.repo_name
        missing_packages = list()
        arg=f'--requirements-file={repo_name}/requirements.txt'
        process = subprocess.Popen(['pip-extra-reqs', arg, repo_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        if err:
            if 'Extra requirements' in str(err): 
                missing_packages = list(err.decode("utf-8").split('\n'))
                # Ignore prefix text for the list of packages output
                missing_packages.pop(0)
            else:
                logger.debug(f'Could not get missing packages for repo {repo_name}')
                return -1
        return len(missing_packages)

    def calculate_repo_security_score(self):
        super().calculate_repo_security_score()

    def pretty_print_repo(self):
        return super().pretty_print_repo()

class JavaScriptRepo(RepoInterface):

    def calculate_repo_security_score_basic(self):
        # some fancy JS score calc goes here
        logger.warning("I am not supported yet because my creator was lazy")

    def calculate_repo_security_score(self):
        super().calculate_repo_security_score()
    
    def pretty_print_repo(self):
        return super().pretty_print_repo()

def RepoFactory(repo):
    
    language = repo.get('language')
    supported_langs = {
        "Python": PythonRepo,
        "JavaScript": JavaScriptRepo,
    }

    if not language or language not in supported_langs:
        raise Exception("Current language is not supported or not provided")

    return supported_langs[language](repo)
