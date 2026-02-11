from pathlib import Path
from setuptools import setup, find_packages

HERE = Path(__file__).resolve().parent

def read_requirements(path: Path) -> list[str]:
    reqs: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        # Skip pip-only directives that don't belong in install_requires
        if line.startswith(("-r", "--requirement", "-c", "--constraint")):
            continue
        reqs.append(line)
    return reqs

setup(
    name="splice",
    version="1.0.1",
    description="",
    author="Alex Oesterling, Usha Bhalla",
    author_email="aoesterling@g.harvard.edu, usha_bhalla@g.harvard.edu",
    py_modules=["splice"],
    packages=find_packages(exclude=["experiments*", "data*"]),
    install_requires=read_requirements(HERE / "requirements.txt"),
)
