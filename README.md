# Cryptocurrency-Address
REST API for generating valid cryptocurrency addresses and displaying them
This project designed for technical challenge Ziply .co by Farzad Ekhtiardini.
The base of this project is written in django that logged in users can have two wallet in the program.
For each wallet generate : Bitcoin, Ethereum, and Litecoin.
------------
sqlite is used to store data, you can check the diagram from the link below:
    https://github.com/Ekhtiardini/Cryptocurrency-Address/blob/main/drawSQL-walletdb-export-2023-05-03.png
1.Creating new currency can only be done by super user
2.The list of all addresses and their management on the admin page
  username : admin
  password : 123
  link : 127.0.0.1:8000/admin
3.It is possible to control each of the tables inside the programs created in Django
------------
After setting up the libraries used in the program that are placed in the requirement.txt file, by executing the manager.py runserver command,
the program is fully available on the web and you can test it.

------------
The list of all addresses is available in the admin.
* What is needed for implementing the next steps, such as signing transactions? Is your 
code and data ready for that? To sign transactions, you can use ARM hardware tokens or use hashed text keys provided by the software.

*How would you back up your private keys? For reliable backup, parallel servers can be used, which can be used in case of disruption.

*How should a teammate add support for a new coin to the API? I have written each part of the project as a separate program so that it can be easily available 
in case of team work or the need to edit a part of the program.
Just add the new part to the program.

*The format you’ve chosen for inputs and outputs of the API! This program could be run on a variety of programming formats, 
but I always consider the fast and reliable way to run, that's why I used the web on Django.
******************************
github link : https://github.com/Ekhtiardini/Cryptocurrency-Address/tree/main
Thank you for giving me your time.
Best regards.




