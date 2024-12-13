from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Project class (One-to-many with Task)
class Project(Base):
    __tablename__ = 'projects'
    
    # Define columns
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)

    # Relationship to Task (One project can have many tasks)
    tasks = relationship("Task", back_populates="project", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Project(name={self.name}, description={self.description})>"

    @classmethod
    def create(cls, session, name, description):
        project = cls(name=name, description=description)
        session.add(project)
        session.commit()

    @classmethod
    def delete(cls, session, project_id):
        project = session.query(cls).get(project_id)
        if project:
            session.delete(project)
            session.commit()
        else:
            print("Project not found.")

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, project_id):
        return session.query(cls).get(project_id)

    @classmethod
    def find_by_name(cls, session, name):
        return session.query(cls).filter(cls.name == name).all()


# Task class (Many-to-one with Project)
class Task(Base):
    __tablename__ = 'tasks'
    
    # Define columns
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    completed = Column(Integer, default=0)  # 0 = not completed, 1 = completed
    project_id = Column(Integer, ForeignKey('projects.id'))

    # Relationship to Project (One task belongs to one project)
    project = relationship("Project", back_populates="tasks")

    def __repr__(self):
        return f"<Task(description={self.description}, completed={self.completed}, project_id={self.project_id})>"

    @classmethod
    def create(cls, session, description, project_id):
        task = cls(description=description, project_id=project_id)
        session.add(task)
        session.commit()

    @classmethod
    def delete(cls, session, task_id):
        task = session.query(cls).get(task_id)
        if task:
            session.delete(task)
            session.commit()
        else:
            print("Task not found.")

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, task_id):
        return session.query(cls).get(task_id)

    @classmethod
    def find_by_description(cls, session, description):
        return session.query(cls).filter(cls.description.ilike(f'%{description}%')).all()
