from flask import Flask , render_template , request , redirect , url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
import sys
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:localdb@localhost:5432/todoapp'
db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer , primary_key = True)
    description = db.Column(db.String(),nullable = False)
    completed = db.Column(db.Boolean, nullable=False)


    def __repr__(self):
        return f"<Todo {self.id} {self.description}>"

with app.app_context():
    db.create_all()

@app.route('/todoapp/create' , methods = ['POST'])
def create_todo():
    error = False
    body = {}
    try:
        description = request.get_json()['description']
        todo = Todo(description = description)
        db.session.add(todo)
        db.session.commit()
        body['description'] = todo.description
    except:
        error = True
        db.session.rollback()    
        print(sys.exc_info())
    finally:
        db.session.close()    
    if not error:
        return jsonify(body)


@app.route('/todos/<todoId>/set-completed' , methods=['POST'])
def set_completed_todo(todoId):
    try:
        completed = request.get_json()['completed']
        todo = Todo.query.get(todoId)
        todo.completed = completed
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
        return redirect(url_for('index'))    

@app.route('/todos/<todoId>' , methods=['DELETE'])
def delete_todo(todoId):
    try:
        Todo.query.filter_by(id=todoId).delete()
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
        return jsonify({'success': True})            


@app.route('/')
def index():
    return render_template('index.html', data =Todo.query.all())


if __name__ == "__main__":
    app.run(debug=True,port=9000)

    