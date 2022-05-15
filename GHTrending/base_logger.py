import logging

# Create and configure logger
logging.basicConfig(filename="repos.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
# Init
logger = logging.getLogger()
# Setting the threshold of logger to INFO
logger.setLevel(logging.DEBUG)
