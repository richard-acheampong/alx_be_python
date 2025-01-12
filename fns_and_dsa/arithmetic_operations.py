#function performs basic arithmetic operations
# def perform_operation(num1, num2, operation):
#     if operation == "add":
#         result = float(num1) + float(num2)
#     elif operation == "subtract":
#         result = float(num1) - float(num2)
#     elif operation == "multiply":
#         result = float(num1) * float(num2)
#     elif operation == "divide":
#         if num2 == 0:
#             return "Division by zero error"
#         result = float(num1) / float(num2)
#     else:
#         return "Invalid operation"
#     return result

def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            result = float(num1) + float(num2)
        case "subtract":
            result = float(num1) - float(num2)
        case "multiply":
            result = float(num1) * float(num2)
        case "divide":
            if num2 == 0:
                return "Division by zero error"
            result = float(num1) / float(num2)
        case _:
            return "Invalid operation"
    return result