from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    # Rename accounts to persian
    verbose_name = "حساب کاربری"

    def ready(self):
        import accounts.signals