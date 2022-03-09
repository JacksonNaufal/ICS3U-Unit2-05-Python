# Copyright (c) 2022 Jackson Naufal All rights reserved
# Created By Jackson Naufal
#  Created On March 2022
#  This is a "Global Variable Program"  with proper style"
variable_X = 25

def local_variable():
# this shows what happens when you use local variables
    variable_X = 10
    variable_Y = 30
    variable_Z = variable_X + variable_Y
    print("Local variable_X, variable_Y, variable_Z: {0} + {1} = {2}".
        format(variable_X, variable_Y, variable_Z))

def global_variable():
# this shows what happens when use use global variables
    global variable_X
    variable_X = variable_X + 1
    variable_Y = 30
    variable_Z = variable_X + variable_Y


    print("Global variable_X, variable_Y, variable_Z: {0} + {1} = {2}".
        format(variable_X, variable_Y, variable_Z))

def main():
    # this function shows how both local and global variables are
    local_variable()
    global_variable()

if __name__ == "__main__":
    main()