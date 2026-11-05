def parse_pipeline_line(line):
    parts = line.strip().split(" | ")

    name = parts[0]
    status = parts[1]
    records = int(parts[2])

    return {
        "name": name,
        "status": status,
        "records": records
    }


def calculate_total_records(pipelines):
    total_records = 0

    for pipeline in pipelines:
        records = parse_pipeline_line(pipeline)["records"]
        total_records += records

    return total_records


def get_successful_pipelines(pipelines):
    successful_pipelines = []

    for pipeline in pipelines:
        if parse_pipeline_line(pipeline)["status"].upper() == "SUCCESS":
            successful_pipelines.append(pipeline)

    return successful_pipelines


def get_failed_pipelines(pipelines):
    failed_pipelines = []

    for pipeline in pipelines:
        if parse_pipeline_line(pipeline)["status"].upper() == "FAILED":
            failed_pipelines.append(pipeline)

    return failed_pipelines


def get_high_volume_pipelines(pipelines, threshold):
    high_volume_pipelines = []

    for pipeline in pipelines:
        parsed_pipeline = parse_pipeline_line(pipeline)

        if parsed_pipeline["records"] >= threshold:
            high_volume_pipelines.append(parsed_pipeline["name"])

    return high_volume_pipelines


if __name__ == "__main__":
    pipelines = [
        "customer_ingestion | SUCCESS | 10500",
        "orders_ingestion | FAILED | 8200",
        "payments_ingestion | SUCCESS | 15200",
        "product_ingestion | SUCCESS | 9800",
        "inventory_ingestion | FAILED | 7300",
        "shipping_ingestion | SUCCESS | 12400"
    ]

    for pipeline in pipelines:
        print(pipeline)
