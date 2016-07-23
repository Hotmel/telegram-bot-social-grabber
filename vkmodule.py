import vk

session = vk.Session()
api = vk.API(session)
print(api.users.get(user_ids=1))