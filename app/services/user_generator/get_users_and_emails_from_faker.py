import faker

faker = faker.Faker()

def get_users_and_emails_from_faker(amount_of_users: int) -> tuple[list[list[str]], str]:
    users_list = [[faker.first_name(), faker.email()] for el in range(amount_of_users)]
    users_text = "".join([f"{user[0]} {user[1]}\n" for user in users_list]).rstrip("\n")
    return users_list, users_text