"""
==============================================================================
📊 DATA SCIENCE PORTFOLIO
==============================================================================
Flask app for Data Scientist portfolio

Run:
    python app.py

Author: Lutik Nikita
==============================================================================
"""

from flask import Flask, render_template, request, redirect, url_for, flash, abort
from datetime import datetime

# import data from config/data.py
from config.data import (
    PERSONAL_INFO,
    STATS,
    SKILLS,
    PROJECTS,
    PROJECT_CATEGORIES
)

# ==============================================================================
# INITIALIZATION
# ==============================================================================

app = Flask(__name__)

# TODO: Замени на свой секретный ключ (любая случайная строка)
app.secret_key = 'your-secret-key-change-this-to-random-string'


# ==============================================================================
# SUPPORT FUNCTIONS
# ==============================================================================

def get_project_by_id(project_id):
    """Get project by ID"""
    for project in PROJECTS:
        if project['id'] == project_id:
            return project
    return None


def get_featured_projects():
    """Get selected projects for main page"""
    return [p for p in PROJECTS if p.get('featured', False)]


def get_projects_by_category(category):
    """Get projects by category"""
    if category == 'all':
        return PROJECTS
    return [p for p in PROJECTS if category in p.get('categories', [])]


# ==============================================================================
# CONTEXT FOR ALL TEMPLATES
# ==============================================================================

@app.context_processor
def inject_globals():
    """Переменные, доступные во всех шаблонах"""
    return {
        'info': PERSONAL_INFO,
        'current_year': datetime.now().year,
    }


# ==============================================================================
# МАРШРУТЫ
# ==============================================================================

@app.route('/')
def index():
    """Главная страница"""
    return render_template(
        'index.html',
        stats=STATS,
        skills=SKILLS,
        featured_projects=get_featured_projects(),
    )


@app.route('/projects')
def projects():
    """Страница со всеми проектами"""
    # Получаем категорию из query параметра (?category=ML)
    category = request.args.get('category', 'all')

    return render_template(
        'projects.html',
        projects=get_projects_by_category(category),
        categories=PROJECT_CATEGORIES,
        current_category=category,
    )


@app.route('/projects/<project_id>')
def project_detail(project_id):
    """Детальная страница проекта"""
    project = get_project_by_id(project_id)

    if not project:
        abort(404)

    # Получаем похожие проекты (той же категории)
    similar = [
        p for p in PROJECTS
        if p['id'] != project_id and
           any(cat in p.get('categories', []) for cat in project.get('categories', []))
    ][:2]  # Максимум 2 похожих

    return render_template(
        'project_detail.html',
        project=project,
        similar_projects=similar,
    )


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Страница контактов"""
    if request.method == 'POST':
        # Получаем данные формы
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        subject = request.form.get('subject', '').strip()
        message = request.form.get('message', '').strip()

        # Простая валидация
        if not name or not email or not message:
            flash('Пожалуйста, заполните все обязательные поля', 'error')
            return redirect(url_for('contact'))

        # TODO: Здесь можно добавить отправку email или сохранение в БД
        # Пример с отправкой в Telegram:
        # send_telegram_message(f"Новое сообщение от {name} ({email}): {message}")

        # Выводим в консоль (для отладки)
        print(f"""
        ╔══════════════════════════════════════════╗
        ║         📧 НОВОЕ СООБЩЕНИЕ               ║
        ╠══════════════════════════════════════════╣
        ║ От: {name}
        ║ Email: {email}
        ║ Тема: {subject}
        ║ Сообщение: {message}
        ╚══════════════════════════════════════════╝
        """)

        flash('Спасибо! Ваше сообщение отправлено.', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')


# ==============================================================================
# ERROR PROCESSING
# ==============================================================================

@app.errorhandler(404)
def page_not_found(e):
    """Страница 404"""
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(e):
    """Страница 500"""
    return render_template('500.html'), 500


# ==============================================================================
# RUN
# ==============================================================================

if __name__ == '__main__':
    # Debug=True только для разработки!
    # При деплое поставь Debug=False
    app.run(debug=True, host='0.0.0.0', port=5000)