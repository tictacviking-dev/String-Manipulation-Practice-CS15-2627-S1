string_to_process = "eggs,cheese,milk,bread,cereal"
text = string_to_process.upper()
items = text.split(",")

print(" | ".join(items))

# Expected Output: "EGGS | CHEESE | MILK | BREAD | CEREAL"