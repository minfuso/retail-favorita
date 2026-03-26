from pathlib import Path
import subprocess
import zipfile

from retail_api.core.paths import KAGGLE_DIR

COMPETITION_NAME: str = "store-sales-time-series-forecasting"


def ensure_directory_exists(directory: Path) -> None:
    """Create the target directory if it does not already exist."""
    directory.mkdir(parents=True, exist_ok=True)
    
    
def build_archive_path(directory: Path, competition_name: str) -> Path:
    """Return the expected local path of the downloaded Kaggle archive."""
    return directory / f"{competition_name}.zip"


def download_archive(competition_name: str, destination_dir: Path) -> Path:
    """Download a Kaggle competition archive into the destination directory."""
    archive_path = build_archive_path(destination_dir, competition_name)

    subprocess.run(
        args=[
            "kaggle",
            "competitions",
            "download",
            "-c",
            competition_name,
            "-p",
            str(destination_dir),
        ],
        check=True,
    )

    return archive_path


def extract_archive(archive_path: Path, destination_dir: Path) -> None:
    """Extract a Kaggle zip archive into the destination directory."""
    with zipfile.ZipFile(archive_path, mode="r") as zip_file:
        zip_file.extractall(destination_dir)


def remove_archive(archive_path: Path) -> None:
    """Delete the specified archive file."""
    archive_path.unlink()

def download_competition_data(keep_archive: bool = False) -> None:
    """Download and extract the Kaggle competition dataset.

    Args:
        keep_archive (bool, optional): Whether to keep the downloaded archive file. Defaults to False.
    """
    ensure_directory_exists(KAGGLE_DIR)

    archive_path = download_archive(
        competition_name=COMPETITION_NAME,
        destination_dir=KAGGLE_DIR,
    )

    extract_archive(
        archive_path=archive_path,
        destination_dir=KAGGLE_DIR,
    )
    
    if not keep_archive:
        remove_archive(archive_path)

    print(f"Dataset downloaded and extracted to: {KAGGLE_DIR}")