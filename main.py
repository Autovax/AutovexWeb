from flask import Flask, request, render_template, url_for, redirect, send_file, Response, Markup, abort, jsonify
import time
import threading
app = Flask(__name__,static_folder='static')


def loop():
	while True:
		time.sleep(1)
		for i in virusDatabase:
			if i["percentComplete"]<100:
				i["percentComplete"]=i["percentComplete"]+1




virusDatabase=[]

tdTemplateSucc="""

 <tr>
										<th scope="row">
											<div class="media align-items-center">
												<a href="#" class="avatar rounded-circle mr-3">
													<img alt="Image placeholder" src="https://image.flaticon.com/icons/png/512/139/139315.png">
												</a>
												<div class="media-body">
													<a href="{}"><span class="name mb-0 text-sm">{}</span>
												</div>
											</div>
										</th>
										<!--<td class="budget">
											$2500 USD
										</td>-->
										<td>
											<span class="badge badge-dot mr-4">
												<i class="bg-success"></i>
												<span class="status">completed</span>
											</span>
										</td>
										<!--<td>
											<div class="avatar-group">
												<a href="#" class="avatar avatar-sm rounded-circle" data-toggle="tooltip" data-original-title="Ryan Tompson">
													<img alt="Image placeholder" src="static/dashboard/assets/img/theme/team-1.jpg">
												</a>
												<a href="#" class="avatar avatar-sm rounded-circle" data-toggle="tooltip" data-original-title="Romina Hadid">
													<img alt="Image placeholder" src="static/dashboard/assets/img/theme/team-2.jpg">
												</a>
												<a href="#" class="avatar avatar-sm rounded-circle" data-toggle="tooltip" data-original-title="Alexander Smith">
													<img alt="Image placeholder" src="static/dashboard/assets/img/theme/team-3.jpg">
												</a>
												<a href="#" class="avatar avatar-sm rounded-circle" data-toggle="tooltip" data-original-title="Jessica Doe">
													<img alt="Image placeholder" src="static/dashboard/assets/img/theme/team-4.jpg">
												</a>
											</div>
										</td>-->
										<td>
											<div class="d-flex align-items-center">
												<span class="completion mr-2">100%</span>
												<div>
													<div class="progress">
														<div class="progress-bar bg-success" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width: 100%;"></div>
													</div>
												</div>
											</div>
										</td>
										</tr>

										"""


tdTemplateProg="""

									 <tr>
										<th scope="row">
											<div class="media align-items-center">
												<a href="#" class="avatar rounded-circle mr-3">
													<img alt="Image placeholder" src="https://image.flaticon.com/icons/png/512/139/139315.png">
												</a>
												<div class="media-body">
													<span class="name mb-0 text-sm">{}</span>
												</div>
											</div>
										</th>
										<!--<td class="budget">
											$2500 USD
										</td>-->
										<td>
											<span class="badge badge-dot mr-4">
												<i class="bg-warning"></i>
												<span class="status">processing</span>
											</span>
										</td>
										<!--<td>
											<div class="avatar-group">
												<a href="#" class="avatar avatar-sm rounded-circle" data-toggle="tooltip" data-original-title="Ryan Tompson">
													<img alt="Image placeholder" src="static/dashboard/assets/img/theme/team-1.jpg">
												</a>
												<a href="#" class="avatar avatar-sm rounded-circle" data-toggle="tooltip" data-original-title="Romina Hadid">
													<img alt="Image placeholder" src="static/dashboard/assets/img/theme/team-2.jpg">
												</a>
												<a href="#" class="avatar avatar-sm rounded-circle" data-toggle="tooltip" data-original-title="Alexander Smith">
													<img alt="Image placeholder" src="static/dashboard/assets/img/theme/team-3.jpg">
												</a>
												<a href="#" class="avatar avatar-sm rounded-circle" data-toggle="tooltip" data-original-title="Jessica Doe">
													<img alt="Image placeholder" src="static/dashboard/assets/img/theme/team-4.jpg">
												</a>
											</div>
										</td>-->
										<td>
											<div class="d-flex align-items-center">
												<span class="completion mr-2">{}%</span>
												<div>
													<div class="progress">
														<div class="progress-bar bg-warning" role="progressbar" aria-valuenow="{}" aria-valuemin="0" aria-valuemax="100" style="width: {}%;"></div>
													</div>
												</div>
											</div>
										</td>
										<!--<td class="text-right">
											<div class="dropdown">
												<a class="btn btn-sm btn-icon-only text-light" href="#" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
													<i class="fas fa-ellipsis-v"></i>
												</a>
												<div class="dropdown-menu dropdown-menu-right dropdown-menu-arrow">
													<a class="dropdown-item" href="#">Action</a>
													<a class="dropdown-item" href="#">Another action</a>
													<a class="dropdown-item" href="#">Something else here</a>
												</div>
											</div>
										</td>-->
									</tr>

										"""



@app.route("/")
def index():
	return render_template("index.html")

@app.route("/dashboard")
def dashboard():
	return render_template("dashboard.html")

@app.route("/addVirus",methods=['POST'])
def addVirus():
	virusName=request.form["virusName"]
	if virusName=="":
		return "Error: Please Fill In Name"
	virusDatabase.append({"virusName":virusName,"stat":"processing","percentComplete":0})
	return redirect(url_for("treatements"))





@app.route("/treatments")
def treatements():
	content=""
	for i in virusDatabase:
		if i["percentComplete"]<100:
			content+=tdTemplateProg.format(i["virusName"],i["percentComplete"],i["percentComplete"],i["percentComplete"])
		else:
			content+=tdTemplateSucc.format("http://ec2-54-166-13-51.compute-1.amazonaws.com/treatmentDetail?ID=2por",i["virusName"])
	print(content)
	print(virusDatabase)
	return render_template("treatments.html",trContent=content)
@app.route("/treatmentDetail")
def treatementDetail():
	treatementID = request.args.get('ID')
	return render_template("treatmentDetail.html",mmdbid=treatementID)


t = threading.Thread(target=loop)
t.start()
app.run(host="0.0.0.0",port=80,threaded=True,debug=True)
