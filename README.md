# Multi-User-Chat-Program

<div align="center">

<img alt="GitHub Created At" src="https://img.shields.io/github/created-at/KieranPritchard/Multi-User-Chat-Program">

<img alt="GitHub License" src="https://img.shields.io/github/license/KieranPritchard/Multi-User-Chat-Program">

<img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/t/KieranPritchard/Multi-User-Chat-Program">

<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/KieranPritchard/Multi-User-Chat-Program">

<img alt="GitHub language count" src="https://img.shields.io/github/languages/count/KieranPritchard/Multi-User-Chat-Program">

<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/KieranPritchard/Multi-User-Chat-Program">

</div>

## Project Description
### Objective
To practise making a multi client app using Python and its socket library. To also create an foundation for multi client which I can then replicate when needed for similar apps, mainly so I don't fumble around getting lost with what to do.
### Features
* **Multi-Client Support:** The server uses threading to manage multiple clients simultaneously.
- **Message Broadcasting:** Messages from one client are broadcasted to all connected clients.
- **User-Friendly Commands:** Clients can send messages and exit using the `quit` command.
### Tools and Langauges 
* **Languages:** Python.
* **Frameworks/Librarys:** socket.
* **Tools:** Git, VS Code.
### Challenges Faced
Learning how to use sockets with threading, because it was a new thing to me to learn how to use. I overcame this by googling and consulting ChatGPT to see how to use it. Other then that, I didn't have any problems with building this. As i referred to my previous project for guidance.
### Outcome
Successfully created the programs needed to facilitate real-time communication and built a backbone which I can use in other projects. 

## How to Use the Project
1. **Prerequisites:**
	* Check if python is installed in your system
	* Then check if you have access to a terminal or command prompt.
2. **Clone The Repository:**
	* Clone the repository to your local computer.
3. **Start The Server:**
	* Open the terminal or command prompt.
	* Navigate to the directory where `server.py` is located using the `cd` command: `cd path/to/your/folder`.
	* Run the server with the following command: `python server.py`.
	* You should see a message indicating the server is listening on `127.0.0.1:12345`.
4. **Start a Client:**
	* Open a **new** terminal or command prompt.
	* Navigate to the directory containing `client.py`.
	* Run the client using the following command:`python client.py`
	* After connecting to the server, you will see a prompt to type your messages.
5. **Test Communication:** 
	* Type a message and press `Enter`. The message will be sent to the server and then broadcasted to all connected clients.
	* Open additional terminals and run more clients using the same `python client.py` command.
	* Confirm that all clients receive each other's messages.
6. **Disconnect:**
	* To disconnect a client, type `quit` and press `Enter`.
	* The connection will close, and the client will exit.
	* The server will print a message confirming the disconnection.
7. **Additional Notes** 
	* The server uses threading to handle multiple clients simultaneously.
	* Messages are broadcasted to all clients except the sender.
	* If any errors occur, appropriate messages will be displayed.

## Licenses
License can be found in root of the repository.
