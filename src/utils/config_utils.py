import yaml

def get_common_config(api_config):
    with open(api_config , 'r') as file:
        api_data = yaml.safe_load(file) 
    return api_data