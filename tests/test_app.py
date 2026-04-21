import pytest
from urlshortener import create_app, db
from urlshortener.models import URL
from urlshortener.services import ShortenerService

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Shorten your links" in response.data

def test_url_shortening(app):
    with app.app_context():
        url, error = ShortenerService.create_short_url("https://google.com", "google")
        assert error is None
        assert url.short_code == "google"
        
                        
        url2, error2 = ShortenerService.create_short_url("https://bing.com", "google")
        assert error2 == "This custom alias is already taken."

def test_redirection(client, app):
    with app.app_context():
        ShortenerService.create_short_url("https://google.com", "g")
    
    response = client.get('/g')
    assert response.status_code == 302
    assert response.location == "https://google.com"
