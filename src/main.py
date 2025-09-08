import argparse
import json

def main():
    # Read configuration file from command
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, required=True)
    args = parser.parse_args()

    # Load configuration file in json
    with open(args.config, "r") as f:
        config = json.load(f)

    # Reader section in config file
    reader = config.get("reader", {})
    path_input = reader.get("pathInput")
    input_type = reader.get("type")

   

    # Preprocessing section in config file
    preprocessing = config.get("preprocessing", [])
    for step in preprocessing:
        if step.get("dropDuplicates"):
            print("drop duplicates")
           

        if "imputation" in step:
            impute = step["imputation"]
            if impute.get("enabled"):
                print("imputation load")
               
    #Training section in config file
    training = config.get("training", {})
    data_split = training.get("dataSplit", {})
    if data_split.get("enabled"):
        print("Split parameters uploaded")


    algorithm = training.get("algorithm", {})
    if algorithm.get("enabled"):
        algo_name = algorithm["name"]
        algo_params = algorithm["params"]
        print(f"Training parameters uploaded")

    #Testing section in config file

    testing = config.get("testing", {})
    if testing.get("enabled"):
        print("Testing parameters uploaded")

if __name__ == "__main__":
    main()

