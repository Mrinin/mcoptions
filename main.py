import os
import shutil
from pathlib import Path
from tkinter import *
from tkinter import filedialog

# SETUP INTERFACE AND PATH ENTER
root = Tk()

computer_name = ""
mco_filepath = ""
mcm_filepath = ""
total_loadouts = 0
available_load = []

def main():
    root.title("MCOptions")
    root.resizable(False, False)

    canvas = Canvas(root, height=450, width=640, bg="#e3e3e3")
    canvas.pack(expand=True)

    # Computer Name created earlier
    global mco_filepath
    global mcm_filepath
    global computer_name
    temp_path = os.path.expanduser('~') + "/AppData/Roaming/.minecraft/"
    computer_name = temp_path + "options.txt"

    if not os.path.exists(temp_path + "mco_loadouts"):
        os.mkdir(temp_path + "mco_loadouts")

    mcm_filepath = temp_path + "mods/"
    mco_filepath = temp_path + "mco_loadouts/"

    actual_program(" ")


# ACTUAL PROGRAM
def actual_program(message):

    # SETUP MAIN INTERFACE
    program_frame = Frame(root, bg="#e3e3e3")
    program_frame.place(relwidth=1, relheight=1, relx=0, rely=0)

    # IT'S ME
    itsme = Label(program_frame, bg="#e3e3e3", text="Made by Mrinin")
    itsme.place(relwidth=0.5, relheight=0.1, relx=0.65, rely=0.9)

    # SHOW CURRENT PATH
    path_text = "Current options.txt Path: " + computer_name
    current_path = Label(program_frame, text=path_text, bg="#e3e3e3")
    current_path.grid(row=1, column=0)

    # LOAD INTERFACE
    load_label = Label(program_frame, bg="#e3e3e3", text="Load...")
    load_label.place(relwidth=0.3, relheight=0.1, relx=0.1, rely=0.1)

    # SAVE INTERFACE
    save_label = Label(program_frame, bg="#e3e3e3", text="Save...")
    save_label.place(relwidth=0.3, relheight=0.1, relx=0.6, rely=0.12)

    name_plz_label = Label(program_frame, bg="#e3e3e3", text="Name of Loadout")
    name_plz_label.place(relwidth=0.3, relheight=0.05, relx=0.6, rely=0.25)

    name_set = Entry(program_frame, text="das", bg="#e3e3e3")
    name_set.place(relwidth=0.2, relheight=0.05, relx=0.65, rely=0.3)

    save_button1 = Button(program_frame, text="Save current options.txt as a Loadout ⚙",
                         command=lambda: save(name_set.get(), True, False), bg="#333333", foreground="#d4d4d4")
    save_button1.place(relwidth=0.35, relheight=0.05, relx=0.57, rely=0.37)

    save_button2 = Button(program_frame, text="Save current mods folder as a Loadout 🔨",
                         command=lambda: save(name_set.get(), False, True), bg="#333333", foreground="#d4d4d4")
    save_button2.place(relwidth=0.35, relheight=0.05, relx=0.57, rely=0.44)

    save_button3 = Button(program_frame, text="Save both current mods folder\n and options.txt as a Loadout ⚙ 🔨",
                         command=lambda: save(name_set.get(), True, True), bg="#333333", foreground="#d4d4d4")
    save_button3.place(relwidth=0.35, relheight=0.09, relx=0.57, rely=0.51)

    # MESSAGE SHOW
    message_lb = Label(program_frame, bg="#e3e3e3", text= message)
    message_lb.place(anchor= CENTER, relx=0.75, rely=0.7)

    # GET BUTTONS FOR LOADING
    global available_load
    available_load.clear()

    if not os.path.exists(mco_filepath + "saved_loadouts.txt"):
        open(mco_filepath + "saved_loadouts.txt", "x")
    else:
        available_load_new_lined = open(mco_filepath + "saved_loadouts.txt", "r").readlines()
        for string in available_load_new_lined:
            string = string.strip('\n')
            if string != "":
                available_load.append(string)

    index = 0

    load_buttons = [0, 1, 2, 3, 4, 5, 6]
    delete_buttons = [0, 1, 2, 3, 4, 5, 6]

    # SHOW LOAD BUTTONS
    for string in available_load:
        string_addition = ""
        if Path(mco_filepath + string + "/load_mods").exists():
            string_addition = " 🔨"
        if Path(mco_filepath + string + "/load_opts.txt").exists():
            string_addition = string_addition + " ⚙"

        string = string + string_addition

        if index == 0:
            load_buttons[index] = Button(program_frame, text=string, command=lambda: load(available_load[0]),
                                         bg="#333333", foreground="#d4d4d4", width= 15)
            delete_buttons[index] = Button(program_frame, text= "X", command=lambda: delete(available_load[0]),
                                         bg="#333333", foreground="#d4d4d4")
        if index == 1:
            load_buttons[index] = Button(program_frame, text=string, command=lambda: load(available_load[1]),
                                         bg="#333333", foreground="#d4d4d4", width= 15)
            delete_buttons[index] = Button(program_frame, text= "X", command=lambda: delete(available_load[1]),
                                         bg="#333333", foreground="#d4d4d4")
        if index == 2:
            load_buttons[index] = Button(program_frame, text=string, command=lambda: load(available_load[2]),
                                         bg="#333333", foreground="#d4d4d4", width= 15)
            delete_buttons[index] = Button(program_frame, text= "X", command=lambda: delete(available_load[2]),
                                         bg="#333333", foreground="#d4d4d4")
        if index == 3:
            load_buttons[index] = Button(program_frame, text=string, command=lambda: load(available_load[3]),
                                         bg="#333333", foreground="#d4d4d4", width= 15)
            delete_buttons[index] = Button(program_frame, text= "X", command=lambda: delete(available_load[3]),
                                         bg="#333333", foreground="#d4d4d4")
        if index == 4:
            load_buttons[index] = Button(program_frame, text=string, command=lambda: load(available_load[4]),
                                         bg="#333333", foreground="#d4d4d4", width= 15)
            delete_buttons[index] = Button(program_frame, text= "X", command=lambda: delete(available_load[4]),
                                         bg="#333333", foreground="#d4d4d4")
        if index == 5:
            load_buttons[index] = Button(program_frame, text=string, command=lambda: load(available_load[5]),
                                         bg="#333333", foreground="#d4d4d4", width= 15)
            delete_buttons[index] = Button(program_frame, text= "X", command=lambda: delete(available_load[5]),
                                         bg="#333333", foreground="#d4d4d4")
        if index == 6:
            load_buttons[index] = Button(program_frame, text=string, command=lambda: load(available_load[6]),
                                         bg="#333333", foreground="#d4d4d4", width= 15)
            delete_buttons[index] = Button(program_frame, text= "X", command=lambda: delete(available_load[6]),
                                         bg="#333333", foreground="#d4d4d4")
        if index == 7:
            load_buttons[index] = Button(program_frame, text=string, command=lambda: load(available_load[7]),
                                         bg="#333333", foreground="#d4d4d4", width= 15)
            delete_buttons[index] = Button(program_frame, text= "X", command=lambda: delete(available_load[7]),
                                         bg="#333333", foreground="#d4d4d4")

        load_buttons[index].place(anchor=CENTER, relx=0.22, rely=(0.1 * index) + 0.22)
        delete_buttons[index].place(anchor=CENTER, relx=0.33, rely=(0.1 * index) + 0.22)

        index = index + 1
        if index == 8:
            break

    # SAVE TOTAL LOADOUT COUNT AS A GLOBAL
    global total_loadouts
    total_loadouts = index

    root.mainloop()

def delete(name):
    #os.remove(mco_filepath + name + ".txt")
    shutil.rmtree(mco_filepath + name)

    # CREATE LISTS
    available_load_new = []
    available_load_new_lined = []
    available_load_new_er = []

    # DELETE THE ERASED THING FROM THE LIST(TM)
    available_load_new_lined = open(mco_filepath + "saved_loadouts.txt", "r").readlines()
    for string in available_load_new_lined:
        string = string.strip('\n')
        if string != "":
            if string != name:
                available_load_new.append(string)

    open(mco_filepath + "saved_loadouts.txt", "w").close()
    available_load_new_er = open(mco_filepath + "saved_loadouts.txt", "a")
    for string in available_load_new:
        available_load_new_er.write(string + "\n")
    available_load_new_er.close()
    actual_program(name + " successfully deleted")

def load(to_be_loaded):

    if Path(mco_filepath + to_be_loaded + "/load_mods").exists():
        if Path(mcm_filepath).exists():
            print(mcm_filepath)
            shutil.rmtree(mcm_filepath)
        shutil.copytree(mco_filepath + to_be_loaded + "/load_mods", mcm_filepath)

    if Path(mco_filepath + to_be_loaded + "/load_opts.txt").exists():
        loaded_file = open(mco_filepath + to_be_loaded + "/load_opts.txt", "r")
        open(computer_name, "r+").write(loaded_file.read())
        loaded_file.close()

    actual_program("Successfully loaded the loadout named: \n" + to_be_loaded)


def save(name, is_options, is_mods):
    errors = True
    if total_loadouts >= 7:
        actual_program("Only a maximum of 7 loadouts\ncan be saved! Please delete\nsome first.")
    else:
        if name == "":
            actual_program("Please enter a name.")
        else:
            # CHECK FOR DUPLICATE LOADOUT SAVE
            name_duplicate = False
            for j in available_load:
                if j == name:
                    name_duplicate = True
                    break

            if name_duplicate:
                actual_program( name + " is already being used!")
            else:
                if is_mods:
                    if os.path.exists(mcm_filepath):
                        errors = False
                    else:
                        actual_program("There is no mods folder in\nminecraft root folder!")
                else:
                    print("?*")
                    errors = False

    if not errors:
        print("what")
        os.mkdir(mco_filepath + name)
        if is_mods:
            shutil.copytree(mcm_filepath, mco_filepath + name + "/load_mods")

        if is_options:
            saved_file = open(mco_filepath + name + "/load_opts.txt", "w")
            save_options = open(computer_name, "r").read()
            saved_file.write(save_options)
            saved_file.close()

        file_lists = open(mco_filepath + "saved_loadouts.txt", "a")
        file_lists.write(name + "\n")
        file_lists.close()

        actual_program("Successfully saved a loadout as: \n" + name)

def get_load_path():
    return filedialog.askopenfilename(title="Select options.txt",
                                      filetypes=(("Text Files", ".txt"), ("All Files", ".*")))

main()
