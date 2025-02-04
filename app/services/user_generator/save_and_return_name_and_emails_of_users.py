from app.services.user_generator.get_users_and_emails_from_faker import get_users_and_emails_from_faker
from app.services.user_generator.save_file import save_file


def save_and_return_name_and_emails_of_users(amount_of_users: int, format_file: str|None) -> str:
    users_list, users_text = get_users_and_emails_from_faker(amount_of_users=amount_of_users)
    if format_file:
        save_file(name_file="user_generator",
                  format_file=format_file,
                  data_for_save=users_text if "txt" in format_file else users_list)
        return f"Saved {amount_of_users} users in 'files_output/{format_file}'"
    return users_text