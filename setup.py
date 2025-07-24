import setuptools
from typing import List

# --- Function to parse requirements.txt ---
def get_requirements(file_path: str) -> List[str]:
    """
    This function reads a requirements file and returns a list of dependencies.
    It removes the '-e .' entry which is used for local editable installs.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")
    
    return requirements

# --- Project Metadata ---
__version__ = "0.0.1"

REPO_NAME = "ArogyaNetra-"
AUTHOR_USER_NAME = "Tushar7012"
SRC_REPO = "skinCancer"
AUTHOR_EMAIL = "td220627@gmail.com"

# Read the contents of the README file for the long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


# --- Setup Configuration ---
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="An AI-driven application for skin cancer classification with visual explanations.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=get_requirements('requirements.txt') # Add dependencies here
)
