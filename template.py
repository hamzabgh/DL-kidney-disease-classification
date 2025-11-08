import os
from pathlib import Path
import logging
from datetime import datetime

# ------------------------------------------
# Logging Configuration
# ------------------------------------------
LOG_DIR = "logs"
project_name = 'cnnClassifier'
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, f"project_{project_name}_{datetime.today().strftime('%Y%m%d')}.log")

# Create file handler with UTF-8 encoding (important for emoji)
file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
stream_handler = logging.StreamHandler()

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] → %(message)s',
    handlers=[file_handler, stream_handler]
)

# ------------------------------------------
# Project Setup
# ------------------------------------------

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]


def create_project_structure(files):
    """Creates the required project directories and files safely."""
    for filepath in files:
        path = Path(filepath)
        directory = path.parent

        try:
            if directory and not directory.exists():
                directory.mkdir(parents=True, exist_ok=True)
                logging.info(f"📁 Directory created: {directory}")

            if not path.exists() or path.stat().st_size == 0:
                path.touch()
                logging.info(f"📝 File created: {path}")
            else:
                logging.info(f"ℹ️ File already exists: {path}")

        except PermissionError:
            logging.error(f"🚫 Permission denied: {path}")
        except OSError as e:
            logging.error(f"⚠️ OS error while handling {path}: {e}")
        except Exception as e:
            logging.exception(f"💥 Unexpected error while processing {path}: {e}")


if __name__ == "__main__":
    logging.info("🚀 Project structure creation started...")
    create_project_structure(list_of_files)
    logging.info("🎉 Project structure setup completed successfully!")
