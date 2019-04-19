#!/usr/bin/env python3
from flask import Flask,render_template,request,jsonify, send_file,json
import sqlite3
db = sqlite3.connect('data.db', check_same_thread=False)           ###Making an SQL Table Database to store answers of quizzes###
cursor = db.cursor()
cursor.execute('''
	CREATE TABLE IF NOT EXISTS data(ans1 TEXT, ans2 TEXT,
                       ans3 TEXT, ans4 TEXT)
	''')
db.commit()
app = Flask(__name__)

@app.route('/')
@app.route('/Introduction.html')                                 
def index():
	return render_template('Introduction.html')

@app.route('/Theory.html')
def theory():
	return render_template('Theory.html')	

@app.route('/Objective.html')
def objective():
	return render_template('Objective.html')	

@app.route('/Experiment.html')
def experiment():
	return render_template('Experiment.html')	

@app.route('/Quizzes.html')
def quizzes():
	return render_template('Quizzes.html')

@app.route('/Procedure.html')
def procedure():
	return render_template('Procedure.html')		

@app.route('/Feedback.html')
def feedback():
	return render_template('Feedback.html')	

@app.route('/Further Readings.html')
def further():
	return render_template('Further Readings.html')	
@app.route('/Introduction1.html')
def introduction1():
	return render_template('Introduction1.html')
@app.route('/References.html')
def reference():	
	return render_template('References.html')
@app.route('/List of experiments.html')
def List_Of_experiments():	
	return render_template('List of experiments.html')
@app.route('/Target Audience.html')
def Target_audience():
	return render_template('Target Audience.html') 
@app.route('/faq.html')
def faq():
	return render_template('faq.html')

@app.route('/quiz',methods=['POST'])
def quiz():
	cursor = db.cursor()
	ans1 = request.form['ans1']
	ans2 = request.form['ans2']
	ans3 = request.form['ans3']
	ans4 = request.form['ans4']
	if ans1 or ans2 or ans3 or ans4 :
		cursor.execute('''INSERT INTO data(ans1,ans2,ans3,ans4) VALUES(?,?,?,?)''', (ans1,ans2,ans3,ans4))
		db.commit()
		cursor.execute("SELECT * FROM data")
		print(cursor.fetchall());
		return jsonify({'sucess' : 'Response has been recorded'})
	else:
		return jsonify({'error' : 'Please answer atleast one question'})
@app.route('/process',methods=['POST'])
def process():
	ques1 = []
	ques2=[]
	ques1.append(request.form['e0'])
	ques1.append(request.form['e1'])
	ques1.append(request.form['e2'])
	ques1.append(request.form['e3'])
	ques1.append(request.form['e4'])
	ques1.append(request.form['e5'])
	ques1.append(request.form['e6'])	
	ques1.append(request.form['e7'])
	ques1.append(request.form['e8'])
	ques1.append(request.form['e9'])
	ques1.append(request.form['e10'])
	ques1.append(request.form['e11'])
	ques1.append(request.form['e12'])
	ques1.append(request.form['e13'])
	ques1.append(request.form['e14'])
	ques1.append(request.form['e15'])
	ques1.append(request.form['e16'])
	ques1.append(request.form['e17'])
	ques1.append(request.form['e18'])
	ques1.append(request.form['e19'])
	ques1.append(request.form['e20'])
	ques1.append(request.form['e21'])
	ques1.append(request.form['e22'])
	ques1.append(request.form['e23'])
	ques1.append(request.form['e24'])
	ques1.append(request.form['e25'])
	ques1.append(request.form['e26'])
	ques1.append(request.form['e27'])
	ques2.append(request.form['t0'])
	ques2.append(request.form['t1'])
	ques2.append(request.form['t2'])
	ques2.append(request.form['t3'])
	ques2.append(request.form['t4'])
	ques2.append(request.form['t5'])
	ques2.append(request.form['t6'])
	ques2.append(request.form['t7'])
	ques2.append(request.form['t8'])
	ques2.append(request.form['t9'])
	ques2.append(request.form['t10'])
	ques2.append(request.form['t11'])
	ques2.append(request.form['t12'])
	ques2.append(request.form['t13'])
	ques2.append(request.form['t14'])
	ques2.append(request.form['t15'])
	ques2.append(request.form['t16'])
	ques2.append(request.form['t17'])
	ques2.append(request.form['t18'])
	ques2.append(request.form['t19'])
	ques2.append(request.form['t20'])
	ques2.append(request.form['t21'])
	ques2.append(request.form['t22'])
	ques2.append(request.form['t23'])
	ques2.append(request.form['t24'])
	
	for i in range(0,28):
		if ques1[i] and ques1[i]:
			continue;
		else:
			 return jsonify({'error' : 'Please Fill All The Boxes'})	
	for i in range(0,25):
		if ques2[i] and ques2[i]:
			continue;
		else: 
			return jsonify({'error' : 'Please Fill All The Boxes'})		


	answer1=[0,0,0,0,0,1,1,0.5,0.5,1,0,0,0,0,0.5,0.5,0,1,0,0,0,0,0,0,0,1,0,0]
	answer2=[0,0.33,0,0.5,0,0,0,1,0,0,1,0,0,0.5,0,0,0.33,0,0,1,0,0.33,0,0,0]
	check=[-2]
	# print(answer1[5])
	# print(ques1[0])
	f1=0
	f2=0
	for i in range(0,28):
		if answer1[i] != float(ques1[i]):
			check.append("e"+ str(i))
			check[0]=-1
			f1=1
	for i in range(0,25):
		if float(ques2[i]) != answer2[i]:
			check.append("t"+ str(i))
			check[0]=0
			f2=1
	if f1 and f2:
		check[0]=1
	# print(check)
	return jsonify(check)
if __name__  ==  '__main__':
	app.run(debug=True)
