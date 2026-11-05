logs = [
    "2026-07-23 | SUCCESS | 10550",
    "2026-07-22 | FAILED | 5000",
    "2026-07-21 | SUCCESS | 9800",
    "2026-07-20 | SUCCESS | 12000"
]


print("""
========================================
       PIPELINE EXECUTION SUMMARY
========================================
""")

total_runs = 0
successful_runs = 0
failed_runs = 0
total_records = 0
records_processed_successfully = 0
is_pipeline_healthy = True

for log in logs:

    total_runs += 1
    total_records += int(log.split(" | ")[2])

    if int(log.split(" | ")[2]) < 0:
        is_pipeline_healthy = False

    print(f"Date: {log.split(" | ")[0]} | Status: {log.split(" | ")[1]} | Records: {log.split(" | ")[2]}")

    if log.split(" | ")[1] == "SUCCESS":
        records_processed_successfully += int(log.split(" | ")[2])
        successful_runs += 1
        if int(log.split(" | ")[2]) < 0:
            is_pipeline_healthy = False
    else:
        failed_runs += 1




average_records = total_records / total_runs
is_pipeline_healthy = (successful_runs >= 1 and is_pipeline_healthy == True)

print(f"Total Runs                      :{total_runs}")
print(f"Successful runs                 :{successful_runs}")
print(f"Failed runs                     :{failed_runs}")
print(f"Total records                   :{total_records}")
print(f"Average records                 :{average_records:.2f}")
print(f"Records Processed Successfully  :{records_processed_successfully}")
print(f"Is Pipeline healthy             :{is_pipeline_healthy}")




