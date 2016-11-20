import configparser
import os

def crudConfig(path):

    if not os.path.exists(path):
        createConfig(path)

    config = configparser.ConfigParser()
    config.read(path)

    #Read some values from the config
    font = config.get("Settings", "font")
    print(font)
    font_size = config.get("Settings", "font_size")
    print(font_size)

    #Change a value in the config
    config.set("Settings", "font_size", "17")
    print(config.get("Settings", "font_size"))
    

    #Delete a value from the config
    config.remove_option("Settings", "font_style")

    #Write changes back to config file
    with open(path, "w") as config_file:
        config.write(config_file)

if __name__ == "__main__":
    path = "settings.ini"
    crudConfig(path)
