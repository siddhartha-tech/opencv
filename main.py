import os
import io
from PIL import Image
import pytesseract
from wand.image import Image as wi
import gc
import xlwt
from xlwt import Workbook
# pdf=wi(filename='Files/EC030BIL6000327_Invoice.pdf',resolution=res)
# pdfImg=pdf.convert('jpeg')
# print(pdfImg)

imgBlobs=[]
extracted_text=[]

def Get_text_from_image(pdf_path, res):
    pdf=wi(filename=pdf_path,resolution=res)
    pdfImg=pdf.convert('jpeg')
    imgBlobs=[]
    extracted_text=[]
    for img in pdfImg.sequence:
        page=wi(image=img)
        imgBlobs.append(page.make_blob('jpeg'))

    for imgBlob in imgBlobs:
        im=Image.open(io.BytesIO(imgBlob))
        text=pytesseract.image_to_string(im,lang='eng')
        extracted_text.append(text)

    return (extracted_text)

def convert(s):
    new = ""
    for x in s:
        new += x

    return new

pdf1 = Get_text_from_image('Files/EC030BIL6000327_Invoice.pdf',315)
str_text = convert(pdf1)
# # print(str_text)
a = str_text.find("Vendor Code")
ven_code = str_text[a+13:a+22]
# print(ven_code)

b = str_text.find("Tatal Amount")
if b == -1:
    b = str_text.find("Total Amount")
tot_amount = str_text[b+13:b+28]
# print(tot_amount)

pdf2 = Get_text_from_image('Files/EC030BIL6000400_EIP-BILL-Annexure.pdf',600)
str_text1 = convert(pdf2)
# print(str_text)
c = str_text1.find("Vendor Code")
vend_code = str_text1[c+14:c+23]
# print(vend_code)

d = str_text1.find("Tatal Amount")
if d == -1:
    d = str_text1.find("Total Amount")
tota_amount = str_text1[d+13:d+28]
# print(tota_amount)

pdf3 = Get_text_from_image('Files/EC030BIL6000400_EIP Bill Summary.pdf',700)
str_text2 = convert(pdf3)
# print(str_text2)

e = str_text2.find("Job Code")
if e == -1:
    e = str_text2.find("Job Address")
job_code = str_text2[e+14:e+22]
# print(job_code)

f = str_text2.find("Vendor Code")
if f == -1:
    f = str_text2.find("Vendor Address")
vendor_code = str_text2[f+17:f+25]
# print(vendor_code)

g = str_text2.find("WO No")
wo_no = str_text2[g+7:g+22]
# print(wo_no)

h = str_text2.find("Dt")
wo_dt = str_text2[h+4:h+15]
# print(wo_dt)

i = str_text2.find("Bill No")
if i == -1:
    i = str_text2.find("Running Bill No")
bill_no = str_text2[i+9:i+10]
# print(bill_no)

bill_date = str_text2[i+16:i+27]
# print(bill_date)

j = str_text2.find("Bill From")
bill_from = str_text2[j+12:j+23]
# print(bill_from)

bill_to = str_text2[j+29:j+40]
# print(bill_to)

# k = str_text2.find("To") #**
# bill_to = str_text2[k:k+23]

l = str_text2.find("Total as per Enclosed Annexure") #**
previou_bill = str_text2[l+31: l+61].split(' ')[0]
# print(previou_bill)

m = str_text2.find("This Bill Amount") #**
bill_amount = str_text2[l+31: l+61].split(' ')[1]
# print(bill_amount)

n = str_text2.find("Total Amount") #**
total_amount = str_text2[l+31: l+61].split(' ')[2]
# print(total_amount)

o = str_text2.find("Balance")
balance = str_text2[o+8:o+17]
# print(balance)

p = str_text2.find("Total Deduction")
total_deduction = str_text2[p+16:p+40]
# print(total_deduction)

q = str_text2.find("Paid Upto Last Bill")
last_bill = str_text2[q+22:q+32]
# print(last_bill)

r = str_text2.find("This Bill Paid")
bill_paid = str_text2[r+17:r+21]
# print(bill_paid)

s = str_text2.find("Amount Payable")
amount_payable = str_text2[s+19:s+32]
# print(amount_payable)

# Workbook is created
# wb = Workbook()

# # add_sheet is used to create sheet.
# sheet1 = wb.add_sheet('Sheet 1')

# # sheet1.write(0, 0, 'Vendor code')
# # sheet1.write(0, 1, ven_code)
# # sheet1.write(1, 0, 'Total Amount')
# # sheet1.write(1, 1, tot_amount)
# # sheet1.write(2, 0, 'Vendor Code')
# # sheet1.write(2, 1, vend_code )
# sheet1.write(3, 0, 'Total Amount')
# sheet1.write(3, 1, tota_amount )
# sheet1.write(0, 0, 'Job Code')
# sheet1.write(0, 1, job_code )
# sheet1.write(1, 0, 'Vendor Code')
# sheet1.write(1, 1, vendor_code )
# sheet1.write(2, 0, 'WO No')
# sheet1.write(2, 1, wo_no )
# sheet1.write(3, 0, 'WO Dt')
# sheet1.write(3, 1, wo_dt)
# sheet1.write(4, 0, 'Bill No')
# sheet1.write(4, 1, bill_no)
# sheet1.write(5, 0, 'Bill Date')
# sheet1.write(5, 1, bill_date)
# sheet1.write(6, 0, 'Bill From')
# sheet1.write(6, 1, bill_from)
# sheet1.write(7, 0, 'Bill To')
# sheet1.write(7, 1, bill_to)
# sheet1.write(8, 0, 'Upto Previous Bill Amount')
# sheet1.write(8, 1, previou_bill)
# sheet1.write(9, 0, 'This Bill Amount')
# sheet1.write(9, 1, bill_amount)
# sheet1.write(10, 0, 'Total Amount')
# sheet1.write(10, 1, total_amount)
# sheet1.write(11, 0, 'Total Deduction')
# sheet1.write(11, 1, total_deduction)
# sheet1.write(12, 0, 'Balance')
# sheet1.write(12, 1, balance)
# sheet1.write(13, 0, 'Paid upto Last Bill')
# sheet1.write(13, 1, last_bill)
# sheet1.write(14, 0, 'This Bill Paid')
# sheet1.write(14, 1, bill_paid)
# sheet1.write(15, 0, 'Amount Payable')
# sheet1.write(15, 1, amount_payable)

# wb.save('L&T pdf_1.xls')

# wb2 = Workbook()
# sheet2 = wb2.add_sheet('Sheet 2')

# sheet2.write(0, 0, 'Vendor code')
# sheet2.write(0, 1, ven_code)
# sheet2.write(1, 0, 'Total Amount')
# sheet2.write(1, 1, tot_amount)

# wb2.save('L&T pdf_2.xls')

# wb3 = Workbook()
# sheet3 = wb3.add_sheet('Sheet 3')

# sheet3.write(0, 0, 'Vendor code')
# sheet3.write(0, 1, vend_code)
# sheet3.write(1, 0, 'Total Amount')
# sheet3.write(1, 1, tota_amount)

# wb3.save('L&T pdf_3.xls')

import re
xx = str_text2
# print(xx)
r1 = re.findall(r"(\-[a-z][a-z]*)*",xx)
print(r1)