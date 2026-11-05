logs = [
    "2026-07-23 | SUCCESS | 10550",
    "2026-07-22 | FAILED | 5000",
    "2026-07-21 | SUCCESS | 9800",
    "2026-07-20 | SUCCESS | 12000"
]

total_runs = 0
successful_runs = 0
failed_runs = 0
total_records = 0
records_processed_successfully = 0
is_pipeline_healthy = True

for log in logs:

    parts = log.split(" | ")

    date = parts[0]
    status = parts[1]
    record_count = int(parts[2])

    total_runs += 1
    total_records += record_count

    print(
        f"Date: {date} | "
        f"Status: {status} | "
        f"Records: {record_count}"
    )

    if record_count < 0:
        is_pipeline_healthy = False

    if status == "SUCCESS":
        successful_runs += 1
        records_processed_successfully += record_count

        if record_count <= 0:
            is_pipeline_healthy = False

    elif status == "FAILED":
        failed_runs += 1

average_records = total_records / total_runs

is_pipeline_healthy = (
    successful_runs >= 1
    and is_pipeline_healthy
)

print()
print("========================================")
print("       PIPELINE EXECUTION SUMMARY")
print("========================================")

print(f"Total Runs                     : {total_runs}")
print(f"Successful Runs                : {successful_runs}")
print(f"Failed Runs                    : {failed_runs}")
print(f"Total Records                  : {total_records}")
print(f"Average Records                : {average_records:.2f}")
print(f"Records Processed Successfully : {records_processed_successfully}")
print(f"Is Pipeline Healthy            : {is_pipeline_healthy}")