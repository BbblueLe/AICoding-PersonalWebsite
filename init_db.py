import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')  # 连接到数据库文件（如果没有此文件，会自动创建）
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')  # 创建用户表（如果已存在则不重新创建）
    conn.commit()  # 提交事务
    conn.close()  # 关闭连接

if __name__ == '__main__':
    init_db()  # 调用初始化数据库函数
