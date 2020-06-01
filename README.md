### Requirements
Python3.8 and libs in requirements.txt
### Setup
`cd codies-backend` and `pip install -r requirements.txt`
### Run
`python3.8 main.py` or `uvicorn main:app --reload` for test locally.
### Deployment
You may need these tools:
- Tmux as a terminal multiplexer.
- systemd offers daemons and keeps tracks of processes.
- Supervisor or Circus as a process manager.
- Nginx as a proxy in front of your Uvicorn processes.