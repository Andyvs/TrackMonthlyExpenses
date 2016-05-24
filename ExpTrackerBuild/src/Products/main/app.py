from OFS.Folder import Folder
from App.special_dtml import HTMLFile
from zope.interface import Interface
import json
import datetime

class MyTracker(Folder):
    meta_type = "MyTracker"
    index_html = HTMLFile("views/index_html", globals())

    def mainPage(self):
    	"""
    	Redirection to Login Page
    	"""
    	main_html = self.views.main
    	return main_html(standard_html_header='', standard_html_footer='')

    def loginPage(self):
        """
        Redirection to Login Page
        """
        login_html = self.views.login
        return login_html(standard_html_header='', standard_html_footer='')

    def registerPage(self):
        """
        Redirection to Register Page
        """
        register_html = self.views.register
        return register_html(standard_html_header='', standard_html_footer='')

    def reportsPage(self):
        """
        Redirection to Register Page
        """
        reports_html = self.views.report
        return reports_html(standard_html_header='', standard_html_footer='')

    def validateLogin(self):
    	"""
    	Login Validation
    	"""
        request = self.REQUEST
    	USER_ID = request.USER_ID
    	PASSWORD = request.PASSWORD

        existinguser = self.zsqls.selectUser(USER_ID=USER_ID)

        if existinguser:
            if existinguser[0]['USER_ID'] == USER_ID and existinguser[0]['PASSWORD'] == PASSWORD:
                if existinguser[0]['role'] == 'Y':
                    report_html = HTMLFile("views/generatUserReports", globals())
                    return report_html(standard_html_header='', standard_html_footer='',USER_ID=USER_ID)
                else:
                    item_list = self.views.itemlist
                    return item_list(standard_html_header='', standard_html_footer='', USER_ID=USER_ID)
        else:
            return "User does not exists. Please Register."


    def validateRegister(self):
    	"""
    	"""
    	request = self.REQUEST

        USER_ID = request.userid
        FIRST_NAME = request.fname
        LAST_NAME = request.lname
        DOB = request.dob
        GENDER = request.gender
        PASSWORD = request.password
        ADMIN = request.admin

        existinguser = self.zsqls.selectUser(USER_ID=USER_ID)

        if existinguser:
            return "UserID is already Exist. Please Create new user"
        else:
            self.zsqls.insertUserDetails(USER_ID=USER_ID,
                                                    FIRST_NAME=FIRST_NAME,
                                                    LAST_NAME=LAST_NAME,
                                                    DOB=DOB,
                                                    GENDER=GENDER,
                                                    PASSWORD=PASSWORD,
                                                    ADMIN=ADMIN)

            login_html = self.views.login
            return login_html(standard_html_header='', standard_html_footer='')

    def savePurchase(self):
        """
        """
        request = self.REQUEST

        USER_ID = request.USER_ID
        product = request.product
        quantity = int(request.quantity)
        unitprice = int(request.unitprice)
        date = datetime.date.today()
        self.zsqls.insertItem(USER_ID=USER_ID,
                                product=product,
                                quantity=quantity,
                                unitprice=unitprice,
                                date=date)
    def reportPage(self):
        """
        """
        request = self.REQUEST
        jsonObj = json.loads(request['userid'])
        user_id = str(jsonObj[0])
        getreport = self.zsqls.selectMyPurchase(user_id=user_id)

        report_html = HTMLFile("views/report", globals())
        return report_html(standard_html_header='', standard_html_footer='', getreport=getreport)

    def generateReports(self):
        """
        """
        request = self.REQUEST
        jsonObj = json.loads(request['repObj'])
        user_id = str(jsonObj[0])
        product = str(jsonObj[1])
        start_date = str(jsonObj[2])
        end_date = str(jsonObj[3])
        getreport = self.zsqls.selectMonthlyReport(user_id=user_id,
                                                   product=product,
                                                   start_date=start_date,
                                                   end_date=end_date)

        report_html = HTMLFile("views/report", globals())
        return report_html(standard_html_header='', standard_html_footer='', getreport=getreport)

manage_addMyTracker = HTMLFile("views/manage_addMyTracker_form", globals())

def addMyTracker(self, id):
	"""
	"""
	self._setObject(id, MyTracker(id))
	return "My Tracker added."



