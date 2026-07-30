# Platform Surveillance System

## 1. Project Description

Platform Surveillance System is a Python automation project that monitors system information such as running processes, CPU usage, RAM usage, and network activity. It generates a timestamp-based log file and sends the log file to the specified email address at a scheduled time interval.

---

## 2. Features

* Monitor running processes
* Display PID, Process Name, Username and Status
* Monitor CPU, RAM and Network usage
* Generate timestamp-based log files
* Schedule tasks periodically
* Send log file through email
* Command-line argument support
* Exception handling

---

## 3. Requirements

### Python Version

* Python 3.14.5 or later

### Required Libraries

* psutil
* schedule
* smtplib
* python-dotenv

### Other Requirements

* Internet connection
* Gmail App Password
* `.env` file for email credentials

---

## 4. Project Structure

```text
PlatformSurveillance/
│
├── PlatformSurveillance.py
├── SendMail.py
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
└── Demo/
```

---

## 5. Command-Line Arguments

| Argument       | Description                             |
| -------------- | --------------------------------------- |
| Time Interval  | Time interval in minutes                |
| Folder Name    | Folder to store log files               |
| Receiver Email | Email address to receive the log report |

---

## 6. Execution Command

```bash
python PlatformSurveillance.py <TimeInterval> <FolderName> <ReceiverEmail>
```

### Example

```bash
python PlatformSurveillance.py 5 Demo example@gmail.com
```

---

## 7. Help Command

```bash
python PlatformSurveillance.py --h
```

Displays the purpose and features of the project.

---

## 8. Usage Command

```bash
python PlatformSurveillance.py --u
```

Displays the correct syntax to run the application.

---

## 9. Log File Information

* Log files are stored in the **Logs** folder.
* A new log file is created for every execution.
* Each log contains CPU, RAM, Network and Process information.

---

## 10. Email Configuration

Create a `.env` file and add:

```text
EMAIL=your_email@gmail.com
PASSWORD=your_google_app_password
```

Do not upload the `.env` file to GitHub.

---

## 11. Expected Output

* System information is collected.
* A log file is generated.
* The log file is stored in the **Demo** folder.
* The log file is sent to the receiver through email.

---

## 12. Author

**Ankita Bhosale**

Python Automation Project
