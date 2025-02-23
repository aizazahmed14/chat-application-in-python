A simple terminal-based chat application built with Python using sockets. This project includes both server and client scripts, allowing real-time text communication between multiple users over a local network.

# 💬 Python Chat Application

A simple and interactive **real-time chat application** built in Python using socket programming. This project demonstrates how to create a basic client-server architecture where users can send and receive messages simultaneously over a local network.

---

## 🚀 Features

- Real-time messaging between users.
- Multi-client support.
- Simple terminal-based interface.
- Easy to set up and run.

---

## 🔧 Tech Stack

- **Python 3**
- **Socket Programming**

---

## 📂 Project Structure

python-chat-application/ │ 
  ├── client.py # Client-side script for sending and receiving messages 
  ├── server.py # Server-side script for managing connections 
  ├── README.md # Project documentation


---

## ✅ Prerequisites

Before running this application, ensure you have:

- Python 3 installed on your machine. [Download Python](https://www.python.org/downloads/)
- Basic knowledge of using the terminal or command prompt.

---

## ⚙️ Installation and Setup

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/python-chat-application.git
cd python-chat-application

```

2. **Create Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. **Run the Server**
Start the server to listen for incoming connections.
```bash
python server.py
```

4. **Run the Client**
Open another terminal window and run the client.
```bash
python client.py
```

You can run multiple instances of client.py to simulate different users.

## 💻 Usage Guide
1. Run server.py first. You should see:
```bash
Server is running and listening for connections...
```

2. Launch client.py. You’ll be prompted to enter a message.
3. Start typing your message and hit Enter to send.
4. Type exit to close the chat from the client side.


## 🔒 Troubleshooting
If you face connection issues:

Ensure the server is running before starting the client.
Check if the port 55556 is available and not in use by another application.
Restart both client and server scripts.
### Common Errors:

**OSError: Address already in use:** Kill any other process using the same port.
**ConnectionRefusedError:** Ensure the server is running before launching the client.


## 📜 License
This project is licensed under the MIT License.

## 🙌 Acknowledgements
This project was built to practice Python's socket programming and networking fundamentals.


## 📞 Contact
Created by Muhammad Aizaz - Feel free to reach out!
