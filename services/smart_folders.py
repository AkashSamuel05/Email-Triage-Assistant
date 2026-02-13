def assign_folder(category):

    folders = {
        "Work": "Work Folder",
        "Personal": "Personal Folder",
        "Spam": "Spam Folder",
        "Important": "Priority Folder"
    }

    return folders.get(category, "General")
