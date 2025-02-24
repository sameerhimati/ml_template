#!/usr/bin/env python
import os
import sys
import shutil
from pathlib import Path
import re
import argparse

def setup_project(project_name=None, template_dir=None):
    # Get project name from command line if not provided
    if not project_name:
        parser = argparse.ArgumentParser(description='Create a new ML project from template')
        parser.add_argument('project_name', help='Name of the project (lowercase, no spaces)')
        args = parser.parse_args()
        project_name = args.project_name
    
    # Validate project name
    if not re.match("^[a-z0-9-]+$", project_name):
        print("Error: Project name should contain only lowercase letters, numbers, and hyphens")
        return
    
    # Determine template directory
    if not template_dir:
        # If installed as a package, template_dir will be set
        # Otherwise, use the directory where this script is located
        template_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create project in current directory
    project_dir = Path(os.getcwd()) / project_name
    if project_dir.exists():
        print(f"Error: Directory {project_name} already exists")
        return
    
    # Create main project directory
    project_dir.mkdir()
    
    # Create directory structure
    for dir_path in [
        "configs/model",
        "configs/training",
        "data/raw",
        "data/processed",
        "data/external",
        "experiments/logs",
        "experiments/models",
        "notebooks",
        "src/data",
        "src/models",
        "src/training",
        "src/utils",
        "tests"
    ]:
        (project_dir / dir_path).mkdir(parents=True, exist_ok=True)
    
    # Create __init__.py files
    for dir_path in [
        "src",
        "src/data",
        "src/models",
        "src/training",
        "src/utils",
        "tests"
    ]:
        init_file = project_dir / dir_path / "__init__.py"
        init_file.touch()
    
    # Copy template files
    for filename in [".gitignore", "environment.yml", "README.md"]:
        source = Path(template_dir) / filename
        if source.exists():
            shutil.copy(source, project_dir)
    
    # Update environment.yml
    env_file = project_dir / "environment.yml"
    if env_file.exists():
        with env_file.open('r') as f:
            content = f.read()
        
        # Replace environment name
        content = re.sub(r'name: .*', f'name: {project_name}', content)
        
        with env_file.open('w') as f:
            f.write(content)
    
    # Update README.md
    readme_file = project_dir / "README.md"
    if readme_file.exists():
        with readme_file.open('r') as f:
            content = f.read()
        
        # Replace project name
        content = content.replace("PROJECT_NAME", project_name.replace('-', ' ').title())
        
        with readme_file.open('w') as f:
            f.write(content)
    
    print(f"\nProject {project_name} created successfully!")
    print("\nNext steps:")
    print(f"1. cd {project_name}")
    print(f"2. conda env create -f environment.yml")
    print(f"3. conda activate {project_name}")

if __name__ == "__main__":
    setup_project()