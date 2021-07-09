# """Populates a configuration file for jolly-brancher."""

# import os
# import configparser

# KEYS_AND_PROMPTS = [['auth_email', 'your login email for Atlassian'], ['base_url', 'the base URL for Atlassian (e.g., https://cirrusv2x.atlassian.net)'], ['token', 'your Atlassian API token which can be generated here (https://id.atlassian.com/manage-profile/security/api-tokens)'], ['repo_root', 'the path to the root directory for the repository']]
# CONFIG_FILENAME = 'example'
# DEFAULT_SECTION_NAME = 'DEFAULT'

# os.chdir('../..')

# config = configparser.ConfigParser()

# if os.path.exists(f'{CONFIG_FILENAME}.ini'):
#     config.read(f'{CONFIG_FILENAME}.ini')

#     for key, input_prompt in KEYS_AND_PROMPTS:
#         if key not in config[DEFAULT_SECTION_NAME] or config[DEFAULT_SECTION_NAME][key] == '':  # check all entries are present and populated
#             config[DEFAULT_SECTION_NAME][key] = input(f'Please enter {input_prompt}: ')

# else:
#     config[DEFAULT_SECTION_NAME] = {key : input(f'Please enter {input_prompt}: ') for key, input_prompt in KEYS_AND_PROMPTS}  # ask for input and set all entries

# with open(f'{CONFIG_FILENAME}.ini', 'w') as configfile:
#     config.write(configfile)
