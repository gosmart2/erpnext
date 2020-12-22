from __future__ import unicode_literals
import frappe,json,os,base64

@frappe.whitelist()
def create_data(doc,doc1,doc2,doc3,doc4,doc5,ap_post,name,email,fname,occ,date,age,gen,bg,reli,com,mar,spo,place,add,add1,expect,qus,qus1,qus2,qus3,qus4,qus5,uanno,esino,aadharcer,passcer,pancer,votercer,rationcer,dricer,birthcer,place1,date1,sign):
	data = frappe.new_doc("Job Applicant")
	data.applicant_name = name
	data.applicant_post = ap_post
	data.email_id=email
	data.father_name = fname
	data.occupation = occ
	data.date_of_birth = date
	data.age=age
	data.gender=gen
	data.blood_group=bg
	data.religion =reli
	data.community=com
	data.marital_status=mar
	data.spouse_name=spo
	data.place_of_birth=place
	data.present_address=add
	data.permanant_address=add1	
	data.expected_salary=expect
	data.qus=qus
	data.qus1=qus1
	data.qus2=qus2
	data.qus3=qus3
	data.qus4=qus4
	data.qus5=qus5
	data.uan_no=uanno
	data.esi_no=esino
	data.aadhar_card=aadharcer
	data.passport=passcer
	data.pancard=pancer
	data.voterid=votercer
	data.rationcard=rationcer
	data.driving_license=dricer
	data.birth_certificate=birthcer
	data.place=place1
	data.date=date1
	data.signature=sign
	new=json.loads(doc)
	for s in range(len(new)):
		data.append('guadian', {
		"parent_name": new[s]["name"],
		"date_of_birth":new[s]["dob"],
		"education":new[s]["education"],
		"occupation":new[s]["occupation"],
		"relation":new[s]["relation"],
		"age":new[s]["age"],
		"depends_you":new[s]["depends"]
		})

	new1=json.loads(doc1)
	for s1 in range(len(new1)):
		data.append('internship_training', {
		"starting_date": new1[s1]["from"],
		"ending_date":new1[s1]["to"],
		"nature_of_training":new1[s1]["nature"],
		"instituteorganization":new1[s1]["organization"]
		})

	new2=json.loads(doc2)
	for s2 in range(len(new2)):
		data.append('education', {
		"starting_date": new2[s2]["edufrom"],
		"ending_date":new2[s2]["eduto"],
		"course":new2[s2]["educo"],
		"board":new2[s2]["edubo"],
		"schoolcollege_name":new2[s2]["edusc"],
		"degree":new2[s2]["edudeg"],
		"specialization":new2[s2]["eduspe"],
		"cgpa_or_":new2[s2]["educg"]
		})	

	new3=json.loads(doc3)
	for s3 in range(len(new3)):
		data.append('training_project', {
		"starting_date": new3[s3]["profrom"],
		"ending_date":new3[s3]["proto"],
		"nature_of_training":new3[s3]["pronature"],
		"instituteorganization":new3[s3]["proorganization"]
		})

	new4=json.loads(doc4)
	for s4 in range(len(new4)):
		data.append('language', {
		"languages": new4[s4]["language"],
		"read":new4[s4]["read"],
		"write":new4[s4]["write"],
		"speak":new4[s4]["speak"]
		})

	new5=json.loads(doc5)
	for s5 in range(len(new5)):
		data.append('experiance', {
		"starting_date": new5[s5]["staexp"],
		"ending_date":new5[s5]["endexp"],
		"company_name":new5[s5]["comexp"],
		"designation":new5[s5]["desexp"],
		"department":new5[s5]["depexp"],
		"take_home":new5[s5]["takeexp"],
		"gross":new5[s5]["groexp"],
		"ctc":new5[s5]["ctcexp"]
		})

	frappe.msgprint("Job Application Submitted Successfully")
	data.save()
	frappe.db.commit()
       
		


		
