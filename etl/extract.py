import pandas as pd
from pathlib import Path
from utils.config import load_config
from utils.logger import get_logger

logger = get_logger()

def extract(dataset_key: str = "raw_data") -> pd.DataFrame:
    """
    reads multiple csvs that match a glob pattern defined in config.json,
    under paths[dataset_key], and return one combined dataframe
    """

    cfg = load_config()
    pattern = cfg["paths"][dataset_key]

    files = list(Path().glob(pattern))

    if not files:
        raise FileNotFoundError(f"No files found!: {pattern}")
    
    logger.info(f"Found {len(files)} files for data '{dataset_key}':")
    for f in files:
        logger.info(f"  - {f}")

    dfs = []
    for f in files:
        logger.info(f"Reading {f}")
        df = pd.read_csv(f)
        dfs.append(df)
    
    combined = pd.concat(dfs, ignore_index=True)
    logger.info(
        f"Combined DataFrame shape: {combined.shape[0]} rows, {combined.shape[1]} columns"
    )

    return combined