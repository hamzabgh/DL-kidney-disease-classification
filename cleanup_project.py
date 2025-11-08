import shutil
from pathlib import Path
import logging
import os
from datetime import datetime

# ------------------------------------------
# Logging Configuration
# ------------------------------------------
LOG_DIR = "logs"
project_name = 'cnnClassifier'

os.makedirs(LOG_DIR, exist_ok=True)

# Use ONE persistent log file instead of timestamped ones
LOG_FILE = os.path.join(LOG_DIR, f"project_{project_name}_{datetime.today().strftime('%Y%m%d')}.log")

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] → %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, mode='a', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

# ------------------------------------------
# Project Configuration
# ------------------------------------------
project_name = 'cnnClassifier'

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
    "templates/index.html",
    "test.py"
]


def cleanup_project_structure(files):
    """Delete all project folders and files created by setup."""
    logging.info("🧹 Starting cleanup process...")

    file_paths = [Path(f) for f in files]

    # -----------------------------
    # 1️⃣ Delete files first
    # -----------------------------
    for path in file_paths:
        if path.exists() and path.is_file():
            try:
                path.unlink()
                logging.info(f"✅ Deleted file: {path}")
            except Exception as e:
                logging.error(f"⚠️ Could not delete file {path}: {e}")

    # -----------------------------
    # 2️⃣ Delete directories (deepest first)
    # -----------------------------
    # Collect unique parent directories, sorted deepest → shallowest
    directories = sorted(
        {p.parent for p in file_paths if p.parent != Path()},
        key=lambda x: len(str(x)),
        reverse=True
    )

    for directory in directories:
        try:
            # Only remove if the directory exists and is now empty
            if directory.exists() and directory.is_dir():
                shutil.rmtree(directory, ignore_errors=True)
                logging.info(f"✅ Deleted directory: {directory}")
        except Exception as e:
            logging.error(f"⚠️ Could not delete directory {directory}: {e}")

    # -----------------------------
    # 3️⃣ Check and remove 'src' root if empty
    # -----------------------------
    src_dir = Path("src")
    if src_dir.exists() and not any(src_dir.iterdir()):
        try:
            shutil.rmtree(src_dir)
            logging.info(f"✅ Deleted empty root directory: {src_dir}")
        except Exception as e:
            logging.error(f"⚠️ Could not delete root directory {src_dir}: {e}")

    logging.info("🎯 Cleanup completed successfully!\n")


if __name__ == "__main__":
    cleanup_project_structure(list_of_files)
