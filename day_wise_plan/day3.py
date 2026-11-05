
#1:

a = 25
b = 4

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
floor_division = a // b
modulus = a % b
power = a**b

print(addition, subtraction, multiplication, division, floor_division, modulus, power, sep = '\n')


#2:

total_records = 1050
batch_size = 100

complete_batches = total_records // batch_size
remaining_batches = total_records % batch_size

print('complete_batches:',complete_batches)
print('remaining_batches:',remaining_batches)


#3

source_count = 1000
target_count = 1000

print(source_count == target_count)
print(source_count > target_count)
print(source_count < target_count)

#4

pipeline_status = "SUCCESS"
record_count = 5000

is_pipeline_valid = (pipeline_status == 'SUCCESS' and record_count > 0)

print(is_pipeline_valid)

#5:

count = 100

count += 50
count -= 25
count *= 2
count /= 5

print(count)


#6:

supported_formats = ["CSV", "JSON", "PARQUET"]

file1 = "CSV"
file2 = "XML"
file3 = "PARQUET"

print('File1 valid status',file1 in supported_formats)
print('File2 valid status',file2 in supported_formats)
print('File2 valid status',file3 in supported_formats)

#7
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)  -- True
print(a is b)  -- True

print(a == c) -- True
print(a is c) -- True


#8

total_records = 10550
batch_size = 1000
source_count = 10550
target_count = 10500
pipeline_status = "SUCCESS"


print('complete_batches:', total_records // batch_size)
print('remaining_records:', total_records % batch_size)
print('pipeline_status:', pipeline_status == 'SUCCESS')
print('source_target_count_validation:', source_count == target_count)
print('is_pipeline_healthy:', pipeline_status == 'SUCCESS' and source_count == target_count and target_count > 0)


#Bonus_challenge:
x = 10
y = 3

result = x + y * 2 ** 2

print(result) -- 24







