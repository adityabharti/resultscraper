from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from json import dump

dumped_results = []

class detail():
	name = ""
	rollno = ""
	gpa = ""

count = 1
driver = webdriver.Firefox()
driver.get("http://www.nitt.edu/prm/nitreg/ShowRes.aspx")
assert "Result" in driver.title
for i in range(106112001,106112108):
	elem = driver.find_element_by_id("TextBox1")

	elem.send_keys(i)
	elem.send_keys(Keys.RETURN)
	#assert "No results found." not in driver.page_source
	#driver.close()
	driver.implicitly_wait(5)
	try:

		element = driver.find_element_by_id("Dt1")
		all_options = element.find_elements_by_tag_name("option")
		print("Value is: %s" % all_options[1].get_attribute("value"))
		all_options[1].click()


		gpa = driver.find_element_by_id("LblGPA")
		name = driver.find_element_by_id("LblName")
		rollno = driver.find_element_by_id("LblEnrollmentNo")

		obj = detail()
		obj.name = name.text
		obj.rollno = rollno.text
		obj.gpa = gpa.text

		dumped_results.append(obj.__dict__)

		print count
		count = count + 1

	except:
		pass

	driver.back()
	driver.back()

	driver.find_element_by_id("TextBox1").clear()

f = open('result.json','w')
dump(dumped_results, f, indent = 1)
