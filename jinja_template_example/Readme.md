### How to run this script: 

1. Make sure you have the following files on your machine:
   a. compare_ilo_ahs.py
   b. AHS_Data.json  
   c. iLO_data.json
   d. template.j2

2. To run the script, I assume all the above mentioned files are in the same directory. However, you can pass the full path names to the file also.
   python compare_ilo_ahs.py AHS_Data.json iLO_data.json
    
   OR 

   Make the compare_ilo_ahs.py execuatble with chmod +x and run the below command: 
   ./compare_ilo_ahs.py AHS_Data.json iLO_data.json       

3. If you run the script will less number of arguments, it will print the usage and exits. For handling file not found errors, I have manged to place some exceptional handlers. 
   ravitezu@Lenevo:~/chiru$ python compare_ilo_ahs.py AHS_Data.json 
   Usage:
        This script accepts two files as arguments to compare and prints out the results in html format.
        compare_ilo_ahs.py path_to_file1 path_to_file2 
   
   ravitezu@Lenevo:~/chiru$ python compare_ilo_ahs.py AHS_Data.json unknown_file
   Oh Boy, Something went really wrong in loading the files: [Errno 2] No such file or directory: 'unknown_file'

4. As the assignment mentions, try to be generic on the logic, I have't hardcoded anything in the script. So, If you want to chage the script, feel free to change it as you want. 

5. Running this script, will generates a index.html file. 

Hope this helps you. Have fun. 
