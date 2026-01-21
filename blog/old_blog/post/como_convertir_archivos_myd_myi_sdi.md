---
title: "Restaurar la base de datos MySQL desde archivos .myd .myi .sdi"
date: 2024-09-27T14:15:01-03:00
tags: ['sql']
---

https://stackoverflow.com/questions/879176/how-to-recover-mysql-database-from-myd-myi-frm-files


¡Simple! Cree una base de datos ficticia (digamos abc)

Copie todos estos archivos .myd, .myi, .frm a var mysql\data\abc donde mysql\data\ es el lugar donde se almacenan .myd, .myi, .frm para todas las bases de datos.


---

I found a solution for converting the files to a .sql file (you can then import the .sql file to a server and recover the database), without needing to access the /var directory, therefore you do not need to be a server admin to do this either.

It does require XAMPP or MAMP installed on your computer.

After you have installed XAMPP, navigate to the install directory (Usually C:\XAMPP), and the the sub-directory mysql\data. The full path should be C:\XAMPP\mysql\data
Inside you will see folders of any other databases you have created. Copy & Paste the folder full of .myd, .myi and .frm files into there. The path to that folder should be

C:\XAMPP\mysql\data\foldername\.mydfiles

**(O podés usar mysql_dump)**   
`/usr/bin/mysqldump -u root --password=root DATABASE > backup.sql`

Then visit localhost/phpmyadmin in a browser. Select the database you have just pasted into the mysql\data folder, and click on Export in the navigation bar. Chooses the export it as a .sql file. It will then pop up asking where the save the file

And that is it! You (should) now have a .sql file containing the database that was originally .myd, .myi and .frm files. You can then import it to another server through phpMyAdmin by creating a new database and pressing 'Import' in the navigation bar, then following the steps to import it


