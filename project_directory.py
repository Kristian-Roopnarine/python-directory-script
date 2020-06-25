import os

SET_UP_FILE_CODE = """
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description':'My Project',
    'author':'My name',
    'url':'URL to get it at.',
    'download_url':'Where to download it.',
    'author_email':'My Email',
    'version':'0.1',
    'install_requires':['requests','python-decouple'],
    'packages':['PROJECT_NAME'],
    'scripts':[],
    'name':'projectname'
}

setup(**config)

"""

class ProjectDirectory:
    
    def __init__(self,project_name):
        self.root_directory = os.getcwd()
        self.project_root = self.root_directory + '/' + project_name
        self.project_name = project_name
        self.sub_directories = ['bin','tests']
        self.exists = False
        self.create_project_root_directory()


    def create_setup_file(self):
        fname="setup.py"
        with open(fname,'w') as f:
            f.write(SET_UP_FILE_CODE)
    
    def create_init_file(self):
        open("__init__.py",'w').close()
    
    def create_project_root_directory(self):
        if os.path.exists(self.project_root):
            self.exists = True
            return 
        else:
            os.mkdir(self.project_root)
            self.create_sub_directories()
            self.create_test_directory_files()

            
    def create_sub_directories(self):
        os.chdir(f"{self.project_name}")
        for sub in self.sub_directories:
            os.mkdir(sub)
        self.create_init_file()
        self.create_setup_file()
    
    def create_test_directory_files(self):
        if os.getcwd() == self.project_root:
            os.chdir("tests")
        else:
            os.chdir(f"{self.project_root}/tests")
        self.create_init_file()
        adjusted_project_name = "_".join(self.project_name.split())
        open(f"{adjusted_project_name}_test.py",'w').close()
