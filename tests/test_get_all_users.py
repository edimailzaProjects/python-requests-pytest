from code.user import User

class TestGetAllUsers:

    def test_when_get_all_users_is_valid_url_must_to_be_status_code_200(self):
        user = User()
        
        expected = 200
        response = user.get_all_users('https://gorest.co.in/public/v2/users/').status_code

        assert expected == response
    
    def test_when_get_all_users_is_invalid_url_must_to_be_status_code_404(self):
        user = User()

        expected = 404
        response = user.get_all_users('https://gorest.co.in/public/v2/invalid_users/').status_code

        assert expected == response

    def test_when_get_user_is_valid_id_must_to_show_in_get_all_users(self):
        user = User()

        data = {
            'name':'Edi',
            'gender':'female',
            'email':'edi@qa.com',
            'status':'active'
            }
        
        new_user = user.post_new_user(data).json()
        id_new_user = str(new_user['id'])

        expected = "[]"
        response = str(user.get_all_users('https://gorest.co.in/public/v2/users/').json())

        assert expected is not response

        user.delete_user(id_new_user)
