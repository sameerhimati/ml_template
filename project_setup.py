import os
import shutil
from pathlib import Path
import re

def setup_project():
    # Get project name
    project_name = input("Enter project name (lowercase, no spaces): ").strip().lower()
    
    # Validate project name (only lowercase letters, numbers, and hyphens)
    if not re.match("^[a-z0-9-]+$", project_name):
        print("Error: Project name should contain only lowercase letters, numbers, and hyphens")
        return

    # Create project directory
    project_dir = Path(project_name)
    if project_dir.exists():
        print(f"Error: Directory {project_name} already exists")
        return

    # Copy template structure
    shutil.copytree(".", project_dir, ignore=shutil.ignore_patterns(
        '.git', '__pycache__', '*.pyc', 'setup_project.py'
    ))

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
        
        # Replace project name and conda environment name
        content = content.replace("ML Project Template", project_name.replace('-', ' ').title())
        content = content.replace("ml-project", project_name)
        
        with readme_file.open('w') as f:
            f.write(content)

    print(f"\nProject {project_name} created successfully!")
    print("\nNext steps:")
    print(f"1. cd {project_name}")
    print(f"2. conda env create -f environment.yml")
    print(f"3. conda activate {project_name}")

if __name__ == "__main__":
    setup_project()