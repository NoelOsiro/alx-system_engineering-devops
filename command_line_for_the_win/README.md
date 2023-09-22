# Project README

## Overview

This project demonstrates how to transfer files from a local Windows machine to a remote server using the Windows Command Prompt and the `sftp` command. The project includes step-by-step instructions and guidelines for performing the file transfer securely.

## Requirements

- Windows operating system
- Access to a remote server with SFTP access (hostname, username, and password provided)

## SFTP File Transfer Instructions

### Step 1: Open Command Prompt

Open the Command Prompt on your Windows machine.

### Step 2: Navigate to the Directory

Use the `cd` command to navigate to the directory where your files are located. For example:

```bash
cd C:\Users\noelo\OneDrive\Desktop\pics
```

### Step 3: Launch SFTP

To initiate an SFTP session, use the `sftp` command followed by the username and hostname of the remote server. Replace `<username>` and `<hostname>` with your actual credentials.

```bash
sftp <username>@<hostname>
```

### Step 4: Authenticate

Enter your password when prompted to authenticate with the remote server.

### Step 5: Navigate to the Destination Directory

Use the `cd` command to navigate to the directory on the remote server where you want to transfer the files. For example:

```bash
cd /path/to/destination/directory
```

### Step 6: Transfer Files

Use the `put` command to transfer files from your local machine to the remote server. You can specify the filename(s) you want to transfer or use wildcards for multiple files. For example:

```bash
put example.txt
put *.jpg
```

### Step 7: Confirm Transfer

After the transfer is complete, you should see the transferred files in the remote directory on the server.

## Additional Information

- Make sure to replace `<username>`, `<hostname>`, and other placeholders with your actual credentials and file paths.
- Ensure that you have appropriate permissions and access rights on both your local machine and the remote server.
- Be cautious when transferring sensitive or important files, and always confirm the success of the transfer.

## References

- [SFTP Guide](https://example.com/sftp-guide)
- [SFTP File Transfer Tutorial](https://example.com/sftp-tutorial)
- 
