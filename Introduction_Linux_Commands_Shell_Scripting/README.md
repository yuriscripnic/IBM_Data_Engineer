# Final Project - Scenario
Imagine that you are a lead Linux developer at the top-tech company ABC International Inc. ABC currently suffers from a huge bottleneck: each day, interns must painstakingly access encrypted password files on core servers and back up any files that were updated within the last 24 hours. This process introduces human error, lowers security, and takes an unreasonable amount of work.

As one of ABC Inc.'s most trusted Linux developers, you have been ### Tasked with creating a script called backup.sh which runs every day and automatically backs up any encrypted password files that have been updated in the past 24 hours.

## Deliverables

- [### Tasks 1-13]: Upload screenshot of sections from the backup.sh script displaying the correct code (13 pts: 1 pt for - each of the 13 ### Tasks)
- [### Task 14]: Submit your completed backup.sh file (1 pt)
- [### Task 15]: Upload screenshot showing executable permissions (2 pts)
- [### Task 16]: Upload screenshot showing file named backup-[TIMESTAMP].tar.gz (2 pts)
- [### Task 17]: Upload screenshot showing crontab schedule of once every day (2 pts)

### ### Task 1
Navigate to # [### Task 1] in the code.

Set two variables equal to the values of the first and second command line arguments, as follows:

Set targetDirectory to the first command line argument
Set destinationDirectory to the second command line argument
This Task is meant to help with code readability.

Click here for Hint
The command line arguments interpreted by the script can be accessed via $1 (first argument) and $2 (second argument).

Take a screenshot of the code above and save it as 01-Set_Variables.jpg or .png.

### Task 2
Display the values of the two command line arguments in the terminal.
Click here for Hint
Remember, you can use the command echo as a print command.

Example: echo "The year is $year"
Take a screenshot of the code above and save it as 02-Display_Values.jpg or .png.
### Task 3
Define a variable called currentTS as the current timestamp, expressed in seconds.
Click here for Hint
Remember you can customize the output format of the date command.

To set a variable equal to the output of a command you can use command substitution: $() or ` `

For example: currentYear=$(date +%Y)
Take a screenshot of the code above and save it as 03-CurrentTS.jpg or .png.
### Task 4
Define a variable called backupFileName to store the name of the archived and compressed backup file that the script will create.
The variable backupFileName should have the value "backup-[$currentTS].tar.gz"

For example, if currentTS has the value 1634571345, then backupFileName should have the value backup-1634571345.tar.gz.
Take a screenshot of the code above and save it as 04-Set_Value.jpg or .png.
### Task 5
Define a variable called origAbsPath with the absolute path of the current directory as the variable's value.
Click here for Hint
You can get the absolute path of the current directory using the pwd command.

Take a screenshot of the code above and save it as 05-Define_Variable.jpg or .png.
### Task 6
Define a variable called destAbsPath whose value equals the absolute path of the destination directory.
Click here for Hint
First use cd to go to destinationDirectory, then use the same method you used in Task 5.

Note: Please Note that you can also use the cd “destinationDirectory” || exit which ensures that if the specified directory is incorrect or inaccessible, the script will terminate immediately at this step. This acts as an implicit validation check to confirm that the correct directory is provided before proceeding with further operations. Follow the same for Task 7 .

Take a screenshot of the code above and save it as 06-Define_Variable.jpg or .png.



### Task 7
Change directories from the current working directory to the target directory targetDirectory.
Click here for Hint
cd into the original directory origAbsPath and then cd into targetDirectory.

Take a screenshot of the code above and save it as 07-Change_Directory.jpg or .png.


### Task 8
You need to find files that have been updated within the past 24 hours. This means you need to find all files whose last-modified date was 24 hours ago or less.

To do make this easier:

Define a numerical variable called yesterdayTS as the timestamp (in seconds) 24 hours prior to the current timestamp, currentTS.
Click here for Hint
Math can be done using $(()), for example:

``` bash
zero=$((3 * 5 - 6 - 9))
```
Thus, to get the timestamp in seconds of 24 hours in the future, you would use:

``` bash
tomorrowTS=$(($currentTS + 24 * 60 * 60))
```

Take a screenshot of the code above and save it as 08-YesterdayTS.jpg or .png.

### Note on arrays
In the script, you will notice the line:


``` bash
declare -a toBackup
```

This line declares a variable called toBackup, which is an array. An array contains a list of values, and you can append items to arrays using the following syntax:

``` bash
myArray+=($myVariable)
```

When you print or echo an array, you will see its string representation, which is simply all of its values separated by spaces:

``` bash
$ declare -a myArray
$ myArray+=("Linux")
$ myArray+=("is")
$ myArray+=("cool!")
$ echo ${myArray[@]}
Linux is cool!
```

This will be useful later in the script where you will pass the array $toBackup, consisting of the names of all files that need to be backed up, to the tar command. This will archive all files at once!


### Task 9
In the for loop, use the wildcard to iterate over all files and directories in the current folder.
The asterisk * is a wildcard that matches every file and directory in the present working directory.
Take a screenshot of the code above and save it as 09-List_AllFilesandDirectoriess.jpg or .png.


### Task 10
Inside the for loop, you want to check whether the $file was modified within the last 24 hours.
To get the last-modified date of a file in seconds, use date -r $file +%s then compare the value to yesterdayTS.

```  bash
if [[ $file_last_modified_date -gt $yesterdayTS ]] 
```

then the file was updated within the last 24 hours!

Since much of this wasn't covered in the course, for this task you may copy the code below and paste it into the double square brackets [[]]:

```  bash
`date -r $file +%s` -gt $yesterdayTS
```

Take a screenshot of the code above and save it as 10-IF_Statement.jpg or .png.

### Task 11
In the if-then statement, add the $file that was updated in the past 24-hours to the toBackup array.
Since much of this wasn’t covered in the course, you may copy the code below and place after the then statement for this task:
```  bash
toBackup+=($file)
```
Take a screenshot of the code above and save it as 11-Add_File.jpg or .png.

### Task 12
After the for loop, compress and archive the files, using the $toBackup array of filenames, to a file with the name backupFileName.
Use ```tar -czvf $backupFileName ${toBackup[@]}```.
Take a screenshot of the code above and save it as 12-Create_Backup.jpg or .png.

## Task 13
Now the file ```$backupFileName``` is created in the current working directory.

Move the file backupFileName to the destination directory located at destAbsPath
Take a screenshot of the code above and save it as 13-Move_Backup.jpg or .png.


### Task 16
Download the following .zip file with the wget command:

```wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/Final%20Project/important-documents.zip```

Unzip the archive file:

```unzip -DDo important-documents.zip```

Note: -DDo overwrites without restoring original modified date.

Update the file’s last-modified date to now:

```touch important-documents/*```

Test your script using the following command:

```./backup.sh important-documents .```

This should have created a file called ```backup-[CURRENT_TIMESTAMP].tar.gz``` in your current directory.

Take a screenshot of the output of ```ls -l``` and save it as 16-backup-complete.jpg or .png.


### Task 17
Copy the backup.sh script into the /usr/local/bin/ directory. (Do not use mv.)
Note: You may need to use sudo cp in order to create a file in /usr/local/bin/.

Test the cronjob to see if the backup script is getting triggered by scheduling it for every 1 minute.
Click here for Hint

```*/1 * * * * /usr/local/bin/backup.sh /home/project/important-documents /home/project```


Please note that since the Theia Lab is a virtual environment, we need to explicitly start the cron service using the below command:

```sudo service cron start```


Once the cron service is started, check in the directory /home/project to see if the .tar files are being created.

If they are, then stop the cron service using the below command, otherwise it will continue to create .tar files every minute:


```sudo service cron stop```

edule your /usr/local/bin/backup.sh script to backup the important-documents folder every 24 hours to the directory /home/project.

Take a screenshot of the output of ```crontab -l``` and save as 17-crontab.jpg or .png.




