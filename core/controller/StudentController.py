from flask import Blueprint, render_template, request, flash, redirect, url_for
from core.model.Student_details import Student_details

app = Blueprint('student', __name__)

# ------------------------------------------all route functions-----------------------------------------------------------------------


#committee page...
@app.route('/committee',methods = ["GET","POST"])
def Committee():
    if request.method == "GET":
        return render_template('committee_home.html')

@app.route('/student_home/<id>/<status>',methods = ["GET","POST"])
def Student_home(id,status):
    s = Student_details()

    if request.method == "GET":
        if status == 'c':
            output = s.solved_cases(id)
            return render_template('display_complaints.html', data = output ,name = "Solved")

        elif status == 'nc':
            output = s.unsolved_cases(id)
            return render_template('display_complaints.html', data = output ,name = "UnSolved")

        # if id == 'm':
    #         #fetch all medium priority cases from complaint db..
    #         medium_cases = s.get_all_medium_cases()

    #         return render_template('student_cases.html', data = medium_cases ,name = "Medium")

    #     elif id == 'h':
    #         #fetch all medium priority cases from complaint db..
    #         high_cases = s.get_all_high_cases()

    #         return render_template('student_cases.html', data = high_cases ,name = "High")

    #     elif id == 'l':
    #         #fetch all medium priority cases from complaint db..
    #         low_cases = s.get_all_low_cases()

    #         return render_template('student_cases.html', data = low_cases ,name = "Low")

    elif request.method == "POST":
        print(id) 
        data = {
            'Status' : request.form["status"],
            'Comments' : request.form["comments"],
            'Complaint_Id':id
        }
        output_update = s.update_complaint_info(data,id)
        return ('success')


# login..
@app.route('/login', methods = ["GET","POST"])
def Login():

    s = Student_details()

    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        #fetch form data..
        form_email = request.form["email"]
        form_password = request.form["password"]

        output_student = s.get_student_details_email(form_email)
        output_committee = s.get_committee_details_email(form_email)

        if output_student :
            if output_student["Password"] == form_password:
                solved = s.get_solved_cases(output_student["Id"])
                un_solved = s.get_unsolved_cases(output_student["Id"])
                # return redirect (url_for('student.Student_home', id = output_student["Id"], name = output_student["Name"], solved = solved, unsolved = un_solved))
                return render_template ('Student_home.html', id = output_student["Id"], name = output_student["Name"], solved = solved, un_solved = un_solved  )
            else:
                flash("Password is incorrect for the given email id. Please verify.")
                return render_template('login.html', data = form_email)
        elif output_committee:
            if output_committee["Password"] == form_password:
                return render_template ('committee_home.html', id = output_committee["Committee_id"], name = output_committee["Name"])
            else:
                flash("Password is incorrect for the given email id. Please verify.")
                return render_template('login.html', data = form_email)

        else:
            flash("Eamil id does not exists. Kindly verify or register yourself.")
            return render_template('login.html', data = form_email)

# register..
@app.route('/register', methods = ["GET", "POST"])
def Register():
    s = Student_details()

    if request.method == "GET":
        return render_template('register.html')
    elif request.method == "POST":
        #fetching form data..
        if request.form["name"]:
            data = {
                'Name' : request.form["name"],
                'Email_id' : request.form["email"],
                'Password' : request.form["password"],
                'Confirm_password' : request.form["confirm_password"],
                'University' : request.form["university"]
            }

            
            output = s.insert_student_info(data)
            return render_template('login.html')

        elif request.form["c_name"]:
            data = { 
                'Name': request.form["c_name"],
                'Email_id' : request.form["c_email"],
                'Password' : request.form["c_password"],
                'Confirm_password' : request.form["c_confirm_password"],
            }

            
            output = s.insert_committee_info(data)
         
        
            return render_template('login.html')

@app.route('/complaint/<id>', methods = ["GET", "POST"])
def Complaint(id):
    s = Student_details()
    output = s.get_student_details_id(id)
    solved = s.get_solved_cases(id)
    un_solved = s.get_unsolved_cases(id)

    if request.method == "GET":
        return render_template('complaint.html', id = output["Id"], name = output["Name"], solved = solved, un_solved = un_solved)
    
    elif request.method == "POST":
        print(id)
        # fetching form data..
        data = {
            'Priority' : request.form["priority"],
            'Description' : request.form["description"],
            'Category' : request.form["category"],
            'Id':id
        }
    
        output_insert = s.insert_complaint_info(data)
        flash("Your complaint has been successfully launched!")
        return render_template('complaint.html', id = output["Id"], name = output["Name"], solved = solved, un_solved = un_solved)

# student cases..
@app.route('/student_cases/<id>', methods = ["GET", "POST"])
def Student_cases (id):
    s = Student_details()

    if request.method == "GET":
        if id == 'sm':
            #fetch all solved medium priority cases from complaint db..
            solved_medium_cases = s.get_all_solved_medium_cases()
            return render_template('student_cases.html', data = solved_medium_cases ,name = "Solved Medium" )

        elif id == 'um':
            #fetch all unsolved medium priority cases from complaint db..
            unsolved_medium_cases = s.get_all_unsolved_medium_cases()
            return render_template('student_cases.html', data = unsolved_medium_cases ,name = "UnSolved Medium" )

        elif id == 'sh':
            #fetch all solved high priority cases from complaint db..
            solved_high_cases = s.get_all_solved_high_cases()
            return render_template('student_cases.html', data = solved_high_cases ,name = "Solved High" )

        elif id == 'uh':
            #fetch all inprogress high priority cases from complaint db..
            unsolved_high_cases = s.get_all_unsolved_high_cases()
            return render_template('student_cases.html', data = unsolved_high_cases ,name = "UnSolved High" )

        elif id == 'sl':
            #fetch all solved low priority cases from complaint db..
            solved_low_cases = s.get_all_solved_low_cases()

            return render_template('student_cases.html', data = solved_low_cases ,name = "Solved Low" )

        elif id == 'ul':
            #fetch all un solved low priority cases from complaint db..
            unsolved_low_cases = s.get_all_unsolved_low_cases()

            return render_template('student_cases.html', data = unsolved_low_cases ,name = "UnSolved Low" )

        elif id == 're':
            #fetch all medium priority cases from complaint db..
            reopened_cases = s.get_all_reopened_cases()

            return render_template('student_cases.html', data = reopened_cases ,name = "Re-opened" )

    elif request.method == "POST":
        print(id) 
        data = {
            'Status' : request.form["status"],
            'Comments' : request.form["comments"],
            'Complaint_Id':id
        }
        output_update = s.update_complaint_info(data,id)
        return render_template('committee_home.html')

@app.route('/student_consultation/<id>', methods = ["GET", "POST"])
def Student_consultation (id):
    s = Student_details()

    if request.method == "GET":
        if id == 'ulc':
            #fetch all medium priority cases from complaint db..
            unsolved_legal = s.get_all_unsolved_legal()

            return render_template('student_consultation.html', data = unsolved_legal ,name = "Unclosed Consultation" )

        elif id == 'slc':
            #fetch all medium priority cases from complaint db..
            solved_legal = s.get_all_solved_legal()

            return render_template('student_consultation.html', data = solved_legal ,name = "Closed Consultation" )

    elif request.method == "POST":
        print(id) 
        data = {
            'Status' : request.form["status"],
            'Comments' : request.form["comments"],
            'Consultation_Id':id
        }
        output_update = s.update_consultation_info(data,id)
        return render_template('committee_home.html')

@app.route('/display_complaint/<id>/<status>', methods = ["GET", "POST"])
def Display_complaints(id,status):
    s = Student_details()
    if request.method == "GET":
        if status == 'c':
            output = s.solved_cases(id)
            return render_template('display_complaints.html', data = output ,name = "Solved", complaint_id = output[0]["Complaint_Id"], student_id = output[0]["Id"])

        elif status == 'nc':
            output = s.unsolved_cases(id)
            return render_template('display_complaints.html', data = output ,name = "UnSolved", complaint_id = output[0]["Complaint_Id"], student_id = output[0]["Id"])

@app.route('/display_consultations/<id>/<status>', methods = ["GET", "POST"])
def Display_consultations(id,status):
    s = Student_details()
    if request.method == "GET":
        if status == 'c':
            output = s.solved_consultations(id)
            return render_template('display_consultations.html', data = output ,name = "Closed") #consultation_id = output[0]["Consultation_Id"], student_id = output[0]["Id"])

        elif status == 'nc':
            output = s.unsolved_consultations(id)
            return render_template('display_consultations.html', data = output ,name = "Pending")# consultation_id = output[0]["Consultation_Id"], student_id = output[0]["Id"])

@app.route('/back_to_login/<id>', methods = ["GET", "POST"])
def Back_to_login(id):
    if request.method == "GET":
        s = Student_details()
        #fetch student details from student_info table..
        output_student = s.get_student_details_id(id)

        #fetch all complaints launched by student from complaints table for dropdown options in student home page..
        solved = s.get_solved_cases(id)
        un_solved = s.get_unsolved_cases(id)

        return render_template ('Student_home.html', id = id, name = output_student["Name"], solved = solved, un_solved = un_solved  )

@app.route('/reopen_case/<complaint_id>', methods = ["GET", "POST"])
def Reopen_case(complaint_id):
    s = Student_details()

    status = 'Re-open'

    output = s.update_complaint_info_status(complaint_id, status)

    #fetch the details updated..

    output = s.get_complaint_info(complaint_id)

    if output:
        return redirect(url_for('student.Back_to_login', id = output[0]["Id"]))

@app.route('/about_us/', methods = ["GET", "POST"])
def About_us():
    s = Student_details()
    
    if request.method == "GET":
        return render_template ('about.html')

@app.route('/consultation/<id>', methods = ["GET", "POST"])
def Consultation(id):
    s = Student_details()
    output = s.get_student_details_id(id)
    solved = s.get_solved_cases(id)
    un_solved = s.get_unsolved_cases(id)

    if request.method == "GET":
        return render_template('consultation.html' , id = output["Id"], name = output["Name"], solved = solved, un_solved = un_solved)
    
    elif request.method == "POST":
        print(id)
        # fetching form data..
        data = {
            'Description' : request.form["description"],
            'Category' : request.form["category"],
            'Id':id
        }
    
        output_insert = s.insert_consultation_info(data)
        flash("Your request has been successfully submitted!")
        return render_template('consultation.html', id = output["Id"], name = output["Name"], solved = solved, un_solved = un_solved)

