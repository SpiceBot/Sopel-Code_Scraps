#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals, absolute_import, print_function, division

# sopel imports
import sopel.module

# imports for system and OS access, directories
import os
import sys


# Ensure Encoding
reload(sys)
sys.setdefaultencoding('utf-8')


"""
This will restart the bots service
"""


@nickname_commands('restart')
@sopel.module.thread(True)
def bot_command_hub(bot, trigger):

    if not trigger.admin:
        return osd(bot, trigger.nick, 'notice', "I was unable to process this Bot Nick command due to privilege issues.")

    stderr("Recieved Command to update.")
    osd(bot, bot.privileges.keys(), 'say', "Received command from " + trigger.nick + " to restart systemd service. Be Back Soon!")

    # restart systemd service
    service_manip(bot, str(bot.nick), "restart")


def service_manip(bot, servicename, dowhat):
    if str(dowhat) not in ["start", "stop", "restart"]:
        return
    try:
        stderr(str(dowhat).title() + "ing " + str(servicename) + ".service.")
        os.system("sudo service " + str(servicename) + " " + str(dowhat))
    except Exception as e:
        stderr(str(dowhat).title() + "ing " + str(servicename) + ".service Failed: " + str(e))
