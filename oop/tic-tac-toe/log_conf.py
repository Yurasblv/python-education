import logging

logging.basicConfig(filename='Tic-Tac-Toe Log',
                    format='%(asctime)s INFO %(message)s',
                    filemode='w'
                    )
logger = logging.getLogger()
logger.setLevel(logging.INFO)
