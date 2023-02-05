import traceback
import yaml

'''
This class is responsible for initializing the different configurations required to execute the program
'''

class Initialize():
    def __init__(self):
        try:
            with open("config.yml", "r") as f:
                config = yaml.load(f, Loader=yaml.FullLoader)
                self.kafka_host = config["settings"]["kafka_host"]

        except Exception as e:
            traceback.print_exc()