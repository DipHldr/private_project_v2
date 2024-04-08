from sqlalchemy import create_engine,text
from flask import jsonify
from Confi import db_connection_string
engine = create_engine(db_connection_string)

def load_jobs_from_db():
    with engine.connect() as conn:
      result=conn.execute(text("select * from jobs"))

      jobs=[]
      for row in result.all():
          jobs.append(row._mapping)
    return jobs
    # print(jobs)
# load_jobs_from_db()


# with engine.connect() as conn:
#       result=conn.execute(text("select * from jobs"))
    #   
    #   print(type(result))
    #   result_all=result.all()
    #   print(type(result_all))
    #   first_result=result_all[0]
    #   print(type(first_result))
    #   first_result_dict= User.as_dict(first_result)
    #   print(type(first_result_dict))
      # print(first_result_dict['requirements'])
