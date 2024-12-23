import sender_stand_request
import data
from data import one_letter
from data import five_hundred_and_eleven
from data import cero_letter
from data import five_hundred_and_twelve
from data import special_symbol
from data import space_in_name
from data import number_in_name
from data import number_type_name

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def positive_assert(kit_body):
    kit_body = get_kit_body(kit_body)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    kit_body = get_kit_body(kit_body)
    response = sender_stand_request.post_new_client_kit(kit_body)

    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "El nombre que ingresaste es incorrecto. " \
                                         "Los nombres solo pueden contener caracteres latinos,  "\
                                         "los nombres deben tener al menos 2 caracteres y no más de 15 caracteres"

def negative_assert_no_name(user_body):
    response = sender_stand_request.post_new_client_kit(user_body)

    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "No se enviaron todos los parámetros requeridos"

# Prueba 1:
def test_create_kit_body_1_letter_in_name_get_success_response():
    positive_assert(one_letter)

# Prueba 2:
def test_create_kit_body_511_letter_in_name_get_success_response():
    positive_assert(five_hundred_and_eleven)

# Prueba 3:
def test_create_kit_body_0_letter_in_name_get_error_response():
    negative_assert_code_400(cero_letter)

# Prueba 4:
def test_create_kit_body_512_letter_in_name_get_error_response():
    negative_assert_code_400(five_hundred_and_twelve)

# Prueba 5:
def test_create_kit_body_has_special_symbol_in_name_get_success_response():
    positive_assert(special_symbol)

# Prueba 6:
def test_create_kit_body_has_space_in_name_get_successful_response():
    positive_assert(space_in_name)

# Prueba 7:
def test_create_kit_body_has_number_in_name_get_success_response():
    positive_assert(number_in_name)

# Prueba 8:
def test_create_kit_body_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_no_name(kit_body)

# Prueba 9:
def test_create_kit_body_number_type_name_get_error_response():
    kit_body = get_kit_body(number_type_name)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400