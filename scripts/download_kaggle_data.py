from retail_api.data.kaggle_downloader import download_competition_data # type: ignore

if __name__ == "__main__":
    download_competition_data(keep_archive=False)