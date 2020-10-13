import json
from jinja2 import template
import os
import shutil

# values

# docset_name
    # to find the docset base path. head to the root of the docset in OPS: https://ops.microsoft.com/#/repos/79cce3b8-1cb1-0a77-ac53-28978d1fa77c?tabName=docsets
    # then look at details and find "Base URL"
# docset_base_path DEFAULT "azure/developer"
# monikers_list
# language

class BaseRepoConfiguration:
    """ BaseRepoConfiguration is the bog-standard for handing template output for a azure documentation repository.
    Any language-specific implementations should be handled in inheriting classes.
    """
    def __init__(self, path_to_config):
        _process_configuration(self, path_to_config)

        # general 
        self.root_dir = os.path.join(os.path.abspath(path_to_config), '..')
        self.output_folder = os.path.join(self.root_dir, 'output')

    def _process_configuration(self, path_to_config):
        if path_to_config:
            with open(path_to_config, 'r', encoding='utf-8') as f:
                self.json_config = json.load(f)
        else:
            self.json_config = {}

        self.docset_name = self.json_config["docset_name"]
        if self.json_config["docset_base_path"]:
            self.docset_base_path = self.json_config["docset_base_path"]
        else: 
            self.docset_base_path = "azure/developer"
        
        self.monikers = self.json_config["monikers"]
        self.language = self.json_config["language"]
        self.lang = self.json_config["lang"]
        self.service_label = self.json_config["service_label"]


    def process_docfx_template(self):
        """ Used to process the docfx template into a language specific string. 
        Returns a populated template, ready for write to a file location.

        Returns String
        """
        

    def process_openpublishing_config(self):
        """ Used to process the open publishing config for the repo configuration currently set.
        Returns a populated template, ready for write to a file location.

        Returns String
        """
        print("Base Repo Configuration openpublishing processing")

    def process_repo_structure(self):
        """ Used to create the basic file structure of the repo. Places the populated templates in the appropriate locations within the _output
        directory.

        Standard Output
        /output
            .openpublishing.publish.config.json
            /<docset name>/
                docfx.json
                /<moniker_1>/
                /<moniker_n>/
                /docs-ref-services/<moniker_n>/


        Returns None
        """
        self._cleanup_output_folder()
        
        os.mkdir(self.output_folder)
        os.mkdir(os.path.join(self.output_folder, 'docs-ref-services'))



    def _cleanup_output_folder(self):
        if os.path.exists(self.output_folder)
            shutil.rmtree(self.output_folder)

    def capitalize(self, input):
        """ Capitalizes the first letter of a word or phrase. 
        Returns String
        """
        if input:
            return input[0].upper + input[1:]
        else:
            return input
        

    