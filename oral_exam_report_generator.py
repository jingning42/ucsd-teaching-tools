from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph
from reportlab.lib.units import inch, cm
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
import csv
import os


######################### general setting ##################################

grading_file = "sample_grading_sheet.csv"          # name of the grading sheet file
target_path = "output_file"             # the name of the folder to store the pdf files
# create the folder
if not os.path.exists(target_path):
    os.mkdir(target_path)               


######################## PDF general setting ###############################

def print_pdf(filename, row, template=False):
    path = os.path.join(target_path, "%s.pdf"%filename)
    pagesize = (8.5 * inch, 11 * inch)   # set the page size as latter-sized
    my_doc = SimpleDocTemplate(path, pagesize=pagesize)
    flowables = []
    sample_style_sheet = getSampleStyleSheet()

    custom_body_style = sample_style_sheet['BodyText']
    custom_body_style.fontName = 'Times-Roman'
    custom_body_style.fontSize = 14
    custom_body_style.spaceBefore = 20
    custom_body_style.leading = 20

    # write content
    title = Paragraph("[SP21 MAE30B] Midterm 1 Oral Exam Grading Report", sample_style_sheet['Heading1'])
    flowables.append(title)
    
    keys = list(row.keys())
    if template == True:
        for i in range(len(keys)):
            paragraph = Paragraph(f"{keys[i]}: ", sample_style_sheet['BodyText'])
            flowables.append(paragraph)
    else:
        for i in range(len(keys)):
            paragraph = Paragraph(f"{keys[i]}: {row[keys[i]]}", sample_style_sheet['BodyText'])
            flowables.append(paragraph)
    
    my_doc.build(flowables)

######################## read infomation from csv file ####################

with open(grading_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        print_pdf(row['PID'], row)

    print_pdf("Template", row, template=True) # print template pdf file




