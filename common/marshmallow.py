
def marshmallow_to_json_one(model,model_data):
    # 创建schema实例
    menu_data_schema = model

    # 序列化多个实例
    menu_data_list_json = menu_data_schema.dump(model_data, many=True).data


def marshmallow_to_json_list(model,model_list):
    # 创建schema实例
    menu_data_schema = model

    # 序列化多个实例
    menu_data_list_json = menu_data_schema.dump(model_list, many=True).data

def model_to_dict(instance):
    output = {}
    for column in instance.__table__.columns:
        output[column.name] = getattr(instance, column.name)
    return output