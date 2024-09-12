from teacher_crud import TeacherCRUD
from teacher_cli import TeacherCLI

if __name__ == '__main__':
    teacherCRUD = TeacherCRUD('neo4j+s://94edaa4a.databases.neo4j.io', 'neo4j', 'rlz79wWyU1w3RqQsLW4Kr_ypFm2RaqooSYs1-4jcX8o')
    cli = TeacherCLI(teacherCRUD)
    cli.run()
    
    teacherCRUD.close()
