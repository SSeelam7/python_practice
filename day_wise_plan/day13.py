
#3:
with open ("day13_pipeline.log", "r") as file:
    content = file.read()
print(content)


#4:
with open("day13_pipeline.log", "r") as file:
    line1 = file.readline()
    line2 = file.readline()

print(line1)
print(line2)

#5:


with open("day13_pipeline.log", "r") as file:
    lines = file.readlines()

print(lines)
print(type(lines))
print(len(lines))


#7:
with open("day13_pipeline.log", "r") as file:
    for line in file:
        line = line.strip()
        print(line)


#8:
with open("day13_pipeline.log", "r") as file:
    for line in file:
        line = line.strip()
        parts = line.split(" | ")

        date = parts[0]
        status = parts[1]
        records = parts[2]

        print(f"Date: {date} | Status: {status} | Records: {records}")


#9:
with open("day13_successful_pipeline.txt", "w") as file:
    file.write("customers_ingestion\n")
    file.write("payments_ingestion\n")
    file.write("product_ingestion")


#10:

content = []

with open("day13_pipeline.log", "r") as file:
    for pipeline in file:
        line = pipeline.strip()
        parts = line.split(" | ")
        status = parts[1]
        if status.upper() == "SUCCESS":
            content.append(line)


with open("day13_successful_pipelines.txt", "w") as file:
    for pipeline in content:
        file.write(pipeline +  "\n")


#11:
with open("day13_successful_pipelines.txt", "a") as file:
    file.write("2026-08-09 | SUCCESS | 12000\n")


#12:

try:
    with open("day13_missing_file.log", "r") as file:
        content = file.read()

except FileNotFoundError:
    print("The given file is not available in directory")


#13:


total_pipelines = 0
successful_pipelines = 0
failed_pipelines = 0
total_records = 0
successful_records = 0
failed_records = 0

with open("day13_pipeline.log", "r") as file:
    for pipeline in file:
        line = pipeline.strip()
        parts = line.split(" | ")

        date = parts[0]
        status = parts[1]
        records = int(parts[2])

        total_pipelines += 1
        total_records += records

        if status.upper() == "SUCCESS":
            successful_pipelines += 1
            successful_records += records
        elif status.upper() == "FAILED":
            failed_pipelines += 1
            failed_records += records

print(f"Total Pipelines :{total_pipelines}")
print(f"Total Records :{total_records}")
print(f"Successful Pipelines :{successful_pipelines}")
print(f"Successful Records :{successful_records}")
print(f"Failed Pipelines :{failed_pipelines}")
print(f"Failed Records :{failed_records}")


# Mini Project

total_pipelines = 0
successful_pipelines = 0
failed_pipelines = 0
total_records = 0
successful_records = 0
failed_records = 0

try:
    with open("day13_mini_project.log", "r") as file:
        for pipeline in file:
            line = pipeline.strip()
            parts = line.split(" | ")

            try:
                date = parts[0]
                status = parts[1]
                records = int(parts[2])

                if status.upper() == "SUCCESS":
                    successful_pipelines += 1
                    successful_records += records

                    with open("day13_mp_successful_pipelines.txt", "a") as file:
                        file.write(date + " | " + status + " | " + str(records) + "\n")

                if records >= 15000:
                    with open("day13_mp_high_volume_pipelines.txt", "a") as file:
                        file.write(date + " | " + status + " | " + str(records) + "\n")

                elif status.upper() == "FAILED":
                    failed_pipelines += 1
                    failed_records += records
            except ValueError:
                continue

            total_pipelines += 1
            total_records += records
except FileNotFoundError:
    print("The mentioned file is not available in location")



print("========================================")
print("       PIPELINE EXECUTION SUMMARY       ")
print("========================================")

print(f"Total Pipelines :{total_pipelines}")
print(f"Total Records :{total_records}")
print(f"Successful Pipelines :{successful_pipelines}")
print(f"Successful Records :{successful_records}")
print(f"Failed Pipelines :{failed_pipelines}")
print(f"Failed Records :{failed_records}")





