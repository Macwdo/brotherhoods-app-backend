from django.db.models import Model


def get_model_fields_name(model: Model):
    return [field.name for field in model._meta.fields]


def get_error_message_for_fields_out_of_model(
    input_fields: dict[str, str], model: Model
):
    fields = get_model_fields_name(model)
    if input_fields not in fields:
        return f"Model fields: {input_fields} aren't in model fields."
