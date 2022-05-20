<h2> <a href="https://github.com/ShubhPatil95/DVC-04-Simple_Project"> 04-Simple_DVC_Project </a></h2>

<p>
<strong> Here in this tutorial we will see how we can use DVC to track the respective code and data </strong>
<h4>Challanges without DVC and how DVC is solving them</h4>
1. How DVC is helping to track the large dataset which cannot be pushed to git ? => DVC will push that data to remote data storage(S3 bucket,Google Drive)<br>
2. How can we remember that which dataset was used for particuler experiment? => Git will track the code for each experiment and DVC will track dataset used for each respective experiment.<br>
 
<h3> Assume we are trying to predict the marks of student by analyzing how much hours that student is studying. Lets take below 3 scenarios for 3 different schools </h3>
School-1: There are 10 student and there data is as below. <br>
School-2: There are 10 student same as school-1, however students who are studying 1 and 2 hours are Absent in exam. <br>
School-3: There are 10 student same as school-1, however students who are studying 1 and 2 hours are getting 50 marks each. <br>
<img src="https://github.com/ShubhPatil95/Raw_Data_Storage/blob/main/DVC-04-Simple_Project_Schools.png" alt="Data Of 3 School">

<strong> Let try to build a model for above all 3 datas </strong><br>
<strong> First of all create new conda environment and install DVC by refering [DVC-01-Installation](https://github.com/ShubhPatil95/DVC-01-Installation)<strong><br>


### Step1
* Create a folders under name DVC-04-Simple_Project DVC_Remote. Further create a code.py and data.csv files inside of DVC-04-Simple_Project
```ruby
mkdir DVC-04-Simple_Project DVC_Remote DVC_Clone
cd DVC-04-Simple_Project
touch code.py data.csv
```
### Step2
* Initiate the Git and DVC
```ruby
git init
dvc init
```  
### Step3
* Create a github repository under name DVC-04-Simple_Project. Add remote storage for DVC and Git.
```ruby
dvc remote add -d My_Local_Remote /home/shubham/DVC_Remote
git remote add origin https://github.com/ShubhPatil95/DVC-04-Simple_Project.git
```

### Step4  
* Lets work on School-1 data, copy and paste containt of code.py and data.csv from here [code.py](https://github.com/ShubhPatil95/DVC-04-Simple_Project/blob/220e6405c49d091e68635604f60330864c1b5f62/code.py) and [data.csv](https://raw.githubusercontent.com/ShubhPatil95/Raw_Data_Storage/main/data_school-1.csv)

### Step5
* Lets run a code.py and check the r_square.
* In case pandas and scikit learn not installed then you can pip install them
```ruby
python3 code.py  ## r_square = 1
```   
### Step6
* Add data.csv file to DVC and rest files to git
```ruby
dvc add data.csv
git add .
git commit -m "School-1_First_Commit_r_sqaure=1"
```  
 
### Step7
* Lets push the data.csv to remote storage My_Local_Remote and code.py to github repository.
* So now you have data.csv in DVC remote and code.py in git repository for School-1
```ruby
dvc push
git branch -M main
git push -u origin main
```
 
### Step8
* Now lets work on School-2 dataset and repeate the steps 3, 4, 5 and 7<br>
* Step3: Replace content of code.py and data.csv with containt from [code.py](https://github.com/ShubhPatil95/DVC-04-Simple_Project/blob/4bcdc457b1e84cf6cb0e630b54a0efecd9b79844/code.py) and [data.csv](https://raw.githubusercontent.com/ShubhPatil95/Raw_Data_Storage/main/data_school-2.csv) <br>
* Step4: Run a code.py
  ```ruby
  python3 code.py  ## r_square = 0.20
  ```
* Step5: Add data to dvc and code to git<br>
     ```ruby
     dvc add data.csv
     git add . 
     git commit -m "School-2_Second_Commit_r_sqaure=0.20"
     ```
* Step6: Push data.csv to DVC and code.py to git <br>
     ```ruby
     dvc push 
     git push -u origin main 
     ```
### Step9
* Now lets work on School-3 dataset and repeate the steps 3, 4, 5 and 7 <br>
* Step3: Replace content of code.py and data.csv with containt from [code.py](https://github.com/ShubhPatil95/DVC-04-Simple_Project/blob/3045210cf52cb3cc7a3925327b15a2204fb41b49/code.py) and [data.csv](https://raw.githubusercontent.com/ShubhPatil95/Raw_Data_Storage/main/data_school-3.csv) <br>
* Step4: Run a code.py
  ```ruby
  python3 code.py  ## r_square = 0.99
  ```
* Step5: Add data to dvc and code to git <br>
    ```ruby
     dvc add data.csv
     git add . 
     git commit -m "School-3_Third_Commit_r_square=0.99"
    ```
* Step6: Push data.csv to DVC and code.py to git <br>
    ```ruby
    dvc push
    git push -u origin main
    ```

### Step10
* Your all experiments are done here. Now, Lets try to see how DVC is works. 
* Go back to folder DVC_Clone and clone the github repository 
```ruby
cd ../DVC_Clone
git clone https://github.com/ShubhPatil95/DVC-04-Simple_DVC_Project
cd DVC-04-Simple_DVC_Project
```  
### Step11
* You will see that there is no data.csv file, hence do DVC pull, which will pull data.csv of School-3
* Now run code.py and see if r_square is correct(should be 0.99)
```ruby
dvc pull
python3 code.py  ## r_square should be 0.99
```     
### Step12
* Now, Just go back to First commit, means School-1 experiment.
* Copy the commit id of School-1_First_Commit
```ruby
git log --oneline      ## copy the commit School-1_First_Commit, should be 220e640
git checkout 220e640   ## checkout to School-1_First_Commit, now you have code.py for School-1 experiment
dvc pull               ## This command will pull data.csv of School-1 from DVC remote location
```    
### Step13
* Run a code.py and see if value of r_square is same a we got it for School-1 Experiment
* Got to back to last commit, git checkout main
```ruby
python3 code.py    ## r_square should be 1
git checkout main  ## Your code.py is updated for School-3_Third_Commit
dvc pull        ## Your data.csv is also updated for School-3
```        
### Step14
* Now, Just go back to Second commit, means School-2 experiment.
* Copy the commit id of School-2_Second_Commit
```ruby
git log --oneline         ## copy the commit School-2_Second_Commit, mine is 4bcdc45
git checkout 4bcdc45     ## checkout to School-2_Second_Commit, now you have code.py for School-2 experiment
dvc pull                 ## This command will pull data.csv of School-2 from DVC remote location
```  
### Step15
* Run a code.py and see if value of r_square is same a we got it for School-2 Experiment
* Got to back to last commit, git checkout main
```ruby
python3 code.py    ## r_square should be 0.20
git checkout main  ## Your code.py is updated for School-2_Second_Commit
dvc pull        ## Your data.csv is also updated for School-2
```  
<strong> This is how we can track the data.csv with code.py for every experiment using DVC and git </strong>
</p>
</details> 
