
# calculate the total records across all pipelines
def calculate_total_records(pipelines):
    total_records = 0
    for pipeline in pipelines:
        records = pipeline["records"]
        total_records += records

    return total_records

# Provides the list of successful pipelines
def get_successful_pipelines(pipelines):
    successful_pipelines = []
    for pipeline in pipelines:
        if pipeline["status"].upper() == "SUCCESS":
            successful_pipelines.append(pipeline)
    return successful_pipelines

# Provides the list of failed pipelines
def get_failed_pipelines(pipelines):
    failed_pipelines = []
    for pipeline in pipelines:
        if pipeline["status"].upper() == "FAILED":
            failed_pipelines.append(pipeline)
    return failed_pipelines


