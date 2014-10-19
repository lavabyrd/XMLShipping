from xml.dom.minidom import Document
doc = Document()

# this should not be in the closing tag
reqshipmentvalidate = doc.createElement('req:ShipmentValidateRequestAP xmlns:req="http://www.dhl.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.dhl.com ship-val-req_AP.xsd"')
doc.appendChild(reqshipmentvalidate)


# <Request>
request = doc.createElement("Request")
reqshipmentvalidate.appendChild(request)

serviceheader = doc.createElement("ServiceHeader")
request.appendChild(serviceheader)

messagetime = doc.createElement("MessageTime")
serviceheader.appendChild(messagetime)
text = doc.createTextNode("time")
messagetime.appendChild(text)

messagereference = doc.createElement("MessageReference")
serviceheader.appendChild(messagereference)
text = doc.createTextNode("Example Message Reference")
messagereference.appendChild(text)

siteid = doc.createElement("SiteID")
serviceheader.appendChild(siteid)
text = doc.createTextNode("User ID")
siteid.appendChild(text)

pword = doc.createElement("Password")
serviceheader.appendChild(pword)
text = doc.createTextNode("PA44word")
pword.appendChild(text)
# </Request>


langcode = doc.createElement("LanguageCode")
reqshipmentvalidate.appendChild(langcode)
text = doc.createTextNode("en")
langcode.appendChild(text)

piecesenab = doc.createElement("PiecesEnabled")
reqshipmentvalidate.appendChild(piecesenab)
text = doc.createTextNode("Y")
piecesenab.appendChild(text)


# <Billing>
billing = doc.createElement("Billing")
reqshipmentvalidate.appendChild(billing)

shipperaccountnum = doc.createElement("ShipperAccountNumber")
billing.appendChild(shipperaccountnum)
text = doc.createTextNode("96000111")
shipperaccountnum.appendChild(text)

shippingpaymenttype = doc.createElement("ShippingPaymentType")
billing.appendChild(shippingpaymenttype)
text = doc.createTextNode("S")
shippingpaymenttype.appendChild(text)

billingaccountnum = doc.createElement("BillingAccountNumber")
billing.appendChild(billingaccountnum)
text = doc.createTextNode("96000111")
billingaccountnum.appendChild(text)

dutypaymenttype = doc.createElement("DutyPaymentType")
billing.appendChild(dutypaymenttype)
text = doc.createTextNode("R")
dutypaymenttype.appendChild(text)

dutyaccountnum = doc.createElement("DutyAccountNumber")
billing.appendChild(dutyaccountnum)
text = doc.createTextNode("96000111")
dutyaccountnum.appendChild(text)
# </Billing>


# <Consignee>
consignee = doc.createElement("Consignee")
reqshipmentvalidate.appendChild(consignee)

cneecompname = doc.createElement("CompanyName")
consignee.appendChild(cneecompname)
text = doc.createTextNode("Cnee company Name")
cneecompname.appendChild(text)

cneeadd1 = doc.createElement("AddressLine")
consignee.appendChild(cneeadd1)
text = doc.createTextNode("Cnee Address Line 1")
cneeadd1.appendChild(text)

cneeadd2 = doc.createElement("AddressLine")
consignee.appendChild(cneeadd2)
text = doc.createTextNode("Cnee Address Line 2")
cneeadd2.appendChild(text)

cneecity = doc.createElement("City")
consignee.appendChild(cneecity)
text =doc.createTextNode("Cnee City")
cneecity.appendChild(text)

cneedivision = doc.createElement("Division")
consignee.appendChild(cneedivision)
text =doc.createTextNode("Cnee division")
cneedivision.appendChild(text)

cneedivcd = doc.createElement("DivisionCode")
consignee.appendChild(cneedivcd)
text =doc.createTextNode("Cnee Division Code")
cneedivcd.appendChild(text)

cneepostcd = doc.createElement("Postalcode")
consignee.appendChild(cneepostcd)
text =doc.createTextNode("Cnee Post Code")
cneepostcd.appendChild(text)

cneecountrycd = doc.createElement("CountryCode")
consignee.appendChild(cneecountrycd)
text =doc.createTextNode("Cnee 2 digit country code")
cneecountrycd.appendChild(text)

cneecountryname = doc.createElement("CountryName")
consignee.appendChild(cneecountryname)
text =doc.createTextNode("Cnee country Name Full")
cneecountryname.appendChild(text)

cneecontactinfo = doc.createElement("Contact")
consignee.appendChild(cneecontactinfo)

cneecontactname = doc.createElement("PersonName")
cneecontactinfo.appendChild(cneecontactname)
text =doc.createTextNode("Cnee Contact Name")
cneecontactname.appendChild(text)

cneephone = doc.createElement("PhoneNumber")
cneecontactinfo.appendChild(cneephone)
text =doc.createTextNode("Cnee Number")
cneephone.appendChild(text)

cneephoneext = doc.createElement("PhoneExtension")
cneecontactinfo.appendChild(cneephoneext)
text =doc.createTextNode("Cnee Phone Extension")
cneephoneext.appendChild(text)

cneefax = doc.createElement("FaxNumber")
cneecontactinfo.appendChild(cneefax)
text =doc.createTextNode("Cnee Fax Number")
cneefax.appendChild(text)

cneetelex = doc.createElement("Telex")
cneecontactinfo.appendChild(cneetelex)
text =doc.createTextNode("Cnee Telex Number")
cneetelex.appendChild(text)

cneeemailform = doc.createElement("Email")
cneecontactinfo.appendChild(cneeemailform)

cneeemailfrom = doc.createElement("From")
cneeemailform.appendChild(cneeemailfrom)
text = doc.createTextNode("Cnee@Cneecompany.com")
cneeemailfrom.appendChild(text)

cneeemailto = doc.createElement("To")
cneeemailform.appendChild(cneeemailto)
text = doc.createTextNode("To@cneecompany.com")
cneeemailto.appendChild(text)

cneeemailcc = doc.createElement("cc")
cneeemailform.appendChild(cneeemailcc)
text = doc.createTextNode("CC@Cneecompany.com")
cneeemailcc.appendChild(text)

cneeemailsub = doc.createElement("Subject")
cneeemailform.appendChild(cneeemailsub)
text = doc.createTextNode("Cnee Email Subject")
cneeemailsub.appendChild(text)

cneereplyto = doc.createElement("ReplyTo")
cneeemailform.appendChild(cneereplyto)
text = doc.createTextNode("Reply@cneecompany.com")
cneereplyto.appendChild(text)

cneeemailbody = doc.createElement("Body")
cneeemailform.appendChild(cneeemailbody)
text = doc.createTextNode("Cnee Email Body")
cneeemailbody.appendChild(text)
# </Consignee>



filename = "ship.xml"
f = open(filename, "w")
f.write(doc.toprettyxml (indent = "	"))
f.close()