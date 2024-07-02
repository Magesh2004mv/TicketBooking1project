import smtplib
import datetime
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="ticket_booking_project"    
)
mycursor=mydb.cursor()
def ticket_data():
    sql="insert into ticket_data_report(name,movie,seat,totalamount,paid) values (%s,%s,%s,%s,%s)"
    print("leo--->190")
    print('vikram---->180')
    print("kaithi----->150")
    def ticket():
        try:
            leo=190
            vikram=180
            kaithi=150
            name1=input("enter the name:")
            movie1=input("enter the movie:")
            if movie1=="leo":
                print("yes available")
                seat1=int(input("if you want howmany seat:"))
                gst1=18
                total=leo*gst1/100
                totalamount1=leo+total
                totalamount2=totalamount1*seat1
                print(totalamount2)
                name=name1
                movie=movie1
                seat=seat1
                totalamount=totalamount2
                paid="paid successfully"
                val=(name,movie,seat,totalamount,paid)
                sender1=(f"\nname:{name}\nmovie:{movie}\nseat:{seat}\ntotalamount:{totalamount}\npaid:{paid}")
                mycursor.execute(sql,val)
                mydb.commit()
                print("data successfully")
                dt=datetime.datetime.now()
                bill=open("ticker_bill.txt","w")
                bill.write(f"moviename:{movie}\ntotalamount is {totalamount}\ndatetime-->{dt}\npaid:{paid}")
                def send_ticketbook(email):
                    ticketbook = sender1
                    print(f"Generated ticketbooking: {ticketbook}")
                    try: 
                        s = smtplib.SMTP("smtp.gmail.com", 587)
                        s.starttls()
                        s.login("---#your emailid---", "#---use your app password---")
                        subject = "Ticket Booking"
                        body = f"Your ticket booking is {ticketbook}"
                        message = f"Subject: {subject}\n\n{body}"
                        s.sendmail("---your mailid---", email, message)
                        s.quit()
                        print("Email has been successfully sent!")
                    except Exception as e:
                        print(f"Failed to send email: {e}")
                mail = input('Enter your email ID: ')
                send_ticketbook(mail)
            elif movie1=="vikram":
                print("yes available")
                seat2=int(input("if you want howmany seat:"))
                gst1=18
                total=vikram*gst1/100
                totalamount3=vikram+total
                totalamount4=totalamount3*seat2
                print(totalamount4)
                name=name1
                movie=movie1
                seat=seat2
                totalamount=totalamount4
                paid="paid successfully"
                val=(name,movie,seat,totalamount,paid)
                sender2=(f"\nname:{name}\nmovie:{movie}\nseat:{seat}\ntotalamount:{totalamount},paid:{paid}")
                mycursor.execute(sql,val)
                mydb.commit()
                print("data successfully")
                dt=datetime.datetime.now()
                bill=open("ticker_bill.txt","w")
                bill.write(f"moviename:{movie}\ntotalamount is {totalamount}\ndatetime-->{dt}\npaid:{paid}")
                def send_ticketbook(email):
                    ticketbook = sender2
                    print(f"Generated ticketbooking: {ticketbook}")
                    try: 
                        s = smtplib.SMTP("smtp.gmail.com", 587)
                        s.starttls()
                        s.login("---#your emailid---", "#---use your app password---")
                        subject = "Ticket Booking"
                        body = f"Your ticket booking is {ticketbook}"
                        message = f"Subject: {subject}\n\n{body}"
                        s.sendmail("---your mailid---", email, message)
                        s.quit()
                        print("Email has been successfully sent!")
                    except Exception as e:
                        print(f"Failed to send email: {e}")
                mail = input('Enter your email ID: ')
                send_ticketbook(mail)
            elif movie1=="kaithi":
                print("yes available")
                seat3=int(input("if you want howmany seat:"))
                gst1=18
                total=kaithi*gst1/100
                totalamount5=kaithi+total
                totalamount6=totalamount5*seat3
                print(totalamount6)
                name=name1
                movie=movie1
                seat=seat3
                totalamount=totalamount6
                paid="paid successfully"
                val=(name,movie,seat,totalamount,paid)
                sender3=(f"\nname:{name}\nmovie:{movie}\nseat:{seat}\ntotalamount:{totalamount}\npaid:{paid}")
                mycursor.execute(sql,val)
                mydb.commit()
                print("data successfully")
                dt=datetime.datetime.now()
                bill=open("ticker_bill.txt","w")
                bill.write(f"moviename:{movie}\ntotalamount is {totalamount}\ndatetime-->{dt}\npaid:{paid}")
                def send_ticketbook(email):
                    mailid = sender3
                    print(f"Generated mailid: {mailid}")
                    try:
                       s = smtplib.SMTP("smtp.gmail.com", 587)
                       s.starttls()
                       s.login("---#your emailid---", "#---use your app password---")
                       subject = "Ticket Booking"
                       body = f"Your ticket booking is {mailid}"
                       message = f"Subject: {subject}\n\n{body}"
                       s.sendmail("---your mailid---", email, message)
                       s.quit()
                       print("Email has been successfully sent")
                    except Exception as e:
                       print(f"Failed to send email: {e}")
                mail = input('Enter your email ID: ')
                send_ticketbook(mail)
            else:
                print("plese enter are leo,vikram,kaithi movie only")
        except NameError:
            print("plese enter the name only")
        except IndexError:
            print("plese check in number index only")   
    ticket()                     
ticket_data()
