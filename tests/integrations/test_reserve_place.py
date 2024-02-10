from server import loadClubs, loadCompetitions


def test_login_purchase_and_logout(client, app, captured_templates, load_clubs_and_competitions_and_bookings):
    club = app.club
    competition = app.competition
    place_to_reserve = "1"
    response = client.get("/")
    assert len(captured_templates) == 1
    assert response.status_code == 200
    template_index, context_index = captured_templates[0]
    assert template_index.name == "index.html"
    assert 'request' in context_index
    assert context_index["request"].url == 'http://localhost/'
    
    # page show summary
    request = client.post('/showSummary', data={'email': club['email']})
    template_showsummary, context_showsummary = captured_templates[1]
    assert request.status_code == 200
    assert template_showsummary.name == "welcome.html"
    assert 'request' in context_showsummary
    assert context_showsummary['request'].url == 'http://localhost/showSummary'

    # page book
    request_book = client.get(f'/book/{competition["name"]}/{club["name"]}')
    template_book, context_book = captured_templates[2]
    assert request_book.status_code == 200
    assert template_book.name == "booking.html"
    assert 'request' in context_book
    clean_url = str(context_book['request'].url).replace('%20', ' ')
    assert clean_url == 'http://localhost/book/Spring Festival/Simply Lift'
    
    # page purchaseplace
    data = {
        'competition': competition['name'],
        'club': club['name'],
        'places': place_to_reserve
    }
    request_purchase = client.post('/purchasePlaces', data=data)
    template_purchase, context_purchase = captured_templates[3]
    assert request_purchase.status_code == 200
    assert template_purchase.name == "welcome.html"
    assert 'request' in context_purchase
    assert context_purchase['request'].url == 'http://localhost/purchasePlaces'

    # logout
    request_logout = client.get('/logout')
    assert request_logout.status_code == 302 
    assert request_logout.location == '/' 
    assert not hasattr(client, "clubs") 
    assert not hasattr(client, "competitions") 
    