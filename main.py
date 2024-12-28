import kaggle

kaggle.api.authenticate()

kaggle.api.dataset_download_files('tarunrm09/climate-change-indicators', path='.', unzip=True)