# create_pay_slip.py
from fpdf import FPDF

##  การสร้างฟังชั่นสำหรับการออกแบบหน้าตาของ Slip
def generate_pdf(output_path, name, month_year, salary, net_pay, ot_normal=0, ot_holiday=0):
    pdf = FPDF()
    pdf.add_page()
    
    # --- กำหนดค่าสี (Color Palette) ---
    charcoal = (42, 40, 42)      # เทาเข้ม 
    blossom_pink = (233, 184, 215) # ชมพูพาสเทล 
    bg_pink = (252, 245, 250)    # ชมพู
    
    
    
    # วาดแถบพื้นหลังยาวด้านบนสีเทาเข้ม
    pdf.set_fill_color(*charcoal)
    pdf.rect(0, 0, 210, 40, 'F')
    
    # ชื่อบริษัท (สีชมพูบนพื้นเทา)
    pdf.set_font("Helvetica", 'B', 26)
    pdf.set_text_color(*blossom_pink)
    pdf.set_y(12)
    pdf.cell(0, 12, txt="LAE THAE 99 CO., LTD.", align='C', ln=1)
    
    # ที่อยู่และสโลแกน (ตัวอักษรขาวจางๆ)
    pdf.set_font("Helvetica", 'I', 9)
    pdf.set_text_color(200, 200, 200)
    pdf.cell(0, 5, txt="Address: 98/28 Chan City Place, Muang Ake 12000", align='C', ln=1)
    
    pdf.set_y(45) # ขยับลงมาส่วนเนื้อหา
    
    # แถบชื่อประเภทเอกสาร
    pdf.set_font("Helvetica", 'B', 16)
    pdf.set_text_color(*charcoal)
    pdf.cell(0, 10, txt="PAY ADVICE", align='L', ln=1)
    pdf.set_draw_color(*blossom_pink)
    pdf.set_line_width(1)
    pdf.line(10, 55, 70, 55) # ขีดเส้นใต้เน้น
    
    pdf.ln(8)


    # 2. ข้อมูลพนักงาน (Employee Card)
    # ==========================================
    pdf.set_fill_color(*bg_pink)
    pdf.rect(10, 62, 190, 25, 'F') # วาดกรอบพื้นหลังให้ข้อมูลส่วนตัว
    
    pdf.set_y(65)
    pdf.set_font("Helvetica", 'B', 11)
    pdf.set_text_color(*charcoal)
    pdf.cell(30, 8, txt="  NAME:", ln=0)
    pdf.set_font("Helvetica", '', 11)
    pdf.cell(90, 8, txt=f"{name.upper()}", ln=0)
    
    pdf.set_font("Helvetica", 'B', 11)
    pdf.cell(20, 8, txt="PERIOD:", ln=0)
    pdf.set_font("Helvetica", '', 11)
    pdf.cell(0, 8, txt=f"{month_year.upper()}", ln=1)
    
    
    pdf.ln(10)


    # 3. ตารางสรุปรายได้ (Financial Summary)
    # ==========================================
    # หัวตาราง
    pdf.set_font("Helvetica", 'B', 12)
    pdf.set_fill_color(*charcoal)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(130, 12, txt="DESCRIPTION", border=0, fill=True, align='C')
    pdf.cell(60, 12, txt="AMOUNT (THB)", border=0, fill=True, align='C', ln=1)
    
    # รายการเงินเดือน
    pdf.set_font("Helvetica", '', 12)
    pdf.set_text_color(*charcoal)
    pdf.set_draw_color(*blossom_pink) # เส้นขอบสีชมพู
    pdf.cell(130, 12, txt="  Basic Monthly Salary", border='B')
    pdf.cell(60, 12, txt=f"{float(salary):,.2f}", border='B', align='R', ln=1)
    
    # รายการ OT (คำนวณจากส่วนต่าง)
    ot_total = float(net_pay) - float(salary)
    pdf.cell(130, 12, txt="  Overtime & Allowances (OT)", border='B')
    pdf.cell(60, 12, txt=f"{ot_total:,.2f}", border='B', align='R', ln=1)
    
    pdf.ln(5)

    # ==========================================
    # 4. ยอดสุทธิ (The Grand Total) - ไฮไลท์เริ่ดๆ
    # ==========================================
    pdf.set_font("Helvetica", 'B', 15)
    pdf.set_fill_color(*blossom_pink)
    pdf.set_text_color(*charcoal)
    # วาดกรอบยอดเน้นๆ
    pdf.cell(120, 15, txt="NET REMITTANCE TOTAL", border=0, fill=True, align='R')
    pdf.set_font("Helvetica", 'B', 18)
    pdf.cell(70, 15, txt=f"{float(net_pay):,.2f} ", border=0, fill=True, align='R', ln=1)

    # ==========================================
    # Footer
    # ==========================================
    pdf.set_y(-40)
    pdf.set_font("Helvetica", 'I', 8)
    pdf.set_text_color(160, 160, 160)
    pdf.cell(0, 5, txt="This document is an official payroll notification and is strictly confidential.", align='C', ln=1)
    pdf.cell(0, 5, txt="Processed by RPA Delivery System | Lae Thae 99 Co., Ltd.", align='C', ln=1)

    pdf.output(output_path)