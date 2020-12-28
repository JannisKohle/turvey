#!/bin/python3

import sys
import os
import matplotlib

if sys.argv[1] == "create":
    surveyName = input("Name of survey: ")
    questions = []
    while True:
        print("\n[a] to add question | [q] to quit | [s] to submit")
        option = input()
        if option in ["a", "add", "[a]"]:
            title = input("Question title: ")
            print("\n[1] for Right or Wrong | [2] for Multiple Choice | [3] for number")
            while True:
                type = input("Question type: ")
                if type in ["1", "[1]"]: # Right or Wrong
                    break

                elif type in ["2", "[2]"]: # Multiple Choice
                    choices = input("Type all the choices seperated by ';': ").split(";")

                elif type in ["3", "[3]"]: # Number
                    minimum = input("Minimum: ")
                    maximum = input("Maximum: ")
                    minimum = minimum if minimum.isnumeric() else None
                    maximum = maximum if maximum.isnumeric() else None

                else:
                    print("Invalid type => Choose again")

        elif option in ["q", "quit", "[q]"]:
            pass

        elif option in ["s", "submit", "[s]"]:
            pass

        else:
            print("Invalid option => Quitting")
            exit()

elif sys.argv[1] == "visualize":
    pass

elif sys.argv[1] == "do":
    pass

elif sys.argv[1] in ["help", "--help", "h", "-h"]:
    pass

else:
    print("Usage: https://www.github.com/JannisKohle/turvey#Usage")
    exit()
