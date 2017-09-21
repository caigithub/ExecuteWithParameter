it will start the external command

you could config the command with hotkey like :

    {
        "keys": ["shift+f11"],
        "command": "execute_with_parameter",
        "args":
        {
            "cmd_path": "C:/port/ol/ol_view.bat"
        }
    },

    {
        "keys": ["f11"],
        "command": "execute_with_current_word_as_parameter",
        "args":
        {
            "cmd_path": "C:/port/ol/ol_view_in_new_console.bat"
        }
    }


the cmd with be exected as
    cmd current_file_name current_word
