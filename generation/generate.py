import json
import yaml
import jinja2
import argparse
import os
import pdb
import sys

from repo_configuration import BaseRepoConfiguration
from java_configuration import JavaRepoConfiguration

root_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), "..", ".."))

if __name__ == "__main__":
    config_path = os.path.join(root_dir, 'repo_configuration.json')
    
    if config_path["language"].lower() == "java":
        configuration = JavaRepoConfiguration(config_path)
    elif config_path["language"].lower() == "dotnet":
        pass
    elif config_path["language"].lower() == "javascript"
        pass
    elif config_path["language"].lower() == "java"
        pass
    else:
        print("Unrecognized language. Exiting")
        exit(1)
    
    configuration.process_repo_structure()
    configuration.process_docfx_template()
    configuration.process_openpublishing_config()
    
