from project import app
from flask import render_template,flash,url_for,redirect,jsonify
from project.models import Item
from flask import request
from project import db
from marshmallow import Schema, fields

class ItemSchema(Schema):
    class Meta:
        fields = ('id', 'name', 'fname', 'description')
item_schema = ItemSchema()


@app.route('/')
@app.route('/create', methods=['GET'])
def create_item_form():
    return render_template('index.html')

@app.route('/createuser', methods=['POST'])
def create():

    name = request.form.get('name')
    fname = request.form.get('fname')
    description = request.form.get('description')



    new_item = Item(name=name, fname=fname,description=description)
    db.session.add(new_item)
    db.session.commit()

    #serializing the created item and sending it as JSON response

    serialized_item = item_schema.dump(new_item)
    return jsonify(serialized_item)
    #flash(f'New user created', category='success')
    #return redirect(url_for("create_item_form"))


@app.route("/read",methods=['GET'])
def Read_page():

    item = Item.query.all()
    return render_template('read.html', item=item)

@app.route('/update', methods=['GET'])
def Update_page():
    item = Item.query.all()
    return render_template('update.html', item=item)




@app.route("/Updateuser/<int:id>",methods=['POST'])
def Updateuser(id):

        user_to_update = Item.query.get_or_404(id)
        user_to_update.name= request.form['name']
        user_to_update.fname = request.form['fname']
        user_to_update.description = request.form['description']

        try:
            db.session.commit()
            flash(f"User: {id} Updated!")
        except:
            flash(f"User: {id} not Updated!")

        # serializing the updated item and sending it as JSON response
        serialized_item = item_schema.dump(user_to_update)
        return jsonify(serialized_item)
        #return redirect(url_for("Update_page"))


@app.route('/delete', methods=['GET'])
def Delete_page():
    item = Item.query.all()
    return render_template('delete.html', item=item)

@app.route("/Deleteuser/<int:id>",methods=['POST'])
def Deleteuser(id):
    user_to_delete = Item.query.get_or_404(id)

    try:
        db.session.delete(user_to_delete)
        db.session.commit()

        flash(f"User: {id} deleted!", category='success')
    except:
        flash(f"User: {id} not deleted!", category='danger')

    return redirect(url_for("Delete_page"))

