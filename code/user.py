import requests
import json

class User:
   url = 'https://gorest.co.in/public/v2/users/'
   auth_token = 'meu_token'
   head = {'Authorization': 'Bearer '+ auth_token}

   ##GET
   
   def get_user(self, id):
      request_get_user = requests.get(self.url + id, headers = self.head)
      return request_get_user

   def get_all_users(self, url):
      request_get_all = requests.get(url)
      return request_get_all
      
   ##POST

   def post_new_user(self, data):
      requisicao_post = requests.post(self.url, json = data, headers = self.head)
      return requisicao_post

   ##PUT

   def put_user_data(self, id, data):
      request_put = requests.put(self.url + id, json = data, headers = self.head)
      return request_put

   ##DELETE

   def delete_user(self, id):
      request_delete = requests.delete(self.url + id, headers = self.head)
      return request_delete.status_code
   
   