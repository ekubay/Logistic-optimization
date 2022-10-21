<<<<<<< HEAD
from pathlib import Path


class Config:
    RANDOM_SEED = 90
    ASSETS_PATH = Path("../")
    REPO = "~/Documents/"
    DATASET_FILE_PATH = "data/train.csv"
    DATASET_PATH = ASSETS_PATH / "data"
    FEATURES_PATH = ASSETS_PATH / "features"
    MODELS_PATH = ASSETS_PATH / "models"
=======
from pathlib import Path


class Config:
    RANDOM_SEED = 90
    ASSETS_PATH = Path("../")
    REPO = "~/Documents/"
    DATASET_FILE_PATH = "data/train.csv"
    DATASET_PATH = ASSETS_PATH / "data"
    FEATURES_PATH = ASSETS_PATH / "features"
    MODELS_PATH = ASSETS_PATH / "models"
>>>>>>> 58d4d2f1a2ecfa6da3c52a080ed733334bdaff97
    IMAGE_PATH = ASSETS_PATH / "images"