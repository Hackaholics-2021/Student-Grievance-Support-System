from sqlalchemy import create_engine, MetaData, Table, insert, select
from core import app
from sqlalchemy.sql import and_, or_


engine = create_engine(app.config['DATABASE_URI'])

#creating a class Mos_user_details for the table mos_user_details 
class Student_details():
    def __init__(self):
        try:
            self.meta = MetaData()
            self.student_info = Table("student_info", self.meta, autoload=True, autoload_with=engine)
            self.complaint_info = Table("complaint_info", self.meta, autoload=True, autoload_with=engine)
            self.committee_info = Table("committee_info", self.meta, autoload=True, autoload_with=engine)
            self.consultation_info = Table("consultation_info", self.meta, autoload=True, autoload_with=engine)
        except Exception as e:
            print(e)

    def insert_student_info(self,data):
        print('inside model insert_student_info')
        result = engine.execute(self.student_info.insert(), data)
        print(result)
        return result

    def insert_committee_info(self,data):
        print('inside model insert_committee_info')
        result = engine.execute(self.committee_info.insert(), data)
        print(result)
        return result
        
    def insert_complaint_info(self,data):
        print('inside model insert_complaint_info')
        result = engine.execute(self.complaint_info.insert(), data)
        return result

    def insert_consultation_info(self,data):
        print('inside model insert_consultation_info')
        result = engine.execute(self.consultation_info.insert(), data)
        return result


    def get_student_details_email(self,email):
        print('inside model get_student_info')
        stmt = self.student_info.select().where(self.student_info.c.Email_id.in_([email]))
        result = engine.execute(stmt)
        results = [dict(r) for r in result] if result else None
        if results : 
            return results[0]
        else:
            return None

    def get_committee_details_email(self,email):
        print('inside model get_student_info')
        stmt = self.committee_info.select().where(self.committee_info.c.Email_id.in_([email]))
        result = engine.execute(stmt)
        results = [dict(r) for r in result] if result else None
        if results : 
            return results[0]
        else:
            return None

    def get_student_details_id(self,id):
        stmt = self.student_info.select().where(self.student_info.c.Id.in_([id]))
        result = engine.execute(stmt)
        results = [dict(r) for r in result] if result else None
        if results : 
            return results[0]
        else:
            return None

    def get_all_solved_high_cases(self):
        stmt = self.complaint_info.select().where(
            and_(
                self.complaint_info.c.Priority.in_(['High']),
                self.complaint_info.c.Status.in_(['Closed'])
            )
        )
        result = engine.execute(stmt)
        out="no solved cases"
        results = [dict(r) for r in result] 
        print(results)
        return results

    def get_all_unsolved_high_cases(self):
        stmt = self.complaint_info.select().where(
            and_(
                self.complaint_info.c.Priority.in_(['High']),
                self.complaint_info.c.Status.notin_(['Closed'])
            )
        )
        result = engine.execute(stmt)
        results = [dict(r) for r in result] 
        print(results)
        return results

    def get_all_solved_medium_cases(self):
        stmt = self.complaint_info.select().where(
            and_(
                self.complaint_info.c.Priority.in_(['Medium']),
                self.complaint_info.c.Status.in_(['Closed'])
            )
        )
        result = engine.execute(stmt)
        results = [dict(r) for r in result]  
        print(results)
        return results

    def get_all_unsolved_medium_cases(self):
        stmt = self.complaint_info.select().where(
            and_(
                self.complaint_info.c.Priority.in_(['Medium']),
                self.complaint_info.c.Status.notin_(['Closed'])
            )
        )
        result = engine.execute(stmt)
        results = [dict(r) for r in result] 
        print(results)
        return results
            
    def get_all_solved_low_cases(self):
        stmt = self.complaint_info.select().where(
            and_(
                self.complaint_info.c.Priority.in_(['Low']),
                self.complaint_info.c.Status.in_(['Closed'])
            )
        )
        result = engine.execute(stmt)
        results = [dict(r) for r in result] 
        print(results)
        return results
        

    def get_all_unsolved_low_cases(self):
        stmt = self.complaint_info.select().where(
            and_(
                self.complaint_info.c.Priority.in_(['Low']),
                self.complaint_info.c.Status.notin_(['Closed'])
            )
        )
        result = engine.execute(stmt)
        results = [dict(r) for r in result]
        print(results)
        return results

    def get_all_reopened_cases(self):
        stmt = self.complaint_info.select().where(self.complaint_info.c.Status.in_(['Re-open']))
        result = engine.execute(stmt)
        results = [dict(r) for r in result]
        print(results)
        return results

    def get_all_unsolved_legal(self):
        stmt = self.consultation_info.select().where(self.consultation_info.c.Status.notin_(['Closed']))
        result = engine.execute(stmt)
        results = [dict(r) for r in result]
        print(results)
        return results

    def get_all_solved_legal(self):
        stmt = self.consultation_info.select().where(self.consultation_info.c.Status.in_(['Closed']))
        result = engine.execute(stmt)
        results = [dict(r) for r in result]
        print(results)
        return results

    def update_complaint_info(self,data,id):
        stmt = self.complaint_info.update().where(self.complaint_info.c.Complaint_Id.in_([id]))
        result = engine.execute(stmt,data)
        return result

    def update_consultation_info(self,data,id):
        stmt = self.consultation_info.update().where(self.consultation_info.c.Consultation_Id.in_([id]))
        result = engine.execute(stmt,data)
        return result

    def get_solved_cases(self,id):
        stmt = self.complaint_info.select().where(
            and_(
                self.complaint_info.c.Id.in_([id]),
                self.complaint_info.c.Status.in_(['Closed'])
            )
        )
        result = engine.execute(stmt)
        if result :
            return (result.rowcount)
        else:
            return 0
        
    def get_unsolved_cases(self,id):
        stmt = self.complaint_info.select().where(
            and_(
                self.complaint_info.c.Id.in_([id]),
                self.complaint_info.c.Status.notin_(['Closed'])
            )
        )
        result = engine.execute(stmt)
        if result :
            return (result.rowcount)
        else:
            return 0

    def get_allsolved_high_cases(self):
        stmt = self.complaint_info.select().where(
            and_(
                self.complaint_info.c.Priority.in_(["High"]),
                self.complaint_info.c.Status.in_(['Closed'])
            )
        )
        result = engine.execute(stmt)
        if result :
            return (result.rowcount)
        else:
            return 0
        
    def get_allunsolved_high_cases(self):
        stmt = self.complaint_info.select().where(
            and_(
                self.complaint_info.c.Priority.in_(["High"]),
                self.complaint_info.c.Status.notin_(['Closed'])
            )
        )
        result = engine.execute(stmt)
        if result :
            return (result.rowcount)
        else:
            return 0
    
    def solved_cases(self,id):
        stmt = self.complaint_info.select().where(
            and_(
                self.complaint_info.c.Id.in_([id]),
                self.complaint_info.c.Status.in_(['Closed'])
            )
        )
        result = engine.execute(stmt)
        results = [dict(r) for r in result] 
        print(results)
        return results

    def unsolved_cases(self,id):
        stmt = self.complaint_info.select().where(
            and_(
                self.complaint_info.c.Id.in_([id]),
                self.complaint_info.c.Status.notin_(['Closed'])
            )
        )
        result = engine.execute(stmt)
        results = [dict(r) for r in result]
        print(results)
        return results

    def solved_consultations(self,id):
        stmt = self.consultation_info.select().where(
            and_(
                self.consultation_info.c.Id.in_([id]),
                self.consultation_info.c.Status.in_(['Closed'])
            )
        )
        result = engine.execute(stmt)
        results = [dict(r) for r in result]
        print(results)
        return results

    def unsolved_consultations(self,id):
        stmt = self.consultation_info.select().where(
            and_(
                self.consultation_info.c.Id.in_([id]),
                self.consultation_info.c.Status.notin_(['Closed'])
            )
        )
        result = engine.execute(stmt)
        results = [dict(r) for r in result] 
        print(results)
        return results

    def update_complaint_info_status(self,id,status):
        stmt = self.complaint_info.update().values ({"Status":status}).where(self.complaint_info.c.Complaint_Id.in_([id]))
        result = engine.execute(stmt)
        return result

    def get_complaint_info(self,id):
        stmt = self.complaint_info.select().where(self.complaint_info.c.Complaint_Id.in_([id]))
        result = engine.execute(stmt)
        results = [dict(r) for r in result] if result else None
        print(result)
        print(results)
        return results

        








