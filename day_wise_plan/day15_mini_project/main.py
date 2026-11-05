print("===== PIPELINE REPORT =====")


import file_utils, pipeline_utils

pipelines = file_utils.read_pipeline_file("day15_pipeline.log")

total_records = pipeline_utils.calculate_total_records(pipelines)
successful_pipelines = pipeline_utils.get_successful_pipelines(pipelines)
Failed_pipelines = pipeline_utils.get_failed_pipelines(pipelines)
high_volume_pipelines = pipeline_utils.get_high_volume_pipelines(pipelines, 10000)

print(f"Total Records : {total_records}")
print(f"Successful Pipelines : {successful_pipelines}")
print(f"Failed Pipelines : {Failed_pipelines}")
print(f"High Volume Pipelines : {high_volume_pipelines}")



