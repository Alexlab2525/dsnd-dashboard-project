from setuptools import setup, find_packages

setup(
    name="employee_events",
    version="0.1.0",
    description="Python API for the employee_events SQLite database",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=["pandas>=1.3"],
    package_data={"employee_events": ["*.db"]},
)
