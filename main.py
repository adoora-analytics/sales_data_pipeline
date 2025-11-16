print(">>> main.py loaded!")
from etl.extract import extract
from etl.transform import transform
from etl.load import load
from etl.validate import validate
from utils.logger import get_logger
from utils.config import load_config

def run_pipeline():
    print(">>> run_pipeline() called")

    logger = get_logger()
    config = load_config()

    try:
        df = extract("raw_data")
        logger.info("Extraction complete!")

        df = transform(df)
        logger.info("Transformation complete!")

        validate(df)
        logger.info("Validation passed!")

        staging_table = config["tables"]["staging"]
        logger.info("Loading into W4D7_staging table!")

        load(df, "W4D7_staging")
        logger.info("Load complete!")

    except Exception as e:
        logger.critical(f"Pipeline failed: {e}",  exc_info=True)


if __name__ == "__main__":
    print(">>> __name__ is __main__, calling pipeline")
    run_pipeline()