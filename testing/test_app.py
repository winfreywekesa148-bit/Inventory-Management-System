from app import app

#get items
def test_get_inventory():
    with app.test_client() as client:
        response = client.get('/inventory')
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, list)

#add items
def test_add_item():
    with app.test_client() as client:
        response = client.post('/inventory', 
            json={'product_name': 'Test Item', 
                  'brands': 'Test Brand', 
                  'ingredients_text': 'Test ingredients'
                  }
                  )
        assert response.status_code == 201

#update item
def test_update_item():
    with app.test_client() as client:
        response = client.patch('/inventory/1', 
            json={'product_name': 'Updated Item', 
                  'brand': 'Updated Brand', 
                  'ingredients_text': 'Updated ingredients'
                  }
                  )
        assert response.status_code == 200
        data = response.get_json()
        assert data['product_name'] == 'Updated Item'

#delete item
def test_delete_item():
    with app.test_client() as client:
        response = client.delete('/inventory/1')
        assert response.status_code == 200
        data = response.get_json()
        assert data['message'] == 'Product deleted successfully.'

#search items
def test_search_item():
    with app.test_client() as client:
        response = client.get('/search?name=Item')
        assert response.status_code == 404
        
