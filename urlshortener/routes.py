from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from .forms import URLShortenForm
from .services import ShortenerService
from .models import URL
from .extensions import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    form = URLShortenForm()
    if form.validate_on_submit():
        url_obj, error = ShortenerService.create_short_url(
            form.original_url.data, 
            form.custom_alias.data
        )
        if error:
            flash(error, 'danger')
        elif url_obj:
            return render_template('result.html', url=url_obj)
        else:
            flash('Unknown error occurred.', 'danger')
    
    stats = ShortenerService.get_url_stats()
    return render_template('index.html', form=form, stats=stats)

@main_bp.route('/<short_code>')
def redirect_to_url(short_code):
    url_record = URL.query.filter_by(short_code=short_code, is_active=True).first()
    if url_record:
        url_record.clicks += 1
        db.session.commit()
        return redirect(url_record.original_url)
    abort(404)

@main_bp.route('/dashboard')
def dashboard():
    urls = ShortenerService.get_all_urls()
    return render_template('dashboard.html', urls=urls)

@main_bp.route('/analytics')
def analytics():
    stats = ShortenerService.get_url_stats()
    return render_template('analytics.html', stats=stats)

@main_bp.route('/delete/<int:url_id>', methods=['POST'])
def delete_url(url_id):
    if ShortenerService.delete_url(url_id):
        flash('Link deleted successfully.', 'success')
    else:
        flash('Link not found.', 'danger')
    return redirect(url_for('main.dashboard'))
