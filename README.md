# LogsAnalysisProject
An internal reporting tool that uses python to query a PostgreSQL database of over 1 million lines to determine viewership and user error on a news site.

## Technologies Used in this Project:

PostgreSQL

Linux VM - Vagrant

Python DB-API

## What You'll Need to Run:

[Vagrant](https://www.vagrantup.com/)

[VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)

[Udacity VM](https://github.com/udacity/fullstack-nanodegree-vm)

## Running the Program 

This project is configured in the Udacity FSND Linux-Based Virtual Machine.

1. Download both VirtualBox and Vagrant and install.

2. Clone the Udacity VM.

3. Clone this repository and place the files in the files in the 'Vagrant' directory. 

4. Call 'vagrant up' with Terminal or Command Line in the 'vagrant' directory. You can check your status by calling 'vagrant ssh'. This will launch the VM, givng you the capability to access the news database.

5. Run 'newsdb.py' in Terminal / Command Line by calling 'python newsdb.py'. It will take a few seconds and then the output featured in 'output.txt' will be displayed in the shell. 
