
#1:
1. 5000
2. No
3. Because records is local variable, we can access directly only inside the function

#2:
def create_pipeline_record(
    name,
    environment,
    status,
    records
):
    return {
        "name": name,
        "environment": environment,
        "status": status,
        "records": records
    }

result = create_pipeline_record(5000, "success", "customers_orders", "production")
print(result)

#3
def calculate_total_records(*args):
    total_records = 0
    for records in args:
        total_records += records
    return total_records

record_count = calculate_total_records(100,200,300,400)
print(f"total Records: {record_count}")


#4:
def pipeline_summary(*records, **pipeline_info):
    for record in records:
        print(record)
    for key, value in pipeline_info.items():
        print(key, ":", value)


result = pipeline_summary(
    1000,
    2000,
    3000,
    pipeline="customer_ingestion",
    environment="production",
    status="SUCCESS"
)


#5:
def calculate_pipeline_metrics(pipeline_runs):
    total_records = 0
    successful_records = 0
    failed_records = 0

    for pipeline in pipeline_runs:
        total_records += pipeline["records"]

        if pipeline["status"].upper() == "SUCCESS":
            successful_records += pipeline["records"]
        elif pipeline["status"].upper() == "FAILED":
            failed_records += pipeline["records"]

    return total_records,successful_records,failed_records


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


total, successful, failed = calculate_pipeline_metrics(pipeline_runs)

print(f"Total Records :{total}")
print(f"Successful Records :{successful}")
print(f"Failed Records :{failed}")




#6:

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

def generate_pipeline_summary(pipeline_runs):
    total_pipelines = get_total_pipelines(pipeline_runs)
    successful_pipelines = get_successful_pipelines(pipeline_runs)
    failed_pipelines = get_failed_pipelines(pipeline_runs)
    total_records = calculate_total_records(pipeline_runs)
    successful_records = calculate_successful_records(pipeline_runs)
    average_records = calculate_average_records(pipeline_runs)
    high_vole_pipelines = get_high_volume_pipelines(pipeline_runs,5000)
    highest_records_pipeline = get_highest_record_pipeline(pipeline_runs)

    return {
        "total_pipelines": total_pipelines,
        "successful_pipelines": successful_pipelines,
        "failed_pipelines": failed_pipelines,
        "total_records": total_records,
        "successful_records": successful_records,
        "average_records": average_records,
        "high_vole_pipelines": high_vole_pipelines,
        "highest_records_pipeline": highest_records_pipeline
    }

summary = generate_pipeline_summary(pipeline_runs)
print(summary)


#ETL Mini Project:

records = [
    {
        "customer_id": 101,
        "name": "Alice",
        "status": "ACTIVE",
        "amount": 1500
    },
    {
        "customer_id": 102,
        "name": "Bob",
        "status": "INACTIVE",
        "amount": 800
    },
    {
        "customer_id": 103,
        "name": "Charlie",
        "status": "ACTIVE",
        "amount": 2200
    },
    {
        "customer_id": 104,
        "name": "David",
        "status": "ACTIVE",
        "amount": 500
    },
    {
        "customer_id": 105,
        "name": "Eva",
        "status": "INACTIVE",
        "amount": 1200
    }
]


#step1: convert the records as list
def extract_records(records):
    record_list = []
    for record in records:
        record_list.append(record)

    return record_list

def get_active_customers(records):
    active_customers = []
    for record in records:
        if record["status"].upper() == "ACTIVE":
            active_customers.append(record["name"])

    return active_customers

def calculate_total_amount(records):
    total_amount = 0
    active_amount = 0
    for record in records:
        total_amount  += record["amount"]
        if record["status"].upper() == "ACTIVE":
            active_amount += record["amount"]
    return total_amount, active_amount

def get_high_value_customers(records, threshold):
    high_value_customers = []
    for record in records:
        if record["amount"] > threshold:
            high_value_customers.append(record["name"])
    return high_value_customers

def generate_customer_summary(records):
    total_customers = len(records)
    active_customer = len(get_active_customers(records))
    inactive_customers = len(records) - len(get_active_customers(records))
    total_amount, active_customer_amount = calculate_total_amount(records)

    return {
    "total_customers": total_customers,
    "active_customers": active_customer,
    "inactive_customers": inactive_customers,
    "total_amount": total_amount,
    "active_customer_amount": active_customer_amount
    }

def run_etl_pipeline(records):

    records = extract_records(records)
    active_customers = get_active_customers(records)
    summary = generate_customer_summary(records)

    return summary

summary = run_etl_pipeline(records)
print(summary)





