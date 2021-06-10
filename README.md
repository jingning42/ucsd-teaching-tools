# Oral Exam Grading Report Script

This is a tutorial is for the MAE30B instructor and TAs.  

It has two part, 

1. Generate the grading report using python script
2. Upload the grading reports on Gradescope



## Part 1. Generate grading report

Below is the instruction for generating oral exam grading reports using the python script in this repo. You will need to install some required libraries to run this script. Check the **prerequisite** section.

### Steps

1. Download oral exam grading sheet as a `csv` file
2. Clean up data and delete the information which you don't want students to see. Your csv file should have the same format as the `sample_grading_sheet.csv`  after cleaning up.
3. Open `oral_exam_report.py`, modify the `grading_file`, `target_path` and `title` of the report as you need
4. Run python script by `python3 oral_exam_report_generator.py` 

### Prerequisite

You need to download these libraries to run the python script

`pip3 install reportlab`



## Part 2. Upload reports on Gradescope

Below is the instruction for uploading the grading reports pdf on Gradescope. Gradescope will automatically scan and assign these reports to corresponding students. Student can only see their own report.

### Steps

1. Create an assignment on Gradescope, like 'Oral Exam 1 Grading Report'
2. Choose Instructor in 'Who will upload submissions' setting
3. Upload the template pdf file  `Template.pdf`
4. Edit Outline: carefully choose the `Name Region` and `ID Region`
5. Manage Scans: Select PDF Files -> choose the grading reports pdf you just generated
6. Manage Submission: Check if the automatic scanning is successful
7. Send out emails to student and ask them to check their grading report on Gradscope

