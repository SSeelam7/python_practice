
#1:

text = "DataEngineering"

print(text[0])
print(text[-1])
print(text[2])
print(text[-3])


#2:

text = "DataEngineering"

print(text[:5])
print(text[-5:])
print(text[::2])
print(text[::-1])


#3:

text = "Python Data Engineering"

print(len(text))


#4:

status = "   success    "
print(status.strip())


#5:

message = "I am learning Java for Data Engineering"

updated_message = message.replace("Java", "Python")
print(updated_message)


#6:

data = "Python,SQL,Spark,Airflow,Kafka"

print(data.split(","))


#7

languages = ["Python", "SQL", "PySpark"]

print(" | ".join(languages))


#8:

filename = "customer_data_2026.csv"

start_check = filename.startswith("customer")
end_check = filename.endswith(".csv")


print(f"Does it starts with customer: {start_check}")
print(f"Does it ends with customer: {end_check}")


#9:

log = " 2026-07-23 | SUCCESS | 10550 records processed "

extracted_log = log.split(" | ")
record_count = extracted_log[2].split()

print(f"date: {extracted_log[0].strip()}")
print(f"status: {extracted_log[1]}")
print(f"record_count: {record_count[0]}")


#10:

logs = [
    "2026-07-23 | SUCCESS | 10550",
    "2026-07-22 | FAILED | 0",
    "2026-07-21 | SUCCESS | 9800",
]

log1 = logs[0].split(" | ")
log2 = logs[1].split(" | ")
log3 = logs[2].split(" | ")



print(f"Date: {log1[0]} | Status: {log1[1]} | Records: {log1[2]}")
print(f"Date: {log2[0]} | Status: {log2[1]} | Records: {log2[2]}")
print(f"Date: {log3[0]} | Status: {log3[1]} | Records: {log3[2]}")


#Bonus challenge:

text = "Python"

print(text[1:4])   #yth
print(text[-3:])   #hon
print(text[::-1])  #nohtyP
print(len(text))   #6


