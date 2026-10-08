from chatbot import ask_chatbot


def test_chatbot_returns_response():
    response = ask_chatbot("Hello")

    assert response is not None
    assert len(response) > 0
