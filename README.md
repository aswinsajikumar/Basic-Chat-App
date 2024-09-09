## Chat Application with Flask and Socket.IO
### Overview
This is a real-time chat application built using Flask (a Python web framework) and Socket.IO for handling real-time communication between users. It allows multiple users to send and receive messages instantly, and all messages are stored in a PostgreSQL database.

### Features
Real-time chat: Messages are sent and received instantly using WebSockets (Socket.IO).

Database storage: All messages are stored in a PostgreSQL database so they can be retrieved later.

Simple UI: A basic user interface where users can enter their username and chat messages.

APIs: There are APIs to get the chat history and to send messages via HTTP requests.

### Working
Users enter their username and message in the User Interface.
Messages are sent to the server using WebSockets and broadcasted to all connected users in real-time.
Each message is saved to the PostgreSQL database, so the chat history is stored.
Users can retrieve the chat history using a GET request to the /messages API endpoint.

* I used Pycharm as the IDE and initialized a virtual environment.
