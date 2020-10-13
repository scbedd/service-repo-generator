import json
import yaml
import jinja2
import argparse
import os
import pdb

from repo_configuration import BaseRepoConfiguration

root_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), "..", ".."))

if __name__ == "__main__":
    config_path = os.path.join(root_dir, 'repo_configuration.json')
    configuration = BaseRepoConfiguration(config_path)

    pdb.set_trace()
    print(configuration)
    # grab and output the appropriate folders/mapping files
