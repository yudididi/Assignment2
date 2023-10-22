from flask import Flask, request, jsonify
import pymysql
import datetime
 
 #建立数据库连接
con = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='lby14021018',
    database='calculate'
)
 
app = Flask(__name__)
#创建游标对象
cursor = con.cursor()

#添加历史记录
@app.route('/get_history', methods=['POST'])
def get_history():
        data = request.get_json()
        calculation = data.get('calculation')
        result = data.get('result')
 
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = (time, calculation, result)
        insert = "INSERT INTO app1_calculation VALUES (%s, %s, %s)"
        cursor.execute(insert, data)
        con.commit()
 
        response_message = "ok"
        return jsonify({"message": response_message})

#获取历史记录
@app.route('/get_calculation', methods=['GET'])
def get_calculation():
        cursor.execute("SELECT calculation, result FROM app1_calculation ORDER BY time DESC LIMIT 10")
        data = cursor.fetchall()
        return jsonify({"data": data})

url = "http://localhost:5000/frontend/get_calculation" 

response = request.get(url)
data = response.json()

print(data)