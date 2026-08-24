from flask import Flask, render_template, flash, request, session, send_file
import pickle
import numpy as np
import mysql.connector
import sys

app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.route("/")
def homepage():
    return render_template('index.html')


@app.route("/Home")
def Home():
    return render_template('index.html')


@app.route("/ScanCenter")
def ScanCenter():
    return render_template('ScanCenter.html')


@app.route("/NewDoctor")
def NewDoctor():
    return render_template('NewDoctor.html')


@app.route("/DoctorLogin")
def DoctorLogin():
    return render_template('DoctorLogin.html')


@app.route("/UserLogin")
def UserLogin():
    return render_template('UserLogin.html')


@app.route("/NewUser")
def NewUser():
    return render_template('NewUser.html')


@app.route("/ScanCenterHome")
def ScanCenterHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb  ")
    data = cur.fetchall()
    return render_template('ScanCenterHome.html', data=data)


@app.route("/Report")
def Report():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
    cur = conn.cursor()
    cur.execute("SELECT UserName FROM doctortb  ")
    data = cur.fetchall()
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
    cur = conn.cursor()
    cur.execute("SELECT UserName FROM regtb  ")
    data1 = cur.fetchall()
    return render_template('Report.html', data=data, data1=data1)


@app.route("/breport", methods=['GET', 'POST'])
def breport():
    if request.method == 'POST':

        doc = request.form['doc']
        pat = request.form['pat']

        date = request.form['date']
        minfo = ''
        oinfo = ''
        file = request.files['file']
        import random
        fnew = random.randint(111, 999)
        savename = str(fnew) + file.filename
        file.save("static/upload/" + savename)

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM regtb where  username='" + pat + "'")
        data = cursor.fetchone()

        if data:
            uname = data[5]
            mobile = data[3]
            email = data[2]


        else:

            return 'Incorrect username / password !'

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO  drugtb VALUES ('','" + uname + "','" + mobile + "','" + email + "','" + doc + "','" +
            minfo + "','" + oinfo + "','','" + date + "','" + savename + "','')")
        conn.commit()
        conn.close()

        flash('Record Saved..!')

        return ADrugInfo()


@app.route("/sclogin", methods=['GET', 'POST'])
def sclogin():
    if request.method == 'POST':
        if request.form['uname'] == 'admin' and request.form['password'] == 'admin':

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb ")
            data = cur.fetchall()
            flash("Login successfully")
            return render_template('ScanCenterHome.html', data=data)

        else:
            flash("UserName Or Password Incorrect!")
            return render_template('ScanCenter.html')


@app.route("/DoctorInfo")
def DoctorInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
    cur = conn.cursor()
    cur.execute("SELECT * FROM doctortb  ")
    data = cur.fetchall()
    return render_template('DoctorInfo.html', data=data)


@app.route("/ADRemove")
def ADRemove():
    id = request.args.get('id')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
    cursor = conn.cursor()
    cursor.execute(
        "delete from doctortb where id='" + id + "'")
    conn.commit()
    conn.close()

    flash('Doctor  info Remove Successfully!')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
    cur = conn.cursor()
    cur.execute("SELECT * FROM doctortb  ")
    data = cur.fetchall()
    return render_template('DoctorInfo.html', data=data)


@app.route("/AURemove")
def AURemove():
    id = request.args.get('id')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
    cursor = conn.cursor()
    cursor.execute(
        "delete from regtb where id='" + id + "'")
    conn.commit()
    conn.close()

    flash('User  info Remove Successfully!')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb  ")
    data = cur.fetchall()
    return render_template('AdminHome.html', data=data)


@app.route("/ADrugInfo")
def ADrugInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  drugtb   ")
    data1 = cur.fetchall()
    return render_template('ADrugInfo.html', data1=data1)


@app.route("/newdoct", methods=['GET', 'POST'])
def newdoct():
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']

        email = request.form['email']

        address = request.form['address']
        specialist = request.form['Specialist']

        uname = request.form['uname']
        password = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO doctortb VALUES ('','" + name + "','" + email + "','" + mobile + "','" + address + "','" + specialist + "','" + uname + "','" + password + "')")
        conn.commit()
        conn.close()
        flash('Doctor  Register Successfully')
        return render_template('DoctorLogin.html')


@app.route("/doctlogin", methods=['GET', 'POST'])
def doctlogin():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['ename'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
        cursor = conn.cursor()
        cursor.execute("SELECT * from doctortb where username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:

            flash('Username or Password is wrong')
            return render_template('DoctorLogin.html', data=data)
        else:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
            cur = conn.cursor()
            cur.execute("SELECT * FROM doctortb where username='" + username + "' and Password='" + password + "'")
            data = cur.fetchall()
            flash("Login successfully")
            return render_template('DoctorHome.html', data=data)


@app.route("/DoctorHome")
def DoctorHome():
    username = session['ename']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM doctortb where username='" + username + "' ")
    data = cur.fetchall()
    return render_template('DoctorHome.html', data=data)


@app.route("/DAppoitmentInfo")
def DAppoitmentInfo():
    username = session['ename']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
    cur = conn.cursor()
    cur.execute("SELECT * FROM drugtb where DoctorName='" + username + "' ")
    data = cur.fetchall()

    return render_template('DAppoitmentInfo.html', data=data)


@app.route("/AssignDrug")
def AssignDrug():
    id = request.args.get('id')
    st = request.args.get('st')
    session['apid'] = id
    im = request.args.get('im')

    import cv2
    from ultralytics import YOLO

    image = cv2.imread('static/upload/' + im)
    # Load the YOLO model with pre-trained weights
    model = YOLO('runs/detect/xray/weights/best.pt')

    # Perform object detection with a confidence threshold of 0.2
    results = model(image, conf=0.2)

    # Extract predictions
    if results and results[0].boxes:
        # Get the class names
        class_labels = results[0].names

        # Get the confidence scores
        confidences = results[0].boxes.conf.cpu().numpy()  # Convert tensor to numpy array for easier handling

        # Find the highest confidence detection
        max_confidence_index = confidences.argmax()  # Index of the max confidence score
        predicted_class = class_labels[results[0].boxes.cls[max_confidence_index].item()]  # Get class label
        confidence_score = confidences[max_confidence_index]  # Get the confidence score

        # Print the results
        print(f"Predicted Class: {predicted_class}")
        print(f"Confidence Score: {confidence_score:.2f}")

        # Visualize the results
        annotated_frame = results[0].plot()

        cv2.imwrite("static/Out/alert.jpg", annotated_frame)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

        if predicted_class != '':
            out = predicted_class
            session['Ans'] = 'Yes'
            pre = predicted_class

            session['out'] = predicted_class

        annotated_frame = results[0].plot()
        cv2.imwrite("static/predict/" + im, annotated_frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        fname = 'static/upload/' + im
        noi = "static/Out/alert.jpg"
        return render_template('Answer.html', result=out, org=fname, noi=noi, pre=pre)
    else:
        print("No detections made")
        annotated_frame = image  # Display the original image if no detections are made

        cv2.imwrite("static/predict/" + im, annotated_frame)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

        out = 'No detections made'
        session['Ans'] = 'No'
        pre = 'No detections made'

        fname = 'static/upload/' + im
        noi = "static/Out/alert.jpg"
        return render_template('Answer.html', result=out, org=fname, noi=noi, pre=pre)


@app.route("/drugs", methods=['GET', 'POST'])
def drugs():
    if request.method == 'POST':

        date = request.form['date']
        minfo = request.form['minfo']
        oinfo = request.form['oinfo']
        file = request.files['file']
        file.save("static/upload/" + file.filename)

        idd = session['apid']

        dname = session['ename']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM drugtb where  id = '" + str(idd) + "'")
        data11 = cursor.fetchone()
        if data11:
            email = data11[3]
            sendmail(email, "Prediction Result  " + session['out'] + " Please Download Report..!")

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
        cursor = conn.cursor()
        cursor.execute(
            "update drugtb set Result='" + session[
                'out'] + "',	Medicine='" + minfo + "',	OtherInfo='" + oinfo + "',	Report='" + file.filename + "'	 where id='" + idd + "'")
        conn.commit()
        conn.close()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
        cur = conn.cursor()
        cur.execute("SELECT * FROM drugtb where DoctorName='" + dname + "' ")
        data = cur.fetchall()
        return render_template('DrugsInfo.html', data=data)


@app.route("/DrugsInfo")
def DrugsInfo():
    username = session['ename']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
    cur = conn.cursor()
    cur.execute("SELECT * FROM drugtb where DoctorName='" + username + "' ")
    data = cur.fetchall()
    return render_template('DrugsInfo.html', data=data)


@app.route('/download1')
def download1():
    id = request.args.get('id')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM drugtb where  id = '" + str(id) + "'")
    data = cursor.fetchone()
    if data:

        Result = data[10]
        if Result != "Nil":
            filename = "static\\upload\\" + data[7]

            return send_file(filename, as_attachment=True)
        else:
            flash('No Report Found..!')
            return UDrugsInfo()


@app.route('/Print')
def Print():
    id = request.args.get('id')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM drugtb where  id = '" + str(id) + "'")
    data11 = cursor.fetchone()
    if data11:
        SImage = data11[9]
        res = data11[10]

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
    cur = conn.cursor()
    cur.execute("SELECT * FROM drugtb where id='" + str(id) + "' ")
    data = cur.fetchall()

    org = "static/upload/" + SImage
    noi = "static/predict/" + SImage
    print(noi)
    return render_template('Print.html', data=data, result=res, org=org, noi=noi, pre=res)


@app.route('/download2')
def download2():
    id = request.args.get('id')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM drugtb where  id = '" + str(id) + "'")
    data = cursor.fetchone()
    if data:

        Result = data[10]
        if Result == "Fractured":
            filename = "static\\upload\\" + data[7]

            return send_file(filename, as_attachment=True)
        else:
            flash('No Report Found..!')
            return DrugsInfo()


@app.route('/download3')
def download3():
    id = request.args.get('id')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM drugtb where  id = '" + str(id) + "'")
    data = cursor.fetchone()
    if data:

        Result = data[10]
        if Result == "Fractured":
            filename = "static\\upload\\" + data[7]

            return send_file(filename, as_attachment=True)
        else:
            flash('No Report Found..!')
            return ADrugInfo()


@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']

        email = request.form['email']

        address = request.form['address']

        uname = request.form['uname']
        password = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO regtb VALUES ('','" + name + "','" + email + "','" + mobile + "','" + address + "','" + uname + "','" + password + "')")
        conn.commit()
        conn.close()
        flash('User Register successfully')

    return render_template('UserLogin.html')


@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:

            flash('Username or Password is wrong')
            return render_template('UserLogin.html')
        else:

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where username='" + username + "' and Password='" + password + "'")
            data = cur.fetchall()
            flash("Login successfully")

            return render_template('UserHome.html', data=data)


@app.route("/UserHome")
def UserHome():
    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM  regtb where username='" + uname + "'  ")
    data = cur.fetchall()
    return render_template('UserHome.html', data=data)


@app.route("/ViewDoctor", methods=['GET', 'POST'])
def ViewDoctor():
    if request.method == 'POST':
        ans = session['Ans']
        if ans == 'Yes':

            return render_template('DAssignDrug.html')

        else:
            flash('No fractured')
            idd = session['apid']

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
            cursor = conn.cursor()
            cursor.execute("SELECT  *  FROM drugtb where  id = '" + str(idd) + "'")
            data11 = cursor.fetchone()
            if data11:
                email = data11[3]
                sendmail(email, "Prediction Result  Not Fractured ")

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
            cursor = conn.cursor()
            cursor.execute(
                "update drugtb set Result='Nil',	Medicine='Nil',	OtherInfo='Nil',	Report='Nil'	 where id='" + idd + "'")
            conn.commit()
            conn.close()

            return DAppoitmentInfo()


@app.route("/Appointment")
def Appointment():
    dname = request.args.get('id')
    session['dname'] = dname
    return render_template('Appointment.html')


@app.route("/appointment", methods=['GET', 'POST'])
def appointment():
    if request.method == 'POST':
        dname = session['dname']
        uname = session['uname']
        date = request.form['date']
        info = request.form['info']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM regtb where  UserNAme='" + uname + "'")
        data = cursor.fetchone()

        if data:
            mobile = data[3]
            email = data[2]


        else:

            return 'Incorrect username / password !'

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO  apptb VALUES ('','" + uname + "','" + mobile + "','" + email + "','" + dname + "','" + date + "','" + info + "','waiting')")
        conn.commit()
        conn.close()

        uname = session['uname']
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
        cur = conn.cursor()
        cur.execute("SELECT * FROM  apptb where username='" + uname + "'  ")
        data = cur.fetchall()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
        cur = conn.cursor()
        cur.execute("SELECT * FROM  drugtb where username='" + uname + "'  ")
        data1 = cur.fetchall()
        return render_template('UDrugsInfo.html', data=data, data1=data1)


@app.route("/UDrugsInfo")
def UDrugsInfo():
    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26chestxraybd')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  drugtb where username='" + uname + "'  ")
    data1 = cur.fetchall()
    return render_template('UDrugsInfo.html', data1=data1)


def sendmail(Mailid, message):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    fromaddr = "projectmailm@gmail.com"
    toaddr = Mailid

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Alert"

    # string to store the body of the mail
    body = message

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "tdyr kebi hnyr yzyh")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
