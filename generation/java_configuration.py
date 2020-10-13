from repo_configuration import BaseRepoConfiguration


class JavaRepoConfiguration(BaseRepoConfiguration):
    def __init__(self, path_to_config):
        super().__init__(path_to_config)

    def process_docfx_template(self):   
        print("Java Repo Configuration")