# import pytest
# from flask import session
# from Crypto.Cipher import AES
# from Crypto.Util.Padding import pad
# import base64
# import time


# def encrypt_password(password, key):
#     cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
#     encrypted = cipher.encrypt(pad(password.encode('utf-8'), AES.block_size))
#     return base64.b64encode(encrypted).decode('utf-8')

# def test_register(client):
#     key = "2130702421307024"  # 与前端一致的密钥
#     password = "password123"
#     encrypted_password = encrypt_password(password, key)
#     unique_username = f'newuser2_{int(time.time())}'

#     response = client.post('/register', data={
#         'username': unique_username,
#         'password': encrypted_password,
#         'email': 'newuser@example.com',
#         'sex': 'M',
#         'birthday': '1990-01-01',
#         'address': '123 Main St',
#         'phone': '1234567890'
#     })
    
#     assert response.status_code == 302  # 检查是否重定向
#     assert b'Invalid info for registration' not in response.data


# def test_login(client):
#     # 模拟用户登录
#     key = "2130702421307024"
#     password = '123456'
#     encrypted_password = encrypt_password(password, key)
#     response = client.post('/login', data={
#         'username': 'lz',
#         'password': encrypted_password,
#     })

#     assert response.status_code == 302  # 检查是否重定向
#     assert b'Invalid username or password' not in response.data


# def test_logout(client):
#     # 模拟用户登出
#     with client.session_transaction() as sess:
#         sess['username'] = 'testuser'
#     response = client.get('/logout')
#     assert response.status_code == 302  # 检查是否重定向
#     with client.session_transaction() as sess:
#         assert 'username' not in sess

# def test_add_to_cart(client):
#     # 模拟添加商品到购物车
#     with client.session_transaction() as sess:
#         sess['username'] = 'testuser'
#     response = client.post('/add_to_cart', data={
#         'goods_name': 'keyboard'
#     })
#     assert response.status_code == 302  # 检查是否重定向

# def test_show_cart(client):
#     # 模拟查看购物车
#     with client.session_transaction() as sess:
#         sess['username'] = 'testuser'
#     response = client.get('/cart')
#     assert response.status_code == 200  # 检查页面是否成功加载
#     assert b'Shopping Cart' in response.data
