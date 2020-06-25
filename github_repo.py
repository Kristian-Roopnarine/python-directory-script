import requests
import os
import json
from decouple import config
from project_directory import ProjectDirectory

# connect to github api
github_key = config('GITHUB_KEY')

url="https://api.github.com/user/repos"

def create_repo_JSON(project_name):
    return {
        "name": project_name,
        "description": "This is your first repository",
        "homepage": "https://github.com",
        "private":False,
    }

headers = {
    'Authorization':f'token {github_key}'
}

project_name = input("New project name: ")
new_project = ProjectDirectory(project_name)


if new_project.exists:
    print("This project already exists in this directory.")
else:
    data = create_repo_JSON(project_name)
    os.chdir(new_project.project_root)
    r = requests.post(url,data=json.dumps(data),headers=headers)
    response = r.json()
    clone_url = response.get('clone_url')


    GITHUB_COMMANDS = [
        'echo "# test" >> README.md',
        'git init',
        'git add .',
        'git commit -m "First commit"',
        f'git remote add origin {clone_url}',
        'git push -u origin master'
    ]

    for command in GITHUB_COMMANDS:
        os.system(command)

