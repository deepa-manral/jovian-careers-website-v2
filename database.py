from sqlalchemy import create_engine, text
import os

database_string = os.environ['DATABASE_STRING']
engine = create_engine(database_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"),
                          {"val": id})
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text(
        "INSERT INTO applications (job_id, full_name, email, linkedin, education,"
        " work_experience, resume_) "
        "VALUES (:job_id, :full_name, :email, :linkedin, "
        ":education, :work_experience, :resume_)")
    conn.execute(
        query, {
            "job_id": job_id,
            "full_name": data['full_name'],
            "email": data['email'],
            "linkedin": data['linkedin'],
            "education": data['edu'],
            "work_experience": data['Workexp'],
            "resume_": data['resume']
        })
