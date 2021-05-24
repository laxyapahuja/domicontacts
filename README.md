# domicontacts
sync google contacts with information from the dominos data breach

## usage
1. open tor browser in the background
2. `pip install -r requirements.txt`
3. go to [google contacts website](https://contacts.google.com)
4. export your contacts and save them in the cloned repository directory
5. `python script.py`
6. after the program is done running (it can take a long time depending on the number of contacts you have), the contacts.csv will be updated with email address and address of every contact which was available on the api
7. if there is any error during the process, note down the index and replace it with the index variable and run it again
9. import the updated csv on google contacts again and merge all the contacts with the existing ones
