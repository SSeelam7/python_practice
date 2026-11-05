
#1:

data_tools = [
    "Python",
    "SQL",
    "PySpark",
    "Airflow",
    "Kafka"
]

print(data_tools[0])
print(data_tools[-1])
print(data_tools[2])
print(len(data_tools))




#2:
print(data_tools[:2])
print(data_tools[-1:-4:-1])
print(data_tools[1:4])
print(data_tools[::-1])




#3:
tools = ["Python", "SQL", "Java", "Hadoop"]
tools[2] = 'Pyspark'
tools[3] = 'Spark'
print(tools)



#4:

pipeline_tools = [
    "Python",
    "SQL"
]

print(pipeline_tools)
pipeline_tools.append("PySpark")
pipeline_tools.append("AirFlow")
pipeline_tools.insert(1,"Git")
pipeline_tools.remove("SQL")
removed_element = pipeline_tools.pop()
print(pipeline_tools)
print(removed_element)


#5:

record_counts = [10500, 2300, 15000, 8000, 4500]

print(record_counts)
record_counts.sort()
print(record_counts[0])
print(record_counts[-1])
record_counts.sort(reverse = True)
print(record_counts)



#6:
pipeline_config = (
    "production",
    "Airflow",
    "PostgreSQL",
    5432
)

print(pipeline_config[0])
print(pipeline_config[1])
print(pipeline_config[2])
print(pipeline_config[3])



#7:

systems = [
    "CRM",
    "ERP",
    "CRM",
    "DATA_LAKE",
    "ERP",
    "API"
]

unique_systems = set(systems)
number_of_unique_systems = len(unique_systems)
print(unique_systems)
print(number_of_unique_systems)



#8:

employee = {
    "name": "Sairam",
    "experience": 5,
    "role": "Data Engineer",
    "company": "CGI"
}

print(employee["name"])
print(employee["experience"])
print(employee["role"])
print(employee["company"])

#9:

employee["experience"] = 6
employee["skills"] = ["Python", "SQL", "PySpark"]
employee["is_active"] = True


#10:
print("name" in employee)
print("role" in employee)
print("salary" in employee)
print("skills" in employee)



#11:

logs = [
    {
        "date": "2026-07-23",
        "status": "SUCCESS",
        "record_count": 10550
    },
    {
        "date": "2026-07-22",
        "status": "FAILED",
        "record_count": 5000
    },
    {
        "date": "2026-07-21",
        "status": "SUCCESS",
        "record_count": 9800
    }
]

for log in logs:

    date = log["date"]
    status = log["status"]
    record_count = log["record_count"]
    print(f"Date: {date} | Status: {status} | Records: {record_count}")



#Challenge;

logs = [
    {
        "date": "2026-07-23",
        "status": "SUCCESS",
        "record_count": 10550
    },
    {
        "date": "2026-07-22",
        "status": "FAILED",
        "record_count": 5000
    },
    {
        "date": "2026-07-21",
        "status": "SUCCESS",
        "record_count": 9800
    },
    {
        "date": "2026-07-20",
        "status": "SUCCESS",
        "record_count": 12000
    }
]

total_runs = len(logs)
successful_runs = 0
failed_runs = 0
total_records = 0
successful_records_processed = 0
failed_pipelines = {}

for log in logs:

    date = log["date"]
    status = log["status"]
    record_count = log["record_count"]

    total_records += record_count

    if status == "SUCCESS":
        successful_runs += 1
        successful_records_processed += record_count
    else:
        failed_runs += 1
        failed_pipelines[date] = record_count


average_records = total_records / total_runs


print(f"Total Runs: {total_runs}")
print(f"Successful Runs: {successful_runs}")
print(f"Failed Runs: {failed_runs}")
print(f"Total Records: {total_records}")
print(f"Successful Records Processed: {successful_records_processed}")
print(f"Average records: {average_records:.2f}")

print("failed Pipeline")
for key,value in failed_pipelines.items():
    print(f"Date: {key}")
    print(f"Records: {value}")