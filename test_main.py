import json
import httpretty
from main import get_info_by_id

@httpretty.activate
def test_get_info_by_id(capsys):
    # Datos de prueba
    test_id = 2222
    test_url = "https://graph.infocasas.com.uy/graphql"
    test_response_data = {
        "data": {
            "property": {
                "id": "2222",
                "title": "Test Property",
                "price": {
                    "amount": 100000,
                    "currency": {
                        "id": "1",
                        "name": "USD",
                        "rate": 1,
                    },
                },
                "link": "/ficha/test-property",
            },
        },
    }

    # Configurar la respuesta simulada
    httpretty.register_uri(
        httpretty.POST,
        test_url,
        body=json.dumps(test_response_data),
        content_type="application/json",
    )

    # Llamar a la función get_info_by_id
    get_info_by_id(test_id)

    # Verificar la salida
    captured = capsys.readouterr()
    assert "Title: Test Property" in captured.out
    assert "Price: 100000 USD" in captured.out
    assert "More Info: https://www.infocasas.com.uy//ficha/test-property" in captured.out

    # Verificar que la solicitud se realizó correctamente
    assert httpretty.last_request().method == "POST"
    assert json.loads(httpretty.last_request().body.decode("utf-8"))["variables"]["id"] == test_id