def read_pipeline_file(filename):
    try:

        with open(filename, "r") as file:
            content = [line.strip() for line in file]

    except FileNotFoundError:
        content = []

    return content


