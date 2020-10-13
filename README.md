# service-repo-generator
A template project used to generate MicrosoftDocs doc repositories. Given a little bit of setup.

# Steps

1. Follow the [onboarding documentation]() till you've populated `monikers`, `docsets`, and have created a `doc repo`.
2. Clone this repository and the generated doc repo. (henceforce known as `doc-repo`)
3. Evaluate the target documentation repo. Populate the `repo_configuration.json` with targeting information relevant to this PR.
4. Ensure a python version newer than 3 is present/activated. Invoke `pip install -r requirements.txt`
5. Invoke the script to generate contents (locally viewable, gitignored) and copy over to the target `doc repo`.

**NOTE**: The `repo_configuration.json` MUST exist at the root of the repo for the automation to work correctly.


# Example Valid Repo Configuraition
```
{
    "docset_name": "storage-java",
    "docset_base_path": "azure/developer",
    "monikers": [
        "storagev12","storagev10"
    ],
    "language": "java"
}
```