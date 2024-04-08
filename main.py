from textSummarizer.pipeline.data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.data_validation import DataValidationPipeline
from textSummarizer.logging import logger

Stage_name = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {Stage_name} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:  
    logger.exception(e)
    raise e

Stage_name = "Data Validation stage"

try:
    logger.info(f">>>>>> stage {Stage_name} started <<<<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:  
    logger.exception(e)
    raise e