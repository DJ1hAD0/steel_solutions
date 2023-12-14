import decimal


def calculate_sheet_spec_entry(unit_type, width_detail, height_detail, amount):
    unit_num = round(
        decimal.Decimal((width_detail * height_detail) / (unit_type.unit_width * unit_type.unit_height)) * amount, 4)
    weight = round(
        decimal.Decimal((width_detail / 1000 * height_detail / 1000)) * amount * unit_type.unit_weight, 1)
    cost = round(unit_num * unit_type.unit_cost)
    return {'num': unit_num, 'weight': weight, 'cost': cost}


def calculate_pogon_spec_entry(unit_type, length_detail, amount):
    unit_num = round(decimal.Decimal(length_detail / unit_type.unit_length) * amount, 4)
    weight = round(decimal.Decimal(length_detail / 1000) * amount * unit_type.unit_weight, 1)
    cost = round(unit_num * unit_type.unit_cost)
    return {'num': unit_num, 'weight': weight, 'cost': cost}
