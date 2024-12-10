from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# 连接数据库
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # 允许使用列名作为字典键
    return conn

# 首页路由，展示数据库中的个人信息
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')  # 查询数据库中的用户信息
    users = cursor.fetchall()  # 获取所有结果
    conn.close()
    return render_template('index.html', users=users)

# 提交个人信息的路由
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))  # 插入数据
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

