

#1:
skill_list = ["Python","SQL"]
skill_list.append(["Spark","Airflow"])
print(skill_list)

skill_list2 = ["Python","SQL"]
skill_list2.extend(["Spark","Airflow"])
print(skill_list2)

tools = ["Python", "SQL", "Spark"]
tools.remove("SQL")

print(tools)

tools = ["Python", "SQL", "Spark"]
removed = tools.pop(1)

print(tools)
print(removed)


#2:
tools = [
    "Python",
    "SQL",
    "PySpark",
    "Airflow",
    "Kafka"
]

tools.remove("SQL")
removed_item = tools.pop()
print(tools)
print(removed_item)


#3:
record_counts = [10500, 2300, 15000, 8000, 4500]
print(record_counts)
sorted_counts = sorted(record_counts)
print(sorted_counts)
record_counts.sort(reverse = True)
print(record_counts)


#4:
x = ["Python", "SQL"]
y = x
y.append("PySpark")

print(x)
print(y)

x = ["Python", "SQL"]
y = x.copy()
y.append("PySpark")

print(x)
print(y)


#5
pipeline = {
    "name": "customer_ingestion",
    "status": "SUCCESS",
    "records": 10550
}

print(pipeline.get("name"))
print(pipeline.get("status"))
print(pipeline.get("records"))
print(pipeline.get("duration",0))


#6
pipeline = {
    "name": "customer_ingestion",
    "status": "FAILED"
}

pipeline.update({
    "records": 0,
    "environment": "production",
    "status": "FAILED"
})

print(pipeline)

pipeline.update({
    "status": "SUCCESS"
})

print(pipeline)


#7:
pipeline = {
    "name": "customer_ingestion",
    "status": "SUCCESS",
    "records": 10550,
    "environment": "production"
}

removed_element = pipeline.pop("environment")
print(pipeline)
print(removed_element)


#8:
pipeline = {
    "name": "customer_ingestion",
    "status": "SUCCESS",
    "records": 10550,
    "environment": "production"
}

for key, value in pipeline.items():
    print(key, "->", value)

#8:
pipeline = {
    "name": "orders_ingestion",
    "status": "SUCCESS",
    "metrics": {
        "records": 25000,
        "duration": 180,
        "failed_records": 25
    }
}

print(pipeline["name"])
print(pipeline["status"])
print(pipeline["metrics"]["records"])
print(pipeline["metrics"]["duration"])
print(pipeline["metrics"]["failed_records"])

#10:
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
    }
]

successful_pipeline = []
failed_pipeline = []
production_pipeline = []
pipelines_with_above_10k = []

for pipeline in pipeline_runs:



    if pipeline["status"] == "SUCCESS":
        successful_pipeline.append(pipeline["pipeline"])

    if pipeline["status"] == "FAILED":
        failed_pipeline.append(pipeline["pipeline"])

    if pipeline["environment"] == "production":
        production_pipeline.append(pipeline["pipeline"])

    if pipeline["records"] > 10000:
        pipelines_with_above_10k.append(pipeline["pipeline"])

print(f"Successful pipelines:")
for pipeline in successful_pipeline:
    print(pipeline)

print("")
print(f"Failed pipelines:")
for pipeline in failed_pipeline:
    print(pipeline)

print("")
print(f"Production pipelines:")
for pipeline in production_pipeline:
    print(pipeline)

print("")
print(f"Pipelines processing more than 10,000 records:")
for pipeline in pipelines_with_above_10k:
    print(pipeline)


#11:
record_counts = [100, 500, 1000, 5000, 10000]

high_volume_list = [num for num in record_counts if num > 1000]
print(high_volume_list)




#Mini Project:

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

total_pipelines = len(pipeline_runs)

successful_pipeline = []
failed_pipeline = []
production_pipeline = []
pipelines_with_above_10k = []
total_records = 0
successful_records = 0
records = 0
highest_record_pipeline = {"pipeline": 'name_of_pipeline'}

for pipeline in pipeline_runs:

    total_records += pipeline["records"]

    if records < pipeline["records"]:
        highest_record_pipeline.pop("pipeline")
        highest_record_pipeline.update({"pipeline":pipeline["pipeline"]})
        records = pipeline["records"]

    if pipeline["status"] == "SUCCESS":
        successful_pipeline.append(pipeline["pipeline"])
        successful_records += pipeline["records"]

    if pipeline["status"] == "FAILED":
        failed_pipeline.append(pipeline["pipeline"])

    if pipeline["environment"] == "production":
        production_pipeline.append(pipeline["pipeline"])

    if pipeline["records"] > 10000:
        pipelines_with_above_10k.append(pipeline["pipeline"])


avarege_recors_per_pipeline = total_records / total_pipelines


print(f"Total Pipelines: {total_pipelines}")
print(f"Successful Pipelines : {len(successful_pipeline)}")
print(f"Failed Pipelines : {len(failed_pipeline)}")
print(f"Total Records : {total_records}")
print(f"Successful Records : {successful_records}")

print("")
print(f"Production pipelines:")
for pipeline in production_pipeline:
    print(pipeline)

print("")
print(f"Failed pipelines:")
for pipeline in failed_pipeline:
    print(pipeline)

print("")
print(f"Pipelines processing more than 10,000 records:")
for pipeline in pipelines_with_above_10k:
    print(pipeline)

print("")
print(f"pipeline with the highest record count: {highest_record_pipeline.get("pipeline")}")

print(f"Average Records Per Pipeline {avarege_recors_per_pipeline:.2f}")

summary = {
    "total_pipelines": total_pipelines,
    "successful_pipelines": successful_pipeline,
    "failed_pipelines": failed_pipeline,
    "total_records": total_records,
    "successful_records": successful_records,
    "average_records": avarege_recors_per_pipeline
}

print(summary)

