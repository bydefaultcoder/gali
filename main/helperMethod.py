def action_on_delete_puchase(obj):
    print("deleting................")
    print(obj)
    pro_base_quan = obj.number_of_unit * obj.unit_type.convertNumber
    print(pro_base_quan)
    convertTo = obj.unit_type.convertTo
    while convertTo:
        pro_base_quan = pro_base_quan * convertTo.convertNumber
        print(convertTo,convertTo.convertNumber,pro_base_quan)
        convertTo = convertTo.convertTo
    obj.product.quantity -= pro_base_quan
    print("number to delte ",obj.product.quantity,pro_base_quan)
    obj.product.save()