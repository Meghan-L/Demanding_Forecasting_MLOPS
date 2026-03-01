from Demanding_Forecasting import logger
# REMOVED 'src.' from the start
from Demanding_Forecasting.components.data_ingestion import DataIngestion
from Demanding_Forecasting.components.data_validation import DataValidation
from Demanding_Forecasting.config.configuration import ConfigurationManager
from Demanding_Forecasting.components.data_transformation import DataTransformation
from Demanding_Forecasting.components.model_trainer import ModelTrainer
STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    # data_ingestion.extract_zip_file()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    config = ConfigurationManager()
    data_validation_config = config.get_data_validation_config()
    data_validation = DataValidation(config=data_validation_config)
    data_validation.validate_all_columns()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage "
try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME}<<<<<<<<<<<<<<<")
    config=ConfigurationManager()
    data_transformation_config=config.get_data_transformation_config()
    data_transformation=DataTransformation(config=data_transformation_config)
    data_transformation.train_test_splitting()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer Stage"
try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME}<<<<<<<<<<<<<<<")
    config = ConfigurationManager()
    model_trainer_config = config.get_model_trainer_config()
    model_trainer=ModelTrainer(config=model_trainer_config)
    model_trainer.train()
    logger.info(f">>>>>>>>>>>>{STAGE_NAME} completed")

except Exception as e:
    logger.exception(e)
    raise e

from Demanding_Forecasting.components.model_evaluation import ModelEvaluation

STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    config = ConfigurationManager()
    model_evaluation_config = config.get_model_evaluation_config()
    
    model_evaluation = ModelEvaluation(config=model_evaluation_config)
    model_evaluation.initiate_model_evaluation()
    
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e