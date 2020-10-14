import json
import yaml
import jinja2
import argparse
import os
import pdb
import sys
import json

from java_configuration import JavaRepoConfiguration

root_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), "..", ".."))

def _get_lang(path_to_config):
    if path_to_config:
        with open(path_to_config, 'r', encoding='utf-8') as f:
            json_config = json.load(f)
    else:
        json_config = {}
    return json_config["language"]

if __name__ == "__main__":
    config_path = os.path.join(root_dir, 'repo_configuration.json')
    
    if _get_lang(config_path).lower() == "java":
        configuration = JavaRepoConfiguration(config_path)
    elif _get_lang(config_path).lower() == "dotnet":
        pass
    elif _get_lang(config_path).lower() == "javascript":
        pass
    elif _get_lang(config_path).lower() == "python":
        pass
    else:
        print("Unrecognized language. Exiting")
        exit(1)
    
    configuration.process_repo_structure()
    configuration.write_docfx_template()
    configuration.write_openpublishing_config()
    configuration.write_breadcrumb()
    configuration.write_ci_configs()
    
