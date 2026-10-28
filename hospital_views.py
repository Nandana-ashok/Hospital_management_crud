from mysql import connector
from datetime import datetime

class HospitalConnection:
    def get_connection(self):
        try:
            self.connection = connector.connect(
                host='localhost',
                user='root',
                password='Nandana@2004',
                database='hospital_db'
            )
            return self.connection
        except Exception as e:
            self.connection = None
            print(e)
            
class HospitalManagement(HospitalConnection):
    def get_object(self,patient_id=None):
        try:
            self.connection = super().get_connection()
            if self.connection is None:
                return
            else:
                self.cursor = self.connection.cursor()
                query = 'select * from patient where patient_id = %s'
                values = (patient_id,)
                self.cursor.execute(query,values)
                record = self.cursor.fetchone()
                if record is not None:
                   return record
                else:
                   print('data not exist')
        except Exception as e:
            print(e)

    def get(self):
        try:
            self.connection = super().get_connection()
            if self.connection is not None:
               self.cursor = self.connection.cursor()
               query = 'select * from patient '
               self.cursor.execute(query)
               record = self.cursor.fetchall()
               for i in record:
                   print(i)
            else:
                return None
        except Exception as e:
            print(e)

    def post(self,**kwargs):
        try:
            self.connection = super().get_connection()
            if self.connection is not None:
               self.cursor = self.connection.cursor()
               query = '''insert into patient(name,age,gender,disease,doctor_name,admission_date,bill_amount)
                        values(%s , %s, %s ,%s , %s , %s ,%s)'''
               values = [v for v in kwargs.values()]
               self.cursor.execute(query,values)
               self.connection.commit()
               print('Patient details added successfully')
            else:
                return None
        except Exception as e:
            print(e)

    def retrieval(self,patient_id=None):
        try:
            record = self.get_object(patient_id=patient_id)
            if record is None:
                return None
            else:
                print(record)
        except Exception as e:
            print(e)

    def delete(self,patient_id=None):
        try:
            record = self.get_object(patient_id=patient_id)
            if record is not None:
                self.connection = super().get_connection()
                if self.connection is not None:
                   self.cursor = self.connection.cursor()
                   query = 'delete from patient where patient_id =%s'
                   value =(patient_id,)
                   self.cursor.execute(query,value)
                   self.connection.commit()
                   print('Patient data is deleted...')
                else:
                   return None
            else:
                return None
        except Exception as e:
            print(e)

    def put(self,patient_id=None,**kwargs):
        try:
            if kwargs :
               self.connection = self.get_connection()

               if self.connection is not None:

                  self.cursor = self.connection.cursor()
                  query = 'select * from patient where patient_id=%s'
                  self.cursor.execute(query,(patient_id,))
                  record = self.cursor.fetchone()
                  if record is not None:
                     placeholder = ""
                     for i in kwargs.keys():
                         placeholder += i + "=%s,"
                     placeholder = placeholder.rstrip(',')
                     query = f'update patient set {placeholder} where patient_id=%s'
                     values = [v for v in kwargs.values()]
                     values.append(patient_id)
                     self.cursor.execute(query,values)
                     self.connection.commit()
                     print('Patient is updated successfully.....')
                  else:
                      return None
               else:
                   return None
            else:
                print('no data are passed to update')

        except Exception as e:
            print(e)


connection = HospitalConnection()
print(connection.get_connection())
patient = HospitalManagement()

print('-----------------------------------------------------------')
patient.get()
print('-----------------------------------------------------------')
# patient.post(name='nandana',age=22,gender='female',disease='fever',doctor_name='ravi',admission_date=datetime.today(),bill_amount=300)
# patient.post(name='ansa',age=22,gender='female',disease='stomachache',doctor_name='alex',admission_date=datetime.today(),bill_amount=550)
# patient.post(name='navya',age=21,gender='female',disease='headache',doctor_name='kumar',admission_date=datetime.today(),bill_amount=500)
print('-----------------------------------------------------------')
patient.retrieval(1)
print('-----------------------------------------------------------')
# patient.delete(2)
print('-----------------------------------------------------------')
patient.put(10)







