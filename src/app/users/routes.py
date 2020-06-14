from app.models.user import User
from app.users import bp
from app.users.forms import (EditProfileForm,
                             RegistrationForm,
                             ChangeEmailForm,
                             ChangePasswordForm)
from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_required


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = RegistrationForm()

    if form.validate_on_submit():
        # Create a new user
        u = User(username=form.username.data, email=form.email.data)
        u.set_password(form.password.data)
        u.save()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('auth.login'))

    return render_template('users/register.html', title='Register', form=form)


@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form1 = EditProfileForm(current_user.username)
    form2 = ChangeEmailForm(current_user.email)

    # Edit normal information
    if form1.submit_profile.data and form1.validate_on_submit():
        if current_user.username != form1.username.data:
            current_user.username = form1.username.data
        current_user.firstname = form1.firstname.data
        current_user.lastname = form1.lastname.data
        current_user.save()
        flash('Your changes have been saved.')
        return redirect(url_for('users.edit_profile'))

    # Edit sensitive fields (Require password)
    if form2.submit_email.data and form2.validate_on_submit():
        if not current_user.check_password(form2.password.data):
            flash('Invalid password.')
            return redirect(url_for('users.edit_profile'))
        if current_user.email != form2.email.data:
            current_user.email = form2.email.data
        current_user.save()
        flash('Your email address has been changed successfully.')
        return redirect(url_for('users.edit_profile'))

    form1.username.data = current_user.username
    form1.firstname.data = current_user.firstname
    form1.lastname.data = current_user.lastname
    form2.email.data = current_user.email
    return render_template('users/edit_profile.html', title='Edit Profile',
                           form1=form1, form2=form2)


@bp.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()

    if form.validate_on_submit():
        if not current_user.check_password(form.password.data):
            flash('Invalid password.')
            return redirect(url_for('main.change_password'))
        current_user.set_password(form.new_password.data)
        current_user.save()
        flash('Your password has been changed successfully')
        return redirect(url_for('auth.logout'))

    return render_template('users/change_password.html',
                           title='Change Password', form=form)
