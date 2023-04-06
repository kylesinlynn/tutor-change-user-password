from tutor import hooks

hooks.Filters.ENV_PATCHES.add_item(
    (
        "openedx-common-settings",
        "FEATURES['ENABLE_CHANGE_USER_PASSWORD_ADMIN'] = True"
    )
)