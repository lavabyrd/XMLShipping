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


filename = "ship.xml"
f = open(filename, "w")
f.write(doc.toprettyxml (indent = "	"))
f.close()