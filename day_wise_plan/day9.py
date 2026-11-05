
#1:
def say_hello():
    print("Hello, Data Engineer!")

say_hello()


#2:
def greet_engineer(name):
    print(f"Hello {name}, welcome to Python Data Engineering!")

greet_engineer("Sairam")

#3:
def print_pipeline_info(pipeline_name, status, records):
    print(f"Pipeline: {pipeline_name} | Status: {status} | Records: {records}")

print_pipeline_info("customer_ingestion", "SUCCESS ", 10550)


#4:
def calculate_total(a, b):
    return (a+b)

result = calculate_total(100, 200)
print(result)

final_result = result * 2
print(final_result)


#5:
def check_record_count(record_count):
    if record_count > 0:
        return "Records processed"
    elif record_count == 0:
        return "No records processed"
    elif record_count < 0:
        return "Invalid record count"

print(check_record_count(100))
print(check_record_count(0))
print(check_record_count(-1))

#6:
def pipeline_info(
        pipeline_name,
        environment="production"):
    return (f"Pipeline: {pipeline_name} | Environment: {environment}")

print(pipeline_info("customer_ingestion"))
print(pipeline_info("customer_ingestion", "development"))

#7:
def get_high_volume_records(record_counts, threshold):

    high_volume_records = []

    for record in record_counts:
        if record > threshold:
            high_volume_records.append(record)

    print(high_volume_records)

record_counts = [
    100,
    500,
    1000,
    5000,
    10000
]

result = get_high_volume_records(
    record_counts,
    1000
)

#8:

def get_pipeline_status(pipeline):
    if pipeline["status"].upper() == "SUCCESS":
        return "SUCCESS"
    elif pipeline["status"].upper() == "FAILED":
        return "FAILED"
    else:
        return "UNKNOWN"


pipeline = {
    "name": "customer_ingestion",
    "status": "success",
    "records": 10550
}

result = get_pipeline_status(pipeline)
print(result)



#8:

pipeline_runs = [
    {
        "pipeline": "customer_ingestion",
        "status": "SUCCESS",
        "records": 10550
    },
    {
        "pipeline": "orders_ingestion",
        "status": "FAILED",
        "records": 5000
    },
    {
        "pipeline": "payments_ingestion",
        "status": "SUCCESS",
        "records": 25000
    }
]

failed_pipelines = []

def get_failed_pipelines(pipeline_runs):
    for pipeline in pipeline_runs:
        if pipeline["status"].upper() == "FAILED":
            failed_pipelines.append(pipeline["pipeline"])

result = get_failed_pipelines(pipeline_runs)
print(failed_pipelines)


#10:

successful_records = 0
no_of_pipelines = len(pipeline_runs)

def calculate_total_records(pipeline_runs):
    total_records = 0
    for pipeline in pipeline_runs:
        total_records += pipeline["records"]
    return total_records

def calculate_successful_records(pipeline_runs):
    for pipeline in pipeline_runs:
        successful_records = 0
        if pipeline["status"].upper() == "SUCCESS":
            successful_records += pipeline["records"]
    return successful_records

def calculate_average_records(pipeline_runs):
    total_records = 0
    for pipeline in pipeline_runs:
        total_records += pipeline["records"]

    average_records = total_records / no_of_pipelines
    return average_records

total_records = calculate_total_records(pipeline_runs)
successful_records = calculate_successful_records(pipeline_runs)
avarage_records = calculate_average_records(pipeline_runs)

print(f"Total Records: {total_records}")
print(f"Successful Records: {successful_records}")
print(f"Average Records: {avarage_records}")


#Mini Project

pipeline_runs = [
    {
        "pipeline": "customer_ingestion",
        "environment": "production",
        "status": "SUCCESS",
        "records": 10550
    },
    {
        "pipeline": "orders_ingestion",
        "environment": "production",
        "status": "FAILED",
        "records": 0
    },
    {
        "pipeline": "payments_ingestion",
        "environment": "development",
        "status": "SUCCESS",
        "records": 25000
    },
    {
        "pipeline": "product_ingestion",
        "environment": "production",
        "status": "SUCCESS",
        "records": 15000
    },
    {
        "pipeline": "inventory_ingestion",
        "environment": "production",
        "status": "FAILED",
        "records": 2000
    }
]



def get_total_pipelines(pipeline_runs):
    total_runs = len(pipeline_runs)
    return total_runs

def get_successful_pipelines(pipeline_runs):
    successful_pipelines = []
    for pipeline in pipeline_runs:
        if pipeline["status"].upper() == "SUCCESS":
            successful_pipelines.append(pipeline["pipeline"])
    return successful_pipelines

def get_failed_pipelines(pipeline_runs):
    failed_pipelines = []
    for pipeline in pipeline_runs:
        if pipeline["status"].upper() == "FAILED":
            failed_pipelines.append(pipeline["pipeline"])
    return failed_pipelines


def get_production_pipelines(pipeline_runs):
    production_pipelines = []
    for pipeline in pipeline_runs:
        if pipeline["environment"].upper() == "PRODUCTION":
            production_pipelines.append(pipeline["pipeline"])
    return production_pipelines

def calculate_total_records(pipeline_runs):
    total_records = 0
    for pipeline in pipeline_runs:
        total_records += pipeline["records"]
    return total_records

def calculate_successful_records(pipeline_runs):
    for pipeline in pipeline_runs:
        successful_records = 0
        if pipeline["status"].upper() == "SUCCESS":
            successful_records += pipeline["records"]
    return successful_records

def calculate_average_records(pipeline_runs):
    total_records = 0
    for pipeline in pipeline_runs:
        total_records += pipeline["records"]

    average_records = total_records / len(pipeline_runs)
    return average_records


def get_high_volume_pipelines(pipeline_runs,threshold):
    high_volume_pipelines = []

    for pipeline in pipeline_runs:
        if pipeline["records"] > threshold:
            high_volume_pipelines.append(pipeline["pipeline"])
    return high_volume_pipelines

def get_highest_record_pipeline(pipeline_runs):
    highest_record_pipeline = " "
    highest_record_pipeline_records = 0

    for pipeline in pipeline_runs:
        if pipeline["records"] > highest_record_pipeline_records:
            highest_record_pipeline = pipeline["pipeline"]
            highest_record_pipeline_records = pipeline["records"]
    return highest_record_pipeline

total_records = calculate_total_records(pipeline_runs)
successful_records = calculate_successful_records(pipeline_runs)
avarage_records = calculate_average_records(pipeline_runs)


def generate_pipeline_summary(pipeline_runs):
    total_pipelines = get_total_pipelines(pipeline_runs)
    successful_pipelines = get_successful_pipelines(pipeline_runs)
    failed_pipelines = get_failed_pipelines(pipeline_runs)
    total_records = calculate_total_records(pipeline_runs)
    successful_records = calculate_successful_records(pipeline_runs)
    average_records = calculate_average_records(pipeline_runs)
    high_vole_pipelines = get_high_volume_pipelines(pipeline_runs,5000)
    highest_records_pipeline = get_highest_record_pipeline(pipeline_runs)


    print(f"total_pipelines : {total_pipelines}")
    print(f"successful_pipelines : {successful_pipelines}")
    print(f"failed_pipelines : {failed_pipelines}")
    print(f"total_records : {total_records}")
    print(f"successful_records : {successful_records}")
    print(f"average_records : {average_records}")
    print(f"high_vole_pipelines : {high_vole_pipelines}")
    print(f"highest_records_pipeline : {highest_records_pipeline}")


generate_pipeline_summary(pipeline_runs)





