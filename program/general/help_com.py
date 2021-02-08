from program.viewing.custom_color import color


def get_help():
    """
    Return useful information about the available commands.

    :return: help_info
    :rtype: str
    """
    return f'''

# See {color.f_d_y}README.md{color.end} for user instructions.



Usage: {color.f_green}clinic{color.end} \
 {color.f_l_b}<command_name>{color.end} {color.f_l_y} \
--[command_argument_name]{color.end}



Available Commands:

    {color.f_l_b}help{color.end} {f"-".rjust(14)} Displays \
information on how to use the commands and
                        command arguments.

    {color.f_l_b}init{color.end} {f"-".rjust(14)} Configures the \
program to use your personal WethinkCode
                        email and calendar.

    {color.f_l_b}view{color.end} {f"-".rjust(14)} Displays a \
list of events from your WethinkCode calendar
                        or the CodingClinic's calendar.

    {color.f_l_b}volunteer{color.end} {f"-".rjust(9)} Adds a \
90 minute slot on the CodingClinic's
                        Calendar as a clinician.

    {color.f_l_b}book{color.end} {f"-".rjust(14)} Allocates \
30 minutes from a clinician's slot to a patient.

    {color.f_l_b}cancel_volunteer{color.end} {f"-".rjust(2)} \
Removes a clinician's 90 minute slot from the CodingClinic's
                        calendar.

    {color.f_l_b}cancel_booking{color.end} {f"-".rjust(4)} \
Removes the relevant 30 minutes from a patient and returns
                        it to the relevant clinician's slot.



Command Arguments:

    {color.f_l_y}--reload{color.end} {f"-".rjust(10)} Updates the \
Google Calendar data to display the newest version 
                        of the Google Calendars' data.



{f"{color.f_d_i_y}Type 'exit' or 'quit' to close the "
f"CodeClinic program.{(color.end)}".center(105)}
'''
