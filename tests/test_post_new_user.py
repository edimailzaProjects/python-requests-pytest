from code.user import User
from faker import Faker

class TestPostNewUser:

    def test_when_is_valid_user_must_to_be_status_code_201(self):
        user = User()
        fake = Faker()

        data = {
            'name': fake.name(),
            'gender':'female',
            'email':fake.email(),
            'status':'active'
            }

        expected = 201
        response = user.post_new_user(data).status_code

        assert expected == response
    
    def test_when_email_exist_must_to_show_message_field_email_has_alredy_been_taken(self):
        user = User()

        data = {
            'name':'Edi',
            'gender':'female',
            'email':'email-twice@qa.com',
            'status':'active'
            }
        
        new_user = user.post_new_user(data).json()
        id_new_user = str(new_user['id'])

        expected = "'field\': \'email\', \'message\': \'has already been taken'"
        response = str(user.post_new_user(data).json())

        assert expected in response
        
        user.delete_user(id_new_user)

    def test_when_field_is_missing_must_to_be_status_code_422(self):
        user = User()

        data = {
            'gender':'female',
            'email':'email-twice@qa.com',
            'status':'active'
            }
        
        expected = 422
        response = user.post_new_user(data).status_code
        

        assert expected == response
    
    def test_when_name_is_missing_must_to_show_message_cant_be_blank(self):
        user = User()

        data = {
            'gender':'female',
            'email':'email-twice@qa.com',
            'status':'active'
            }
        
        json_response = user.post_new_user(data).json()
        
        expected_name = 'name'
        response_name = str(json_response[0]['field'])
        expected_message = 'can\'t be blank'
        response_message = str(json_response[0]['message'])
        

        assert expected_name in response_name
        assert expected_message in response_message
    
    def test_when_gender_is_missing_must_to_show_message_cant_be_blank_can_be_male_or_female(self):
        user = User()

        data = {
            'name':'Edi',
            'email':'email-twice@qa.com',
            'status':'active'
            }
        
        json_response = user.post_new_user(data).json()
        
        expected_gender = 'gender'
        response_gender = str(json_response[0]['field'])
        expected_message = 'can\'t be blank, can be male or female'
        response_message = str(json_response[0]['message'])
        

        assert expected_gender in response_gender
        assert expected_message in response_message
    
    def test_when_email_is_missing_must_to_show_message_cant_be_blank(self):
        user = User()

        data = {
            'name':'Edi',
            'gender':'female',
            'status':'active'
            }
        
        json_response = user.post_new_user(data).json()
        
        expected_email = 'email'
        expected_email = str(json_response[0]['field'])
        expected_message = 'can\'t be blank'
        response_message = str(json_response[0]['message'])
        

        assert expected_email in expected_email
        assert expected_message in response_message
    
    def test_when_active_is_missing_must_to_show_message_cant_be_blank(self):
        user = User()

        data = {
            'name':'Edi',
            'email':'email-twice@qa.com',
            'gender':'female',
            }
        
        json_response = user.post_new_user(data).json()
        
        expected_status = 'status'
        expected_status = str(json_response[0]['field'])
        expected_message = 'can\'t be blank'
        response_message = str(json_response[0]['message'])
        
        assert expected_status in expected_status
        assert expected_message in response_message

