from code.user import User

class DeleteUser:

    def test_when_is_valid_user_id_must_to_be_status_code_204(self):
        user = User()

        data = {
            'name':'Edi',
            'gender':'female',
            'email':'edi@qa.com',
            'status':'active'
            }
        
        new_user = user.post_new_user(data).json()
        id_new_user = str(new_user['id'])

        expected = 204
        response = user.delete_user(id_new_user).status_code

        assert expected == response
    
    def test_when_is_invalid_id_must_to_be_status_code_404(self):
        user = User()

        expected = 404
        response = user.delete_user('invalid')