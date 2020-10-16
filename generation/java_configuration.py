from repo_configuration import BaseRepoConfiguration

import os
from jinja2 import Template

class JavaRepoConfiguration(BaseRepoConfiguration):
    def __init__(self, path_to_config):
        super().__init__(path_to_config)

        self.ci_config_folder = self.output_folder
    
    def generate_ci_configs(self):
        """ Used to populate a single package.json

        Returns String
        """
        ci_config_source = os.path.join(self.root_dir, 'template', 'package.json')
        with open(ci_config_source, 'r', encoding='utf-8') as f:
            template_string = f.read()

        template = Template(template_string)
        return template.render(config=self)


    def write_ci_configs(self):
        populated_template = self.generate_ci_configs()
        package_json_dest = os.path.join(self.ci_config_folder, 'package.json')

        with open(package_json_dest, 'w', encoding='utf-8') as f:
            f.write(populated_template)