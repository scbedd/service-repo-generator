import json
from jinja2 import Template
import os
import shutil

class BaseRepoConfiguration:
    """ BaseRepoConfiguration is the bog-standard for handing template output for a azure documentation repository.
    Any language-specific implementations should be handled in inheriting classes.
    """
    def __init__(self, path_to_config):
        self._process_configuration(path_to_config)

        # general 
        self.root_dir = os.path.abspath(os.path.join(os.path.abspath(path_to_config), '..'))
        self.output_folder = os.path.abspath(os.path.join(self.root_dir, 'output'))
        self.docset_folder = os.path.join(self.output_folder, self.docset_name)
        self.docs_ref_services = os.path.join(self.docset_folder, 'docs-ref-services')
        self.breadcrumb_folder = os.path.join(self.docset_folder, 'breadcrumb')
        self.ci_config_folder = os.path.join(self.output_folder, 'ci-configs')

        self.docfx_dest = os.path.join(self.docset_folder , 'docfx.json')
        self.openpublishing_dest = os.path.join(self.output_folder, '.openpublishing.publish.config.json')
        self.breadcrumb_dest = os.path.join(self.breadcrumb_folder, 'toc.yml')
        self.package_dest = os.path.join(self.output_folder, 'package.json')

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
        self.language = self.json_config["language"].lower()
        self.lang = self.json_config["lang"]
        self.service_label = self.json_config["service_label"]


    def process_docfx_template(self):
        """ Used to process the docfx template into a language specific string. 
        Returns a populated template, ready for write to a file location.

        Returns String
        """
        docfx_location = os.path.join(self.root_dir, 'template', 'docfx.json')
        with open(docfx_location,'r',encoding='utf-8') as f:
            template_string = f.read()

        template = Template(template_string)
        result = template.render(config=self)
        return result

    def write_docfx_template(self):
        populated_template = self.process_docfx_template()
        
        with open(self.docfx_dest ,'w', encoding='utf-8') as f:
            f.write(populated_template)

    def process_openpublishing_config(self):
        """ Used to process the open publishing config for the repo configuration currently set.
        Returns a populated template, ready for write to a file location.

        Returns String
        """
        open_publish_location = os.path.join(self.root_dir, 'template', '.openpublishing.publish.config.json')
        with open(open_publish_location,'r',encoding='utf-8') as f:
            template_string = f.read()

        template = Template(template_string)
        return template.render(config=self)


    def write_openpublishing_config(self):
        populated_template = self.process_openpublishing_config()

        with open(self.openpublishing_dest ,'w', encoding='utf-8') as f:
            f.write(populated_template)

    def process_breadcrumb(self):
        """ Used to populate a breadcrumb.toc. Returns a populated toc, ready for write to a file location.

        Returns String
        """
        breadcrumb_location = os.path.join(self.root_dir, 'template', 'breadcrumb.toc')
        with open(breadcrumb_location,'r',encoding='utf-8') as f:
            template_string = f.read()

        template = Template(template_string)
        return template.render(config=self)


    def write_breadcrumb(self):
        populated_template = self.process_breadcrumb()
        with open(self.breadcrumb_dest ,'w', encoding='utf-8') as f:
            f.write(populated_template)




    def process_repo_structure(self):
        """ Used to create the basic file structure of the repo. Places the populated templates in the appropriate locations within the _output
        directory.

        Doc Repo Output:

        /output
            .openpublishing.publish.config.json
            /<docset name>/
                docfx.json
                /breadcrumb/
                    toc.yml
                /<moniker_1>/
                /<moniker_n>/
                /docs-ref-services/<moniker_1>/
                /docs-ref-services/<moniker_n>/


        Returns None
        """

        self._cleanup_output_folder()

        print('Creating output folder: {}'.format(self.output_folder))        
        os.mkdir(self.output_folder)

        print('Creating docset folder: {}'.format(self.docset_folder))
        os.mkdir(self.docset_folder)

        print('Creating docs-ref-services: {}'.format(self.docs_ref_services))
        os.mkdir(self.docs_ref_services)

        for moniker in self.monikers:
            moniker_output = os.path.join(self.docset_folder, moniker)
            doc_ref_autogen = os.path.join(moniker_output, 'docs-ref-autogen')
            doc_output_folder = os.path.join(self.docs_ref_services, moniker)
            print('Creating moniker output folder: {}'.format(moniker_output))
            os.mkdir(moniker_output)
            os.mkdir(doc_ref_autogen)

            print('Creating doc folder: {}'.format(doc_output_folder))
            os.mkdir(doc_output_folder)

        print('Creating breadcrumb folder: {}'.format(self.breadcrumb_folder))
        os.mkdir(self.breadcrumb_folder)

    def _cleanup_output_folder(self):
        print('Cleaning output folder: {}'.format(self.output_folder))
        if os.path.exists(self.output_folder):
            shutil.rmtree(self.output_folder)

    def get_moniker_range(self):
        return ", ".join(['"' + moniker + '"' for moniker in self.monikers])


    def capitalize(self, input):
        """ Capitalizes the first letter of a word or phrase. 
        Returns String
        """
        if input:
            return input[0].upper() + input[1:]
        else:
            return input
        
