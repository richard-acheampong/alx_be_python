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
    num1 = float(num1)  # Convert to float once at the start
    num2 = float(num2)
    
    match operation:
        case "add":
            result = num1 + num2  
        case "subtract":
            result = num1 - num2  
        case "multiply":
            result = num1 * num2 
        case "divide":
            if num2 == 0:
                return "Division by zero error"
            result = num1 / num2  
        case _:
            return "Invalid operation"
    return result



    