from flask import url_for


def test_index_page(client):
    """
    GIVEN nothing
    WHEN a client browse to the index page
    THEN test status code and content of the response
    """
    response = client.get(url_for('main.index'))
    assert response.status_code == 302
