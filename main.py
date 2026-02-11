from src.Demanding_Forecasting import logger 
from src.Demanding_Forecasting.components.Data_Ingestion import DataIngestion
from src.Demanding_Forecasting.config.configuration import ConfigurationManager

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>stage {STAGE_NAME} started <<<<<<<<<")
    config = ConfigurationManager()
    data_ingestion_config=config.get_data_ingestion_config()
    data_ingestion=DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.extract_zip_file()
    logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise(e)