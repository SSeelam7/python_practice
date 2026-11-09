


#2:
def convert_record_count(value):
    try:
        converted_value = int(value)
    except ValueError:
        return 0
    return converted_value


print(convert_record_count("10550"))
print(convert_record_count("5000"))
print(convert_record_count("ABC"))


#3:
def get_pipeline_status(pipeline):
    try:
        output = pipeline["status"]
    except KeyError:
        return "UNKNOWN"
    return output

pipeline1 = {
    "name": "customer_ingestion",
    "status": "SUCCESS"
}

pipeline2 = {
    "name": "orders_ingestion"
}

print(get_pipeline_status(pipeline1))
print(get_pipeline_status(pipeline2))


#4:
def calculate_average(total_records, pipeline_count):
    try:
        average = total_records / pipeline_count
    except ZeroDivisionError:
        return 0
    return average

print(calculate_average(50000, 5))
print(calculate_average(50000, 0))


#5:
def process_record_count(value):
    try:
        converted_value = int(value)
    except ValueError:
        return "Invalid"
    else:
        return "Valid"

print(process_record_count("10550"))
print(process_record_count("ABC"))

#6:
def process_pipeline():
    try:
        return 100/0

    except:
        print("Pipeline failed")

    finally:
        print("Pipeline execution completed")

process_pipeline()


#7:
def validate_pipeline(pipeline):
    if "status" not in pipeline.keys():
        raise KeyError("Respective key is not available")
    if pipeline["status"].upper() != "SUCCESS" and pipeline["status"].upper() != "FAILED":
        raise ValueError("Invalid Status")
    if pipeline["records"] < 0:
        raise ValueError("Record count should not be negative")
    else:
        return True

pipeline1 = {
    "status": "SUCCESS",
    "records": 10550
}

pipeline2 = {
    "status": "UNKNOWN",
    "records": 100
}

pipeline3 = {
    "status": "SUCCESS",
    "records": -100
}

print(validate_pipeline(pipeline1))
print(validate_pipeline(pipeline2))
print(validate_pipeline(pipeline3))


#Mini Project:

def process_pipeline(pipelines):

    pipeline_name = pipelines["pipeline"]
    status = pipelines["status"]

    try:
        if int(pipelines["records"]) < 0:
            raise ValueError("Record count cannot be negative")
        converted_records = int(pipelines["records"])

    except ValueError:
        status = "Invalid"
        converted_records = 0

    return {
        "pipeline": pipeline_name,
        "status": status,
        "records": converted_records
    }


pipeline_runs = [
    {
        "pipeline": "customer_ingestion",
        "status": "SUCCESS",
        "records": "10550"
    },
    {
        "pipeline": "orders_ingestion",
        "status": "FAILED",
        "records": "0"
    },
    {
        "pipeline": "payments_ingestion",
        "status": "SUCCESS",
        "records": "25000"
    },
    {
        "pipeline": "inventory_ingestion",
        "status": "SUCCESS",
        "records": "ABC"
    },
    {
        "pipeline": "product_ingestion",
        "status": "SUCCESS",
        "records": "-500"
    }
]


def generate_summary(processed_pipelines):
    successful_pipelines = []
    valid_pipelines = []
    invalid_pipelines = []
    total_valid_records = 0
    for pipeline in pipeline_runs:
        result = process_pipeline(pipeline)
        total_pipelines = len(pipeline_runs)
        if result["status"].upper() != "INVALID":
            total_valid_records += result["records"]
            valid_pipelines.append(result["pipeline"])

        if result["status"].upper() == "SUCCESS":
            successful_pipelines.append(result["pipeline"])

        elif result["status"].upper() == "INVALID":
            invalid_pipelines.append(result["pipeline"])
    return {
        "total_pipelines": total_pipelines,
        "valid_pipelines": len(valid_pipelines),
        "invalid_pipelines": len(invalid_pipelines),
        "successful_pipelines": len(successful_pipelines),
        "total_valid_records": total_valid_records
    }


print(generate_summary(pipeline_runs))











