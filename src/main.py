import argparse
import json
from inputReader import factoryReader
from Logger import Logger
import logging
def main():
    logger=Logger()
    logger.create_handler_with_level_and_format("info", "%(asctime)s - %(levelname)s - %(message)s","file",filename="app1.log")
    log = logger.logger
    log.setLevel(logging.DEBUG)
    log.info("test")
    log.error("this an error")
    
# ------------------------------
    # READ CONFIGURATION FILE PARAMETERS AND CALL CLASSES AND METHODS
    #-------------------------------
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--config", type=str, required=True)
    # args = parser.parse_args()
    # configPath=args.config
    # configPath="./config/config.json"
    # # Load configuration file in json
    # with open( configPath, "r") as f:
    #     config = json.load(f)

    # # Reader section in config file

    # reader = config.get("reader")
    # if reader.get("enabled"):
    #     pathInput = reader.get("pathInput") #Get path from config file
    #     inputType = reader.get("type")      #Get type input from config file
    #     logger.info()
    #     from inputReader import factoryReader   
    #     readerObj=factoryReader.selectInput(inputType) #Select factory from reader type
    #     df=readerObj.readInput(pathInput)       #Read input

   

    # # Preprocessing section in config file
    # preprocessing = config.get("preprocessing")
    # for stepPreproc in preprocessing:
    #     if "duplicates" in stepPreproc:
    #         duplicatesConfig=stepPreproc["duplicates"]
    #         if duplicatesConfig.get("enabled") and duplicatesConfig.get("dropDuplicates"):                               
    #             print("Drop duplicates parameters load")
    #             from preprocessing import preprocessing
    #             preprocessingObj=preprocessing(df)
    #             df=preprocessingObj.dropDuplicates()
            

    #     if "imputation" in stepPreproc:
    #         inputationConfig=stepPreproc["imputation"]
    #         if inputationConfig.get("enabled"):  
    #             featureToInput= inputationConfig["featureName"]
    #             lookUpValue=inputationConfig["lookUpValue"]   
    #             method=inputationConfig["method"]   
    #             print("Imputation parameters load")
    #             from preprocessing import preprocessing
    #             preprocessingObj=preprocessing(df)
    #             df=preprocessingObj.imputeValue(method,featureToInput,lookUpValue)


               
    # #Training section in config file
    # training = config.get("training")
    # dataSplit = training.get("dataSplit", {})
    # if dataSplit.get("enabled"):    
    #     from classificationTrainer import classificationTrainer   
    #     objclassificationTrainer=classificationTrainer()
    #     methodCrossValidation= dataSplit["crossValidation"]
    #     if methodCrossValidation=="kfold":
    #         numberFolds= dataSplit["numberFoldsTraining"]
    #         print("Split parameters uploaded")

    #     if methodCrossValidation=="split":
    #         trainSet=dataSplit["trainSetPercentage"]
    #         testSet=dataSplit["testSetPercentage"]
    #         validationSet=dataSplit["validationSetPercentage"]
    #         print("Split parameters uploaded")
    #     if methodCrossValidation=="LOOCV":
    #         print("Split parameters uploaded")

       
        
     


    # algorithm = training.get("algorithm", {})
    # if algorithm.get("enabled"):
    #     algo_name = algorithm["name"]
    #     algo_params = algorithm["params"]
    #     print(f"Training parameters uploaded")

    # #Testing section in config file

    # testing = config.get("testing", {})
    # if testing.get("enabled"):
    #     print("Testing parameters uploaded")

  


if __name__ == "__main__":
    main()

