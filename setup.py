from setuptools import setup

setup(
    name="ml-template",
    version="0.1",
    description="AI/ML project template generator",
    author="Your Name",
    py_modules=["project_setup"],
    entry_points={
        'console_scripts': [
            'activate-project=project_setup:setup_project',
        ],
    },
    include_package_data=True,
    package_data={
        '': ['.gitignore', 'requirements.txt', 'README.md'],
    },
)