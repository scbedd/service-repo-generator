import json

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

    def process_docfx_template(self):
        """ Used to process the docfx template into a language specific string. 
        Returns a populated template, ready for write to a file location.

        Returns String
        """
        pass

    def process_openpublishing_config(self):
        """ Used to process the open publishing config for the repo configuration currently set.
        Returns a populated template, ready for write to a file location.

        Returns String
        """
        pass

    def process_repo_structure(self):
        """ Used to create the basic file structure of the repo. Places the populated templates in the appropriate locations within the _output
        directory.

        Returns None
        """
        pass
    