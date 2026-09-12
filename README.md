# ALL RISK NO REWARD

A multiplayer auction and trading game built with:

- **Python + FastAPI** for the backend
- **React + Vite** for the frontend
- **WebSockets** for live multiplayer updates

The game is designed to be hosted by one computer while other players connect using the host computer's IP address.

---

## 1. Requirements

Before running the setup script, install:

- **Python 3** — https://www.python.org/downloads/
- **Node.js + npm** — https://nodejs.org/en/download
- **Git** — https://git-scm.com/downloads

You can check that they are installed with:

```bash
python --version
node --version
npm --version
git --version
```

On macOS, you may need to use:

```bash
python3 --version
```

---

## 2. Clone the Repository

```bash
git clone https://github.com/minhmInhmIh/ALL-RISK-NO-REWARD.git
cd ALL-RISK-NO-REWARD
```

---

## 3. Find Your Host IP Address

You will need the IP address of the computer that will host the game.

### Windows

Open Command Prompt and run:

```bat
ipconfig
```

Look for the IPv4 address of the network you want players to use.

If you are using Radmin VPN, use your **Radmin VPN IP address**.

### macOS

Open Terminal and run:

```bash
ipconfig getifaddr en0
```

If that does not return an address, check:

```bash
ifconfig
```

Use the IP address of the network that the other players can reach.

---

# Windows Setup

## 4. Run the Setup Script

Run:

```bat
./setup.bat
```

The script will ask:

```text
Enter your IP address:
```

Paste the host computer's IP address and press Enter.

The setup script will:

1. Create the backend `.env`
2. Create the frontend `.env`
3. Save your IP address into both files
4. Install Python dependencies from `requirements.txt`
5. Install frontend dependencies with `npm install`

The generated environment files will contain:

Backend `.env`:

```env
IP_ADDRESS=YOUR_IP
```

Frontend `frontend/.env`:

```env
VITE_IP_ADDRESS=YOUR_IP
```

---

## 5. Start the Game on Windows

Run:

```bat
./start.bat
```

Two terminal windows should open:

- FastAPI backend on port **8000**
- Vite frontend on port **5173**

The backend runs on:

```text
http://0.0.0.0:8000
```

The frontend is available to other players at:

```text
http://YOUR_IP:5173
```

For example:

```text
http://192.168.1.20:5173
```

or, when using Radmin VPN:

```text
http://26.x.x.x:5173
```

Send that frontend address to the other players.

---

# macOS Setup

## 4. Make the Scripts Executable

The first time you use the project, run:

```bash
chmod +x setup.sh
chmod +x start.sh
```

---

## 5. Run the Setup Script

Run:

```bash
./setup.sh
```

The script will ask for your host IP address.

It will then:

1. Create the backend `.env`
2. Create the frontend `.env`
3. Save your IP address
4. Install Python dependencies
5. Install frontend dependencies

---

## 6. Start the Game on macOS

Run:

```bash
./start.sh
```

The script opens separate Terminal sessions for:

- FastAPI backend
- Vite frontend

Players connect using:

```text
http://YOUR_IP:5173
```

---

# Joining the Game

Once the host has started both servers:

1. Open a browser.
2. Go to:

```text
http://HOST_IP:5173
```

3. Enter a team/player name.
4. Click **Join**.

The lobby updates live for all connected players.

A player who has already joined in the same browser tab will remain joined after refreshing because the player ID is stored in `sessionStorage`.

Players can also leave the lobby using the **Leave** button.

---

# Important Networking Notes

## `localhost` vs Host IP

Do **not** send players a URL using:

```text
http://localhost:5173
```

`localhost` always refers to the computer currently opening the page.

Only the host can normally use localhost.

Other players must use:

```text
http://HOST_IP:5173
```

---
