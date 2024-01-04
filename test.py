CODE = "SB"
value = 1


while value <= 250:
    padded_value = str(value).zfill(3)
    final_code = f"{CODE}{padded_value}"
    print(final_code)
    value +=1