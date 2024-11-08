import datetime

today = datetime.datetime.today()
thisd = int(today.day)
thism = int(today.month)
thisy = int(today.year)

print("โปรแกรมคำนวณอายุ ปีนักษัตร และราศี\n")
def cal() :
  def eday():
    global day
    day = int(input("กรอกวันเกิดของคุณ (1-31) : "))
    if day <= 0 or day > 31:
      print("-------------------------")
      print("ข้อมูลผิดพลาด กรุณาตรวจสอบข้อมูลอีกครั้ง\n")
      eday()
  eday()

  def emonth():
    global month
    month = int(input("กรอกเดือนเกิดของคุณ (1-12) : "))
    if month <= 0 or month > 12:
      print("-------------------------")
      print("ข้อมูลผิดพลาด กรุณาตรวจสอบข้อมูลอีกครั้ง\n")
      eday()
    elif month == 2 and day > 29:
      print("-------------------------")
      print("ข้อมูลผิดพลาด กรุณาตรวจสอบข้อมูลอีกครั้ง\n")
      eday()
    elif (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
      print("-------------------------")
      print("ข้อมูลผิดพลาด กรุณาตรวจสอบข้อมูลอีกครั้ง\n")
      eday()
  emonth()


  def eyear():
    global year
    year = int(input("กรอกปีเกิดของคุณ (พ.ศ.) : "))
    global byear
    byear = year - 543
    if byear <= 0 or byear > thisy:
      print("-------------------------")
      print("ข้อมูลผิดพลาด กรุณาตรวจสอบข้อมูลอีกครั้ง\n")
      eday()
    elif (byear % 4 != 0 and month == 2) and day > 28:
      print("-------------------------")
      print("ข้อมูลผิดพลาด กรุณาตรวจสอบข้อมูลอีกครั้ง\n")
      eday()
    elif byear==thisy and month>thism :
      print("-------------------------")
      print("ข้อมูลผิดพลาด กรุณาตรวจสอบข้อมูลอีกครั้ง\n")
      eday()
    elif byear==thisy and month<=thism and day>thisd :
      print("-------------------------")
      print("ข้อมูลผิดพลาด กรุณาตรวจสอบข้อมูลอีกครั้ง\n")
      eday()
  eyear()


  print("\nคุณเกิดวันที่", day, "เดือน", month, "ปีพ.ศ.", year, "( ค.ศ.", byear,
      ")")

  age_y = thisy - byear
  age_m = thism - month
  if age_m < 0:
    age_y = age_y - 1
    age_m = 12 + age_m

  print("อายุของคุณ คือ", age_y, "ปี", age_m, "เดือน")

  if year % 12 == 1:
    print("ปีนักษัตรของคุณ คือ ปีมะเมีย")
  elif year % 12 == 2:
    print("ปีนักษัตรของคุณ คือ ปีมะแม")
  elif year % 12 == 3:
    print("ปีนักษัตรของคุณ คือ ปีวอก")
  elif year % 12 == 4:
    print("ปีนักษัตรของคุณ คือ ปีระกา")
  elif year % 12 == 5:
    print("ปีนักษัตรของคุณ คือ ปีจอ")
  elif year % 12 == 6:
    print("ปีนักษัตรของคุณ คือ ปีกุน")
  elif year % 12 == 7:
    print("ปีนักษัตรของคุณ คือ ปีชวด")
  elif year % 12 == 8:
    print("ปีนักษัตรของคุณ คือ ปีฉลู")
  elif year % 12 == 9:
    print("ปีนักษัตรของคุณ คือ ปีขาล")
  elif year % 12 == 10:
    print("ปีนักษัตรของคุณ คือ ปีเถาะ")
  elif year % 12 == 11:
    print("ปีนักษัตรของคุณ คือ ปีมะโรง")
  else:
    print("ปีนักษัตรของคุณ คือ ปีมะเส็ง")

  if month == 1 and day >= 15:
    print("ราศี(แบบไทย)ของคุณ คือ ราศีมังกร")
  elif month == 2 and day <= 12:
    print("ราศี(แบบไทย)ของคุณ คือ ราศีมังกร")
  elif month == 2 and day >= 13:
    print("ราศี(แบบไทย)ของคุณ คือ ราศีกุมภ์")
  elif month == 3 and day <= 14:
    print("ราศี(แบบไทย)ของคุณ คือ ราศีกุมภ์")
  elif month == 3 and day >= 15:
    print("ราศี(แบบไทย)ของคุณ คือ ราศีมีน")
  elif month == 4 and day <= 12:
    print("ราศี(แบบไทย)ของคุณ คือ ราศีมีน")
  elif month == 4 and day >= 13:
    print("ราศี(แบบไทย)ของคุณ คือ ราศีเมษ")
  elif month == 5 and day <= 14:
    print("ราศี(แบบไทย)ของคุณ คือ ราศีเมษ")
  elif month == 5 and day >= 15:
    print("ราศี(แบบไทย)ของคุณ คือ ราศีพฤษก")
  elif month == 6 and day <= 14:
    print("ราศี(แบบไทย)ของคุณ คือ ราศีพฤษก")
  elif month == 6 and day >= 15:
    print("ราศี(แบบไทย)ของคุณ คือ ราศีเมถุน")
  elif month == 7 and day <= 15:
    print("ราศี(แบบไทย)ของคุณ คือ ราศีเมถุน")
  elif month == 7 and day >= 16:
    print("ราศี(แบบไทย)ของคุณ คือ ราศีกรกฎ")
  elif month == 8 and day <= 16:
    print("ราศี(แบบไทย)ของคุณ คือ ราศีกรกฎ")
  elif month == 8 and day >= 17:
    print("ราศี(แบบไทย)ของคุณ คือ ราศีสิงห์")
  elif month == 9 and day <= 16:
    print("ราศี(แบบไทย)ของคุณ คือ ราศีสิงห์")
  elif month == 9 and day >= 17:
    print("ราศี(แบบไทย)ของคุณ คือ ราศีกันย์")
  elif month == 10 and day <= 16:
    print("ราศี(แบบไทย)ของคุณ คือ ราศีกันย์")
  elif month == 10 and day >= 17:
    print("ราศี(แบบไทย)ของคุณ คือ ราศีตุลย์")
  elif month == 11 and day <= 15:
    print("ราศี(แบบไทย)ของคุณ คือ ราศีตุลย์")
  elif month == 11 and day >= 16:
    print("ราศี(แบบไทย)ของคุณ คือ ราศีพิจิก")
  elif month == 12 and day <= 15:
    print("ราศี(แบบไทย)ของคุณ คือ ราศีพิจิก")
  elif month == 12 and day >= 16:
    print("ราศี(แบบไทย)ของคุณ คือ ราศีธนู")
  else:
    print("ราศี(แบบไทย)ของคุณ คือ ราศีธนู")

  if month == 12 and day >= 22:
    print("ราศี(แบบตะวันตก)ของคุณ คือ ราศีมังกร")
  elif month == 1 and day <= 20:
    print("ราศี(แบบตะวันตก)ของคุณ คือ ราศีมังกร")
  elif month == 1 and day >= 21:
    print("ราศี(แบบตะวันตก)ของคุณ คือ ราศีกุมภ์")
  elif month == 2 and day <= 19:
    print("ราศี(แบบตะวันตก)ของคุณ คือ ราศีกุมภ์")
  elif month == 2 and day >= 20:
    print("ราศี(แบบตะวันตก)ของคุณ คือ ราศีมีน")
  elif month == 3 and day <= 20:
    print("ราศี(แบบตะวันตก)ของคุณ คือ ราศีมีน")
  elif month == 3 and day >= 21:
    print("ราศี(แบบตะวันตก)ของคุณ คือ ราศีเมษ")
  elif month == 4 and day <= 20:
    print("ราศี(แบบตะวันตก)ของคุณ คือ ราศีเมษ")
  elif month == 4 and day >= 21:
    print("ราศี(แบบตะวันตก)ของคุณ คือ ราศีพฤษก")
  elif month == 5 and day <= 20:
    print("ราศี(แบบตะวันตก)ของคุณ คือ ราศีพฤษก")
  elif month == 5 and day >= 21:
    print("ราศี(แบบตะวันตก)ของคุณ คือ ราศีเมถุน")
  elif month == 6 and day <= 21:
    print("ราศี(แบบตะวันตก)ของคุณ คือ ราศีเมถุน")
  elif month == 6 and day >= 22:
    print("ราศี(แบบตะวันตก)ของคุณ คือ ราศีกรกฎ")
  elif month == 7 and day <= 23:
    print("ราศี(แบบตะวันตก)ของคุณ คือ ราศีกรกฎ")
  elif month == 7 and day >= 24:
    print("ราศี(แบบตะวันตก)ของคุณ คือ ราศีสิงห์")
  elif month == 8 and day <= 23:
    print("ราศี(แบบตะวันตก)ของคุณ คือ ราศีสิงห์")
  elif month == 8 and day >= 24:
    print("ราศี(แบบตะวันตก)ของคุณ คือ ราศีกันย์")
  elif month == 9 and day <= 23:
    print("ราศี(แบบตะวันตก)ของคุณ คือ ราศีกันย์")
  elif month == 9 and day >= 24:
    print("ราศี(แบบตะวันตก)ของคุณ คือ ราศีตุลย์")
  elif month == 10 and day <= 23:
    print("ราศี(แบบตะวันตก)ของคุณ คือ ราศีตุำลย์")
  elif month == 10 and day >= 24:
    print("ราศี(แบบตะวันตก)ของคุณ คือ ราศีพิจิก")
  elif month == 11 and day <= 22:
    print("ราศี(แบบตะวันตก)ของคุณ คือ ราศีพิจิก")
  elif month == 11 and day >= 23:
    print("ราศี(แบบตะวันตก)ของคุณ คือ ราศีธนู")
  else:
    print("ราศี(แบบตะวันตก)ของคุณ คือ ราศีธนู")
  global x
  x=int(input("\nคำนวณอีกรอบ กด1 จบการคำนวณ กด0 : "))
cal()
while x>0 :
  x=x+0
  print("-------------------------")
  cal()
print("\nEnd")