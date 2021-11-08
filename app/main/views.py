from flask import render_template,request,redirect,url_for,abort, flash
from . import main
from ..models import Comment, User,pitch
from flask_login import login_required
from .. import db,photos
from .forms import UpdateProfile, PitchForm, CommentForm

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data.
    '''
    pitch_form = PitchForm()
    all_pitches = pitch.query.order_by(pitch.date_posted).all()
    return render_template('index.html', pitch = all_pitches)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile',uname=user.username))
    return render_template('profile/update.html',form =form)

    
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/add_comment', methods=['GET', 'POST'])
@login_required
def add_comment():
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(name=form.name.data)
        db.session.add(comment)
        db.session.commit()
        flash('Category added successfully.')
        return redirect(url_for('.index'))
    return render_template('add_category.html', form=form)