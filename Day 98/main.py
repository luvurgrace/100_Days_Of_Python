from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# ============== APP CONFIG ==============
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Регистрация Python функций для использования в Jinja2 шаблонах
app.jinja_env.globals.update(min=min, max=max)

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


# ============== MODELS ==============
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    reports = db.relationship('MonthlyReport', backref='user', lazy=True)
    goals = db.relationship('Goal', backref='user', lazy=True)


class MonthlyReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    month = db.Column(db.Integer, nullable=False)

    # Income
    income_plan = db.Column(db.Float, default=0)
    income_fact = db.Column(db.Float, default=0)

    # Expenses - Plan
    plan_housing = db.Column(db.Float, default=0)
    plan_food = db.Column(db.Float, default=0)
    plan_transport = db.Column(db.Float, default=0)
    plan_entertainment = db.Column(db.Float, default=0)
    plan_shopping = db.Column(db.Float, default=0)
    plan_health = db.Column(db.Float, default=0)
    plan_education = db.Column(db.Float, default=0)
    plan_other = db.Column(db.Float, default=0)

    # Expenses - Fact
    fact_housing = db.Column(db.Float, default=0)
    fact_food = db.Column(db.Float, default=0)
    fact_transport = db.Column(db.Float, default=0)
    fact_entertainment = db.Column(db.Float, default=0)
    fact_shopping = db.Column(db.Float, default=0)
    fact_health = db.Column(db.Float, default=0)
    fact_education = db.Column(db.Float, default=0)
    fact_other = db.Column(db.Float, default=0)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def total_plan(self):
        return (self.plan_housing + self.plan_food + self.plan_transport +
                self.plan_entertainment + self.plan_shopping + self.plan_health +
                self.plan_education + self.plan_other)

    @property
    def total_fact(self):
        return (self.fact_housing + self.fact_food + self.fact_transport +
                self.fact_entertainment + self.fact_shopping + self.fact_health +
                self.fact_education + self.fact_other)

    @property
    def savings_plan(self):
        return self.income_plan - self.total_plan

    @property
    def savings_fact(self):
        return self.income_fact - self.total_fact


class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    icon = db.Column(db.String(50), default='bi-star')
    target_amount = db.Column(db.Float, nullable=False)
    current_amount = db.Column(db.Float, default=0)
    is_completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def progress(self):
        if self.target_amount > 0:
            return min(round((self.current_amount / self.target_amount) * 100, 1), 100)
        return 0

    @property
    def remaining(self):
        return max(0, self.target_amount - self.current_amount)


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


# ============== CATEGORIES ==============
CATEGORIES = [
    {'key': 'housing', 'name': 'Housing', 'icon': 'bi-house'},
    {'key': 'food', 'name': 'Food', 'icon': 'bi-cart'},
    {'key': 'transport', 'name': 'Transport', 'icon': 'bi-car-front'},
    {'key': 'entertainment', 'name': 'Entertainment', 'icon': 'bi-film'},
    {'key': 'shopping', 'name': 'Shopping', 'icon': 'bi-bag'},
    {'key': 'health', 'name': 'Health', 'icon': 'bi-heart-pulse'},
    {'key': 'education', 'name': 'Education', 'icon': 'bi-book'},
    {'key': 'other', 'name': 'Other', 'icon': 'bi-three-dots'},
]

MONTHS = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]


# ============== ROUTES: AUTH ==============
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if user exists
        if User.query.filter_by(email=email).first():
            flash('Email already registered.', 'error')
            return redirect(url_for('register'))

        if User.query.filter_by(username=username).first():
            flash('Username already taken.', 'error')
            return redirect(url_for('register'))

        # Create new user
        new_user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password)
        )
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        flash('Account created successfully!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash('Welcome back!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password.', 'error')

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))


# ============== ROUTES: MAIN ==============
@app.route('/')
@login_required
def dashboard():
    now = datetime.now()
    current_report = MonthlyReport.query.filter_by(
        user_id=current_user.id,
        year=now.year,
        month=now.month
    ).first()

    goals = Goal.query.filter_by(user_id=current_user.id, is_completed=False).limit(3).all()

    return render_template('dashboard.html',
                           report=current_report,
                           goals=goals,
                           categories=CATEGORIES,
                           current_month=MONTHS[now.month - 1],
                           current_year=now.year)


@app.route('/monthly')
@login_required
def monthly():
    reports = MonthlyReport.query.filter_by(user_id=current_user.id) \
        .order_by(MonthlyReport.year.desc(), MonthlyReport.month.desc()).all()
    return render_template('monthly.html', reports=reports, months=MONTHS)


@app.route('/monthly/add', methods=['GET', 'POST'])
@login_required
def add_monthly():
    now = datetime.now()

    if request.method == 'POST':
        year = int(request.form.get('year'))
        month = int(request.form.get('month'))

        # Check if report exists
        report = MonthlyReport.query.filter_by(
            user_id=current_user.id, year=year, month=month
        ).first()

        if not report:
            report = MonthlyReport(user_id=current_user.id, year=year, month=month)
            db.session.add(report)

        # Update values
        report.income_plan = float(request.form.get('income_plan') or 0)
        report.income_fact = float(request.form.get('income_fact') or 0)

        for cat in CATEGORIES:
            setattr(report, f"plan_{cat['key']}", float(request.form.get(f"plan_{cat['key']}") or 0))
            setattr(report, f"fact_{cat['key']}", float(request.form.get(f"fact_{cat['key']}") or 0))

        db.session.commit()
        flash('Report saved successfully!', 'success')
        return redirect(url_for('monthly'))

    # GET - check for copy from previous month
    copy_from = request.args.get('copy_from')
    previous_report = None

    if copy_from:
        prev_year, prev_month = map(int, copy_from.split('-'))
        previous_report = MonthlyReport.query.filter_by(
            user_id=current_user.id, year=prev_year, month=prev_month
        ).first()

    return render_template('add_monthly.html',
                           categories=CATEGORIES,
                           months=MONTHS,
                           current_year=now.year,
                           current_month=now.month,
                           previous_report=previous_report)


@app.route('/monthly/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_monthly(id):
    report = MonthlyReport.query.get_or_404(id)

    if report.user_id != current_user.id:
        flash('Access denied.', 'error')
        return redirect(url_for('monthly'))

    if request.method == 'POST':
        report.income_plan = float(request.form.get('income_plan') or 0)
        report.income_fact = float(request.form.get('income_fact') or 0)

        for cat in CATEGORIES:
            setattr(report, f"plan_{cat['key']}", float(request.form.get(f"plan_{cat['key']}") or 0))
            setattr(report, f"fact_{cat['key']}", float(request.form.get(f"fact_{cat['key']}") or 0))

        db.session.commit()
        flash('Report updated successfully!', 'success')
        return redirect(url_for('monthly'))

    return render_template('edit_monthly.html',
                           report=report,
                           categories=CATEGORIES,
                           months=MONTHS)


@app.route('/monthly/delete/<int:id>')
@login_required
def delete_monthly(id):
    report = MonthlyReport.query.get_or_404(id)

    if report.user_id != current_user.id:
        flash('Access denied.', 'error')
        return redirect(url_for('monthly'))

    db.session.delete(report)
    db.session.commit()
    flash('Report deleted.', 'success')
    return redirect(url_for('monthly'))


# ============== ROUTES: ANALYTICS ==============
@app.route('/analytics')
@login_required
def analytics():
    year = request.args.get('year', datetime.now().year, type=int)

    reports = MonthlyReport.query.filter_by(user_id=current_user.id, year=year) \
        .order_by(MonthlyReport.month).all()

    # Prepare data for charts
    months_data = []
    max_value = 1  # min 1

    for month in range(1, 13):
        report = next((r for r in reports if r.month == month), None)
        income = report.income_fact if report else 0
        expense = report.total_fact if report else 0

        # Look for max
        if income > max_value:
            max_value = income
        if expense > max_value:
            max_value = expense

        months_data.append({
            'month': MONTHS[month - 1][:3],
            'income': income,
            'expense': expense,
            'savings': report.savings_fact if report else 0
        })

    # Totals
    total_income = sum(r.income_fact for r in reports)
    total_expense = sum(r.total_fact for r in reports)
    total_savings = total_income - total_expense

    # Category totals
    category_totals = []
    for cat in CATEGORIES:
        total = sum(getattr(r, f"fact_{cat['key']}") for r in reports)
        category_totals.append({
            'name': cat['name'],
            'icon': cat['icon'],
            'amount': total,
            'percent': round((total / total_expense * 100), 1) if total_expense > 0 else 0
        })
    category_totals.sort(key=lambda x: x['amount'], reverse=True)

    # Available years
    all_reports = MonthlyReport.query.filter_by(user_id=current_user.id).all()
    years = sorted(set(r.year for r in all_reports), reverse=True)
    if not years:
        years = [datetime.now().year]

    return render_template('analytics.html',
                           months_data=months_data,
                           max_value=max_value,
                           total_income=total_income,
                           total_expense=total_expense,
                           total_savings=total_savings,
                           category_totals=category_totals,
                           current_year=year,
                           years=years)


# ============== ROUTES: GOALS ==============
@app.route('/goals')
@login_required
def goals():
    active_goals = Goal.query.filter_by(user_id=current_user.id, is_completed=False).all()
    completed_goals = Goal.query.filter_by(user_id=current_user.id, is_completed=True).all()
    return render_template('goals.html', active_goals=active_goals, completed_goals=completed_goals)


@app.route('/goals/add', methods=['POST'])
@login_required
def add_goal():
    name = request.form.get('name')
    icon = request.form.get('icon', '🎯')
    target_amount = float(request.form.get('target_amount') or 0)

    goal = Goal(
        user_id=current_user.id,
        name=name,
        icon=icon,
        target_amount=target_amount
    )
    db.session.add(goal)
    db.session.commit()
    flash('Goal created!', 'success')
    return redirect(url_for('goals'))


@app.route('/goals/contribute/<int:id>', methods=['POST'])
@login_required
def contribute_goal(id):
    goal = Goal.query.get_or_404(id)

    if goal.user_id != current_user.id:
        flash('Access denied.', 'error')
        return redirect(url_for('goals'))

    amount = float(request.form.get('amount') or 0)
    action = request.form.get('action', 'add')

    if action == 'subtract':
        goal.current_amount -= amount
        goal.current_amount = max(0, goal.current_amount)  # Не уходим в минус
        flash(f'Removed ${amount:.0f} from {goal.name}', 'success')
    else:
        goal.current_amount += amount
        flash(f'Added ${amount:.0f} to {goal.name}', 'success')

    # Check if completed
    if goal.current_amount >= goal.target_amount:
        goal.is_completed = True
        flash(f'Goal "{goal.name}" completed!', 'success')
    else:
        goal.is_completed = False

    db.session.commit()
    return redirect(url_for('goals'))


@app.route('/goals/delete/<int:id>')
@login_required
def delete_goal(id):
    goal = Goal.query.get_or_404(id)

    if goal.user_id != current_user.id:
        flash('Access denied.', 'error')
        return redirect(url_for('goals'))

    db.session.delete(goal)
    db.session.commit()
    flash('Goal deleted.', 'success')
    return redirect(url_for('goals'))


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


@app.route('/profile/delete', methods=['POST'])
@login_required
def delete_account():
    user_id = current_user.id

    # Delete all user data
    MonthlyReport.query.filter_by(user_id=user_id).delete()
    Goal.query.filter_by(user_id=user_id).delete()

    # Delete user
    user = db.session.get(User, user_id)
    logout_user()
    db.session.delete(user)
    db.session.commit()

    flash('Your account has been deleted.', 'success')
    return redirect(url_for('login'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500


# ============== CREATE DB ==============
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
