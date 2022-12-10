from code.user import User

class TestPostNewUser:
    
    def test_when_data_user_is_changed_must_to_show_data_canged(self):
        user = User()

        data = {
            'name':'Edi',
            'gender':'female',
            'email':'edi@qa.com',
            'status':'active'
            }
        
        new_user = user.post_new_user(data).json()
        id_new_user = str(new_user['id'])

        data = {
            'name':'Edu',
            'gender':'male',
            'email':'edu@qa.com',
            'status':'inactive'
            }

        update_user = user.put_user_data(id_new_user, data).json()
        name_user = str(update_user['name'])
        gender_user = str(update_user['gender'])
        email_user  = str(update_user['email'])
        status_user = str(update_user['status'])

        new_name_expected = 'Edu'
        new_gender_expected = 'male'
        new_email_expected = 'edu@qa.com'
        new_status_expected = 'inactive'

        assert name_user == new_name_expected
        assert gender_user == new_gender_expected
        assert email_user == new_email_expected
        assert status_user == new_status_expected

        user.delete_user(id_new_user)
    
    def test_when_user_id_is_invalid_must_to_show_message(self):
        user = User()

        data = {
            'name':'Edi',
            'gender':'female',
            'email':'edi@qa.com',
            'status':'active'
            }
        
        expected = 'message\': \'Resource not found'
        result = str(user.put_user_data('invalid', data).json())

        assert expected in result