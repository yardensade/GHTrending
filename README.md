# GHTrending

Welcome to GHTrending, where you can get Trending GH repos with their security score.
To your convinience you may clone the repo and run the program either from CLI, local API, or API using Docker.

About the author:
  I did not write python for the last 3 years so I'm sorry in advance for whatever conventions I have butchered on the way, I looked at PEP-8 conventions but not enough :)
  

Dependencies:
- existing: Docker, Git.
- setup venv with Python3.9
- `pip install -r requirements.txt`

Running from CLI:
- `python GHTrending/GHTrending.py -n 2`

Running local API:
- python GHTrending/app.py
- either curl or directly access: `curl http://127.0.0.1:5000/trending/<number of trending repos to query>`
- example:  `curl http://127.0.0.1:5000/trending/3`

Running project from docker:
- I set up docker compose for your convinience `docker-compose up`
- either curl or directly access: `curl http://127.0.0.1:5000/trending/<number of trending repos to query>`
- example:  `curl http://127.0.0.1:5000/trending/3`
  
  
Output example:
```
Report for "nuclei-templates" repo: 

URL: https://github.com/projectdiscovery/nuclei-templates 

Author: projectdiscovery 

Risk Score: -1 



Report for "nannyml" repo: 

URL: https://github.com/NannyML/nannyml 

Author: NannyML 

Risk Score: -1 



Report for "TopFreeProxies" repo: 

URL: https://github.com/alanbobs999/TopFreeProxies 

Author: alanbobs999 

Risk Score: -1 

```
  
Risk score explanation:
```
  -1 -> Was not able to determine
  0 -> benign
  positive number -> Higher number is riskier
```

Known Limitations for first draft:
- Only repos with requierments.txt file in root dir are scanable.

TO DO (was not added due to time restrictions):
- Switch to better scan package OR forking better open source function for unused packages detection and implement locally.
- Add SAST scanner, should be set up as another service under the docker compose.
We can use add a second service python + bandit which exposes a simple API to run a scan on a specific repo by name, the services of the main app + the SAST scanner will have shared VOLUME configured on the docerfile level, thus each cloned repo from main app will be accessible to multiple checks.
- Change the fetch trending repos to better implementation either package OR scraping locally, due to poor performance and no ability to limit fetched results.
