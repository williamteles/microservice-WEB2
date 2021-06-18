def generate_error_message(error_detail):
    error_message = ""

    for field, error in error_detail.items():
        error_message += f"{field}: {error[0]}\n"

    return error_message
