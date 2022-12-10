from code.user import User

class TestGetUser:

    def test_when_is_valid_user_id_must_to_be_status_code_200(self):
        user = User()

        data = {
            'name':'Edi',
            'gender':'female',
            'email':'edi@qa.com',
            'status':'active'
            }
        
        new_user = user.post_new_user(data).json()
        id_new_user = str(new_user['id'])

        expected = 200
        response = user.get_user(id_new_user).status_code

        assert expected == response
        
        user.delete_user(id_new_user)
    
    def test_when_is_invalid_user_id_must_to_be_status_code_404(self):
        user = User()

        expected = 404
        response = user.get_user('invalid').status_code

        assert expected == response

    
    def test_when_is_invalid_user_id_show_message_resource_not_found(self):
        user = User()

        expected = 'message\': \'Resource not found'
        response = str(user.get_user('invalid').json())

        assert expected in response
