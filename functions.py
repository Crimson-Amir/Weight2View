def convert_mm_to_cm(mm):
    return round(mm / 10, 2)

def calculate_size_by_item(item_obj, weight):
    # Solid Items
    one_item_weight = item_obj['weight_in_gram']

    number_of_item = weight / one_item_weight

    height = convert_mm_to_cm(item_obj['height_mm'] * number_of_item)
    width =  convert_mm_to_cm(item_obj['width_mm'] * number_of_item)
    length = convert_mm_to_cm(item_obj['length_mm'] * number_of_item)

    return width, height, length
