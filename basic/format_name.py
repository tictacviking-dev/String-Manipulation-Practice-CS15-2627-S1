string_to_process = "   sMitH, aLeX    "
name = string_to_process.strip()
name = name.title()
name = name.replace(",", "")
parts = name.split()

print(parts[1] + " " + parts[0])

# Expected output: "Alex Smith"