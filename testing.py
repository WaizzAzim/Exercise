# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

 def guess_my_number();:
     number = 16
     number_of_tries=0
     while True:
         try:
             x=int(raw_input("Please enter a number: "))
         except ValueError:
             print("Oops! That was no valid number. Try again...")