'''
#1
import math

print(math.sqrt(144))
print(math.pow(5,3))
print(math.ceil(10.2))
print(math.floor(10.8))
print(math.pi)

#2: Understood the concept completely, Hence jumping to next exercise.

#3: Understood the concept completely, Hence jumping to next exercise.

'''
#4:
import day15_pipeline_utils

pipelines = [
    {"name": "customer_ingestion", "status": "SUCCESS", "records": 10500},
    {"name": "orders_ingestion", "status": "FAILED", "records": 8200},
    {"name": "payments_ingestion", "status": "SUCCESS", "records": 15200},
    {"name": "product_ingestion", "status": "SUCCESS", "records": 9800},
]

print(day15_pipeline_utils.calculate_total_records(pipelines))
print(day15_pipeline_utils.get_successful_pipelines(pipelines))
print(day15_pipeline_utils.get_failed_pipelines(pipelines))


#5: Understood the concept completely, Hence jumping to next exercise.

#6: Understood the concept completely, Hence jumping to next exercise.

#7: Understood the concept completely, Hence jumping to next exercise.

#Mini Project:






